from django.urls import path
from .views import CovenListView, CovenDetailView, CovenCreateView, CovenUpdateView, CovenDeleteView

urlpatterns = [
    path('', CovenListView.as_view(), name='coven_list'),
    path('<int:pk>/', CovenDetailView.as_view(), name='coven_detail'),
    path('create/', CovenCreateView.as_view(), name='coven_create'),
    path('<int:pk>/update/', CovenUpdateView.as_view(), name='coven_update'),
    path('<int:pk>/delete/', CovenDeleteView.as_view(), name='coven_delete'),
]