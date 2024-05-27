from django.urls import path

from .views import EstateListView, EstateDetailView

urlpatterns = [
    path('estates/', EstateListView.as_view(), name='estate-list'),
    path('estates/<int:pk>/', EstateDetailView.as_view(), name='estate-detail')
]
