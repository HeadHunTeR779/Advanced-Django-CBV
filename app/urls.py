from django.conf.urls import url
from app import views

app_name = 'app'


urlpatterns = [
    url(r'^$',views.SchoolListView.as_view(), name="list"),
    #url(r'^detail/$',views.SchoolDetailView.as_view(), name="detail"),
]
