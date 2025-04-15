import sys
import math
from functools import reduce

numbers = (int(line.strip()) for line in sys.stdin)
gcd_result = reduce(math.gcd, numbers)
print(gcd_result)