from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    Q = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    total = 0
    while Q:
        time += 1
        a = Q.popleft()
        if a:
            total -= a
        if truck_weights:
            if total + truck_weights[0] <= weight:
                total += truck_weights[0]
                Q.append(truck_weights.popleft())
            else:
                Q.append(0)
    
    return time

print(solution(2, 10, [7,4,5,6]))
#print(solution(100, 100, [10]))
