from django.urls import path
from .views import TeamsDetailView, TeamsListView


urlpatterns = [
    path('', TeamsListView.as_view(), name='team-list'),
    path('<int:id>', TeamsDetailView.as_view(), name='team-detail' ),

]