import sys
import os
sys.path.append(os.getcwd())
from my_tasks import add

add.delay(2,8)

print('i dont need wait')