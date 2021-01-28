from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import *


class PostView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context
