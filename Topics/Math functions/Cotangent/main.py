import math

angle = int(input())
angle_rad = math.radians(angle)
cotangent_angle = math.cos(angle_rad) / math.sin(angle_rad)
print(round(cotangent_angle, 10))
