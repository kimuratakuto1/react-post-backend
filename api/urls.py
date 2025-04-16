from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    get_csrf_token, 
    PostViewSet, 
    login_view, 
    logout_view, 
    current_user_view
)

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('csrf/', get_csrf_token),      # ← ここを残すなら下の 'csrf/' は削除
    path('', include(router.urls)),
    path('login/', login_view),
    path('logout/', logout_view),
    path('me/', current_user_view),
]

