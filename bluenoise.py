import random
import math

def generate_blue_noise(num_points):
    points = []
    min_dist = math.sqrt(math.pi) / (8 * math.sqrt(num_points))

    # Generate the first point randomly
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    points.append((x, y))

    while len(points) < num_points:
        # Generate a new point randomly within the annulus around the previous point
        r1 = random.uniform(min_dist, 2*min_dist)
        r2 = random.uniform(0, 2*math.pi)
        x = points[-1][0] + r1 * math.cos(r2)
        y = points[-1][1] + r1 * math.sin(r2)

        # Check that the new point is not too close to any existing points
        too_close = False
        for p in points:
            if math.sqrt((x-p[0])**2 + (y-p[1])**2) < min_dist:
                too_close = True
                break
        if not too_close:
            points.append((x, y))

    return points
for vec in generate_blue_noise(64):
  print("glm::vec2",vec,",")