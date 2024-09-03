from django.urls import path
from . import views

urlpatterns = [
    path("", views.portfolio, name = "portfolio"),
    path('<int:pk>', views.DetailView.as_view(), name='portf-art')
    
] 

