from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('blog/<int:year>/<int:month>/<int:pk>/', views.blog_details, name="blog_details"),
    path('blog/category/<str:slug>/', views.categories, name="categories"),
    path('blog/tag/<str:slug>/', views.tags, name="tag"),
]
