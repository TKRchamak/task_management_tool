from django.urls import path
from .views import ProjectDetailListCreate
urlpatterns = [
    path('project-list/', ProjectDetailListCreate.as_view()),
]
