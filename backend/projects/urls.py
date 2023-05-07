from django.urls import path
from .views import ProjectDetailView
urlpatterns = [
    path('project-list/', ProjectDetailView.as_view())
]
