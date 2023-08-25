from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # 127.0.0.1:8000
    path('add/', views.add, name='add'), # 127.0.0.1:8000/add
    path('delete/<int:pk>', views.delete, name='delete'), # 127.0.0.1:8000/delete
    path('update/<int:pk>', views.update, name='update'), # 127.0.0.1:8000/update/5
]

