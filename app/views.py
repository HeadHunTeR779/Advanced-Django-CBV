from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse
from . import models


class SchoolListView(ListView):
    model = models.School

class SchoolDetailView(DetailView):
    model = model.School
    template_name = "app/school_detail.html"
