from django.urls import path
from . import views

urlpatterns = [
    path('', views.sample_list, name="sample_list"),
    path('upload/', views.upload, name="upload"),
    path('samples/<int:pk>', views.sample_detail, name="sample_detail"),
    path('samples/upload/', views.upload_sample, name='upload_sample'),
    path('sampless/<int:pk>/edit', views.edit_sample, name="edit_sample"),

]
