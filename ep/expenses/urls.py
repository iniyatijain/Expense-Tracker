from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('budget/', views.budget_view, name='budget'), 
    path('addexpensepage/', views.addexpensepage, name='addexpensepage') ,
    path('addexpense/', views.addexpense_view, name='addexpense'),
    path('editexpense/<int:id>/',views.editexpense_view, name="editexpense"),
    path('deleteexpense/<int:id>/',views.deleteexpense_view, name="deleteexpense"),
   
]