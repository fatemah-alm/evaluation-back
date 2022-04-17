from django.urls import path
from .views import SemesterListView

urlpatterns = [
    path('', SemesterListView.as_view(), name='semester-list')
]