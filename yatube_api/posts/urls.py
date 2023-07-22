from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import GroupViewSet, PostViewSet, CommentViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comments')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/api-token-auth/', include('djoser.urls')),
    path('api/v1/api-token-auth/jwt/', include('djoser.urls.jwt')),
]
