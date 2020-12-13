from django.shortcuts import render, redirect
from .models import *
from .forms import CommentForm


def blog(request):
    page_title = 'Blog'
    posts = Post.objects.all()

    recent_posts = Post.objects.all()[:2]
    context = {
        'posts': posts,
        'recent_posts': recent_posts,
        'page_title': page_title

    }
    return render(request, 'blog/blog.html', context)


# Create your views here.


def blog_details(request, year, month, pk):

    post = Post.objects.get(id=pk)
    post_tags = post.tags.all()
    post_comments = post.comments.filter(allowed=True)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    recent_posts = Post.objects.all()[:3]

    user_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            return redirect('/' + f'blog/{post.published.year}/{post.published.month}/{post.id}/')
    else:
        comment_form = CommentForm()

    if post.status == 'Published':
        context = {
            'post': post,
            'categories': categories,
            'tags': tags,
            'post_tags': post_tags,
            'recent_posts': recent_posts,
            'comments': post_comments,
            'comment_form': comment_form,
            'user_comment': user_comment

        }

        return render(request, 'blog/blog_details.html', context)
    else:
        return redirect('/')


def categories(request, slug):
    posts = Post.objects.filter(cats__slug=slug)
    category = Category.objects.get(slug=slug)

    if posts:

        context = {
            'posts': posts,
            'category': category,
        }
        print(slug, category)
        return render(request, 'blog/categories.html', context)
    else:
        return redirect('blog')


def tags(request, slug):
    posts = Post.objects.filter(tags__slug=slug)
    tag = Tag.objects.get(slug=slug)
    if posts:
        context = {
            'posts': posts,
            'tag': tag,
        }
        return render(request, 'blog/tags.html', context)
    else:
        return redirect('blog')
