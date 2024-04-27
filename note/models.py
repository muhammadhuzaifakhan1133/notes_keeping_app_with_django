from user.models import UserModel
from django.db import models

class NoteCategoryModel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now=True)

class NoteModel(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    category = models.ManyToManyField(NoteCategoryModel, through="NotesCategoriesModel")

    class Meta:
        indexes = [
            models.Index(fields=["user_id"])
        ]

class NotesCategoriesModel(models.Model):
    note = models.ForeignKey(NoteModel, on_delete=models.CASCADE)
    category = models.ForeignKey(NoteCategoryModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('note', 'category')
