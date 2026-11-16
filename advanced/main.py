mission_route = (
    "Earth",
    "Luna Station",
    "Mars",
    "Europa",
    "Titan",
    "Neptune Station"
)

print(f"mission_route: {mission_route[0]}")
print(f"mission_route: {mission_route[-1]}")

print(len(mission_route))

for mission in mission_route:
    print(mission)

if "Europa" in mission_route:
    print("Europa is included")

while True:
    guess = input("\nEnter your mission: \n")
    if guess in mission_route:
        print("You have entered the mission")
        break

    else:
        print("Wrong input")

stops = mission_route.index(guess)
print(stops)

stops_till_end = len(mission_route) - 1 -stops
print(stops_till_end)

if stops_till_end == 0:
    print("No more stops left")
else:
    stops_right = stops + 1
    print(f"Next destination: {mission_route[stops_right]}")