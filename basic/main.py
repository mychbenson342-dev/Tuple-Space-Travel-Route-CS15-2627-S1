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