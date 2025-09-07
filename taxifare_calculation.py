BASE_FARE = 50
PER_KM_FARE = 10
def calculate_fare(distance):
    return BASE_FARE + (PER_KM_FARE * distance)
n = int(input("Enter number of trips: "))
trips = []

for i in range(n):
    distance = float(input(f"Enter distance for trip {i+1} (in km): "))
    trips.append(distance)

total_fare = 0
for i, distance in enumerate(trips, 1):
    fare = calculate_fare(distance)
    print(f"Trip {i}: ${fare}")
    total_fare += fare

print(f"Total Fare: ${total_fare}")
