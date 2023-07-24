from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import GroupViewSet, PostViewSet, CommentViewSet


v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register('groups', GroupViewSet, basename='groups')
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/api-token-auth/jwt/', include('djoser.urls.jwt')),
]