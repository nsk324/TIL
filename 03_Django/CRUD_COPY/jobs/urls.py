from django.urls import path
from . import views

app_name = 'job'
urlpatterns=[
    path('', views.index, name='index'),
    path('past_life/',views.past_life, name="past_life"),
]                       