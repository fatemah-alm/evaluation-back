from django.urls import path
from .views import JudgeListView, JudgeDetailView


urlpatterns = [
    path('', JudgeListView.as_view(), name='judge-list'),
    path('<int:id>', JudgeDetailView.as_view(), name='judge-detail' ),

]