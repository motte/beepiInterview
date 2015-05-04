from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class IndexTwoView(TemplateView):
    template_name = 'index3.html'


class IndexThreeView(TemplateView):
    template_name = 'index2.html'


class IndexFourView(TemplateView):
    template_name = 'index-animations.html'