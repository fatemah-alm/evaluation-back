from django.urls import path
from .views import EvaluationView, EvaluationDetailView


urlpatterns = [
    path('', EvaluationView.as_view(), name='evaluation-list'),
    path('<int:id>', EvaluationDetailView.as_view(), name='evaluation-detail' ),

]