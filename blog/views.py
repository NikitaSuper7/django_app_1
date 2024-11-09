from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import BlogPostsModel
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy, reverse


# Create your views here.

class BlogLIstView(ListView):
    model = BlogPostsModel
    template_name = "blog/articles_list.html"
    context_object_name = 'articles'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_publicated=True)


class BlogCreateView(CreateView):
    model = BlogPostsModel
    fields = ["title", "text", "image", "is_publicated"]
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy('blog:articles_list')


class BlogDetailView(DetailView):
    model = BlogPostsModel
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = BlogPostsModel
    fields = ["title", "text", "image", "is_publicated"]
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy('blog:articles_list')

    def get_success_url(self):
        return reverse("blog:article_detail", args=[self.kwargs.get("pk")])


class BlogDeleteView(DeleteView):
    model = BlogPostsModel
    template_name = 'blog/article_confirm_delete.html'
    success_url = reverse_lazy('blog:articles_list')
    context_object_name = 'book'
