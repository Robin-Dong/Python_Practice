from celery_app import task1
from celery_app import task2

task1.add.apply_async(args=[2,6])
task2.multiply.apply_async(args=[3,7])

print('i dont need wait !')