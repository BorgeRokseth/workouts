from django.urls import path

from . import views

urlpatterns = [
    path('', views.EquipmentListView.as_view(), name='equipment_list'),
    path('<int:pk>/', views.EquipmentDetailView.as_view(), name='equipment_details')
]