from rest_framework.routers import DefaultRouter
from .views import NoteCategoryModelViewSet, NoteModelViewSet, NotesCategoriesModelViewSet

router = DefaultRouter()

router.register("note-category", NoteCategoryModelViewSet)
router.register("notes", NoteModelViewSet)
router.register("note/categories", NotesCategoriesModelViewSet)

urlpatterns = [] + router.urls