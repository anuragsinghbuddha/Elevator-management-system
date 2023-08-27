# urls.py

from django.urls import path
from .views import InitializeElevators, ElevatorRequests, NextDestination, ElevatorDirection, SaveRequest, ElevatorMaintenance, ElevatorDoor

urlpatterns = [
    path('initialize-elevators/', InitializeElevators.as_view(), name='initialize_elevators'),
    path('elevator-requests/<int:elevator_id>/', ElevatorRequests.as_view(), name='elevator_requests'),
    path('next-destination/<int:elevator_id>/', NextDestination.as_view(), name='next_destination'),
    path('elevator-direction/<int:elevator_id>/', ElevatorDirection.as_view(), name='elevator_direction'),
    path('save-request/', SaveRequest.as_view(), name='save_request'),
    path('elevator-maintenance/<int:elevator_id>/', ElevatorMaintenance.as_view(), name='elevator_maintenance'),
    path('elevator-door/<int:elevator_id>/<str:action>/', ElevatorDoor.as_view(), name='elevator_door'),
]

