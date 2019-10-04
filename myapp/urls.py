from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListView.as_view(), name="list"),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
]
