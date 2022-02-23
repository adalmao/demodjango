from django.urls import path
from panel import views

app_name = "panel"

urlpatterns = [
    path('',views.home,name="home"),
    path('edit/<int:code>/',views.edit,name="edit"),
    path('delete/<int:code>/',views.delete,name="delete"),
    path('list/',views.list,name="list"),
]
