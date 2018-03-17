import math
x = 0.95
y = 2.0
while y < 25:
  h = x*y
  z = y*y - h*h
  z = math.sqrt(z)
  z = z*2
  print ('Kogato bedroto ni e', y, ' osnovata ni e',z)
  y += 0.1

x = 0.829
z = 1.0
while z < 25:
  y = z * x
  print ('Kogato osnovata ni e', z, ' bedroto ni e',y)
  z += 0.1
