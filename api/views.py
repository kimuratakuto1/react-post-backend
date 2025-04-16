from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from rest_framework import generics,viewsets,permissions
from .serializers import PostSerializer
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
import json
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.middleware.csrf import get_token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user_view(request):
    return JsonResponse({'username': request.user.username})

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "ログイン成功"})
        else:
            return JsonResponse({"error": "認証失敗"}, status=401)

@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({"message": "ログアウトしました"})

@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'detail': 'CSRF cookie set'})

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
