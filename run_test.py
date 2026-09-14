import sys
sys.path.append("src")

from rectangle import Rectangle
from square import Square

r = Rectangle(3, 5)
s = Square(5)

print(r.add_area(s))
print(s.add_area(r))