from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Elevator
from .serializers import RequestSerializer
from .models import Request





class InitializeElevators(APIView):
    def post(self, request):
        n = request.data.get('n')  # Get the value of 'n' from the request data
        print(n)
        
        if n is None or not isinstance(n, int) or n <= 0:
            return Response({'message': 'Invalid value for n'}, status=400)
        
        created_elevators = []
        
        for _ in range(n):
            elevator = Elevator.objects.create()  # Create an elevator instance
            created_elevators.append(elevator)
        
        return Response({'message': f'{n} elevators created successfully'})

    


class ElevatorRequests(APIView):
    def get(self, request, elevator_id):
        try:
            requests = Request.objects.filter(elevator_id=elevator_id)  # Get all requests for the elevator
        except Request.DoesNotExist:
            return Response({'message': 'Elevator requests not found'}, status=404)
        
        serializer = RequestSerializer(requests, many=True)  # Serialize the requests
        
        return Response(serializer.data)

    
  




class NextDestination(APIView):
    def get(self, request, elevator_id):
        try:
            elevator = Elevator.objects.get(pk=elevator_id)  # Get the elevator instance
        except Elevator.DoesNotExist:
            return Response({'message': 'Elevator not found'}, status=404)
        
        # Calculate the next destination floor based on elevator's current floor and direction
        next_destination = elevator.current_floor
        
        if elevator.moving_up:
            next_destination += 1
        else:
            next_destination -= 1
        
        return Response({'next_destination': next_destination})




class ElevatorDirection(APIView):
    def get(self, request, elevator_id):
        try:
            elevator = Elevator.objects.get(pk=elevator_id)  # Get the elevator instance
        except Elevator.DoesNotExist:
            return Response({'message': 'Elevator not found'}, status=404)
        
        is_moving_up = elevator.moving_up
        
        return Response({'moving_up': is_moving_up})





class SaveRequest(APIView):
    def post(self, request):
        floor = request.data.get('floor')
        direction = request.data.get('direction')
        
        if not all([floor, direction]):
            return Response({'message': 'Missing required data'}, status=400)
        
        # Find an available elevator that is closest to the requested floor
        elevators = Elevator.objects.filter(operational=True)
        best_elevator = None
        min_distance = float('inf')
        
        for elevator in elevators:
            distance = abs(int(elevator.current_floor )- int(floor))
            if distance < min_distance:
                best_elevator = elevator
                min_distance = distance
        
        if best_elevator is None:
            return Response({'message': 'No available elevators'}, status=404)
        
        # Create a request for the chosen elevator
        request_instance = Request.objects.create(
            elevator=best_elevator,
            floor=floor,
            direction=direction
        )
        
        return Response({'message': 'Request saved successfully'})


class ElevatorMaintenance(APIView):
    def put(self, request, elevator_id):
        try:
            elevator = Elevator.objects.get(pk=elevator_id)  # Get the elevator instance
        except Elevator.DoesNotExist:
            return Response({'message': 'Elevator not found'}, status=404)
        
        elevator.operational = False  # Mark the elevator as not operational
        elevator.save()
        
        return Response({'message': 'Elevator marked as not working'})




class ElevatorDoor(APIView):
    def put(self, request, elevator_id, action):
        if action not in ['open', 'close']:
            return Response({'message': 'Invalid action'}, status=400)
        
        try:
            elevator = Elevator.objects.get(pk=elevator_id)  # Get the elevator instance
        except Elevator.DoesNotExist:
            return Response({'message': 'Elevator not found'}, status=404)
        
        elevator.doors_open = (action == 'open')  # Update the doors_open field based on action
        elevator.save()
        
        return Response({'message': f'Door {action}ed'})
