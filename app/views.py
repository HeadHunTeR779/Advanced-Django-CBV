from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):          #This name is compulsory!
        context_dict = super().get_context_data(**kwargs)
        context_dict['stuff'] = "Injecting From TemplateView"
        return context_dict
