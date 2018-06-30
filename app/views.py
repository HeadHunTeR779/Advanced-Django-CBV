from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse
from . import models



class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    model = models.School
    #it takes the model then lower cases everything and adds _list in the end so we have school_list
    #if you wanna bypass this then use the following cmd
    context_object_name = "schools"

    #also the template it wants is school_list.html so this file name is also compulsory

class SchoolDetailView(DetailView):
    context_object_name = "school_detail" #default is just school it just lowercases everything thats it!
    model = models.School
    template_name = "app/school_detail.html"
