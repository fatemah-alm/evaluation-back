from django.urls import path
from .views import CriteriaListView, CriteriaDetailView 


urlpatterns = [
    path('', CriteriaListView.as_view(), name='criteria-list'),
    path('<int:id>', CriteriaDetailView.as_view(), name='criteria-detail' ),

]