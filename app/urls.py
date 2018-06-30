from django.conf.urls import url
from app import views

app_name = 'app'


urlpatterns = [
    url(r'^$',views.SchoolListView.as_view(), name="list"),
    url(r'^(?P<pk>\d+)/$',views.SchoolDetailView.as_view(), name="detail"),   #necessarily the guy should be pk
    url(r'^create/$', views.SchoolCreateView.as_view(), name="create"),
    url(r'^update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name="update"),
    url(r'^delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name="delete"),
]
