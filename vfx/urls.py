from django.urls import path
from . import views
urlpatterns=[
    path('',views.vfx_post,name="vfx")

]