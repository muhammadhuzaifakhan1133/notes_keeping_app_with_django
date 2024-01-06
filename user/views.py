from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from .models import UserModel
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.request import Request

class IsSuperuser(BasePermission):
    def has_permission(self, request: Request, view):
        user: UserModel = request.user
        if user and user.is_superuser:
            return True
        return False

class UserModelViewSet(ModelViewSet):
    permission_classes = [IsSuperuser]
    authentication_classes = [JWTAuthentication]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer