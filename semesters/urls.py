from django.urls import path
from .views import SemesterListView, SemesterDetailView

urlpatterns = [
    path('', SemesterListView.as_view(), name='semester-list'),
    path('<int:id>', SemesterDetailView.as_view(), name='semester-detail' ),
    
]