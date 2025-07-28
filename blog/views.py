from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    categorias = {
        'recurrencia': 'Recurrencia y árboles',
        'fundamentos': 'Fundamentos de programación',
        'arreglos': 'Arreglos',
        'poo': 'Programación orientada a objetos',
        'micro': 'Microeconomía',
    }

    posts_por_categoria = {
        nombre_visible: Post.objects.filter(category=clave).order_by('-created_at')
        for clave, nombre_visible in categorias.items()
    }

    return render(request, 'blog/post_list.html', {'posts_por_categoria': posts_por_categoria})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
