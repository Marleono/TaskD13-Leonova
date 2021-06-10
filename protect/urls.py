from django.urls import path
from .views import IndexView


urlpatterns = [
    path('accounts/', IndexView.as_view()),
]