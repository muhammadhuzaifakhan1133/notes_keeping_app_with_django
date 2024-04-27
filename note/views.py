from rest_framework.viewsets import ModelViewSet
from .models import NoteCategoryModel, NoteModel, NotesCategoriesModel
from .serializers import NoteCategorySerializer, NoteSerializer, NotesCategoriesSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class NoteCategoryModelViewSet(ModelViewSet):
    queryset = NoteCategoryModel.objects.all()
    serializer_class = NoteCategorySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class NoteModelViewSet(ModelViewSet):
    queryset = NoteModel.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return NoteModel.objects.filter(user_id=self.request.user.id).all()
    
    def get_serializer(self, *args, **kwargs):
        if self.action == "list" or self.action == "create":
            kwargs["context"] =  {"is_not_detail": True}
        return super().get_serializer(*args, **kwargs)

class NotesCategoriesModelViewSet(ModelViewSet):
    queryset = NotesCategoriesModel.objects.all()
    serializer_class = NotesCategoriesSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        note_id = self.request.GET.get("note_id", None)
        if not note_id:
            return Response({"note_id": ["This parameter is required"]}, status=status.HTTP_400_BAD_REQUEST)
        return NotesCategoriesModel.objects.filter(note_id=2).all()
