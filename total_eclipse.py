
n = int(input())

planets = []

for i in range(n):
    distance, diameter, angle = map(float, input().split())

    left = angle - diameter / 2
    right = angle + diameter / 2

    planets.append((distance, left, right))

# Sort planets by distance (closest first)
planets.sort()

shadows = []
eclipsed = 0

for distance, left, right in planets:

    # Check if the planet is completely covered
    covered_until = left

    for start, end in shadows:
        if start > covered_until + 1e-10:
            break

        covered_until = max(covered_until, end)

        if covered_until >= right - 1e-10:
            eclipsed += 1
            break

    # Add this planet's shadow
    shadows.append([left, right])
    shadows.sort()

print(eclipsed)
