from django.urls import path, include
from .views import ItemListCreateView, ItemRetrieveView, UserCreateView, whoami

urlpatterns = [
    path('items/', ItemListCreateView.as_view()),
    path('items/<int:pk>/', ItemRetrieveView.as_view()),
    path('users/', UserCreateView.as_view()),
    path('whoami/', whoami, name='whoami'),
    path('', include('django_prometheus.urls')),
]
