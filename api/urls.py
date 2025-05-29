from django.urls import path
from .views import ItemListCreateView, ItemRetrieveView

urlpatterns = [
    path('items/', ItemListCreateView.as_view()),
    path('items/<int:pk>/', ItemRetrieveView.as_view()),
]
