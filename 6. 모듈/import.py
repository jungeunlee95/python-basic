# import math
# print(math.sin(math.pi/6), math.cos(math.pi/3), math.tan(math.pi/4))
#
# from math import pi, sin, cos, tan
# print(sin(pi/6), cos(pi/3), tan(pi/4))
#
# from math import pi, sin, cos, tan
# from mymath import pi
# print(sin(pi/6), cos(pi/3), tan(pi/4))

from math import sin as mysin, cos as mycos, tan as mytan
import mymath as m
print(mysin(m.pi / 6), mycos(m.pi / 3), mytan(m.pi / 4))


