def decide_direction(current_floor, destination_floor):
    if current_floor < destination_floor:
        return 'up'
    elif current_floor > destination_floor:
        return 'down'
    else:
        return 'stop'

def update_elevator_state(elevator, direction, destination_floor):
    elevator.moving_up = (direction == 'up')
    elevator.current_floor = destination_floor
    elevator.save()

def process_request(elevator, request):
    direction = decide_direction(elevator.current_floor, request.floor)
    update_elevator_state(elevator, direction, request.floor)
    request.completed = True
    request.save()

def assign_elevator(elevators, floor):
    best_elevator = None
    min_distance = float('inf')
    for elevator in elevators:
        distance = abs(elevator.current_floor - floor)
        if distance < min_distance and elevator.operational:
            min_distance = distance
            best_elevator = elevator
    return best_elevator
