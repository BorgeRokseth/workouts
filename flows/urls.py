from django.urls import path

from . import views

urlpatterns = [
    path('', views.FlowListView.as_view(), name='flow_list'),
    path('<int:pk>/', views.FlowDetailView.as_view(), name='flow_details'),
    path('set', views.SetListView.as_view(), name='set_list'),
    path('set/<int:pk>/', views.SetDetailView.as_view(), name='set_details')
]
