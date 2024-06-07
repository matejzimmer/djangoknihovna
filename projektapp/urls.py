from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # přidáváme cestu pro zobrazení indexu
]
