from rest_framework import serializers
from .models import NoteCategoryModel, NoteModel, NotesCategoriesModel
from user.models import UserModel

class NoteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteCategoryModel
        fields = "__all__"

class NoteSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(NoteSerializer, self).__init__(*args, **kwargs)
        
        if "request" in self.context.keys() and self.context['request'].method == "PUT":
            self.fields.pop('category_ids')
        elif "is_not_detail" in self.context.keys() and self.context['is_not_detail'] == True:
            self.fields.pop('category')
            
    category = NoteCategorySerializer(many=True, read_only=True)
    category_ids = serializers.ListField(write_only=True, child=serializers.IntegerField(), allow_empty=False)
    
    class Meta:
        model = NoteModel
        exclude = ["user"]

    def create(self, validated_data):
        user_id = self.context['request'].user.id
        user = UserModel.objects.get(pk=user_id)
        category_ids = validated_data.pop("category_ids", [])
        categories = []
        for catg_id in category_ids:
            category = NoteCategoryModel.objects.filter(id=catg_id).first()
            if not category:
                raise serializers.ValidationError({"categori_ids": [f"Invalid Id {catg_id}"]})
            categories.append(category)
        print(validated_data)
        note = NoteModel.objects.create(**validated_data, user=user)
        if not note:
            raise serializers.ValidationError({"note": ["Something went wrong, Note can't be save"]})
        for category in categories:
            note.category.add(category)
        note.save()
        return note
    
class NotesCategoriesSerializer(serializers.ModelSerializer):
    note = NoteSerializer(many=False)
    class Meta:
        model = NotesCategoriesModel
        fields = ["note"]
        depth = 1
