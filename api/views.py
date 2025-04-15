from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from rest_framework import generics
from .serializers import PostSerializer

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save() # 投稿をデータベースに保存
            return redirect('post_list') # 投稿一覧ページにリダイレクト
    else:
        form = PostForm() # GETリクエストの場合、空のフォールを表示
    return render(request, 'api/create_post.html', {'form: form'})
        
