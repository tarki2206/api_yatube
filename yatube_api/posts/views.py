from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import GroupSerializer, \
    PostSerializer, CommentSerializer
from .models import Group, Post


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
