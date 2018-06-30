from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from . import models



class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):  #TO LIST ALL OBJECTS OF A MODEL
    model = models.School
    #it takes the model then lower cases everything and adds _list in the end so we have school_list
    #if you wanna bypass this then use the following cmd
    context_object_name = "schools"

    #also the template it wants is school_list.html so this file name is also compulsory

class SchoolDetailView(DetailView): #TO SHOW ALL THE DETAILS OF AN OBJECT OF A MODEL
    model = models.School
    context_object_name = "school_detail" #default is just school it just lowercases everything thats it!
    template_name = "app/school_detail.html"


#IT AUTOMATICALLY PASSES THE FORM NAME!!  AND OBJECT NAME IS : form
class SchoolCreateView(CreateView):  #alt to the view which calls forms which take data for a model
    model = models.School
    fields = "__all__"  #or ["name" ,"principal","location"]
    template_name = "app/create_school.html"  #default is school_form.html  is lowercase the model and add _form
    #it looks for the file in the app's folder named templates and under that  put ur shit inside that



#IT AUTOMATICALLY PASSES THE FORM NAME!!  AND OBJECT NAME IS : form
class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ["name","principal"]
    template_name = "app/create_school.html"
