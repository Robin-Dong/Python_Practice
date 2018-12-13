import time

from celery import Celery



broker = 'redis://127.0.0.1:6379/0'
backend = 'redis://127.0.0.1:6379/1'
app = Celery('my_task',broker=broker, backend=backend)


@app.task
def add(x,y):
    print('callback...')
    time.sleep(4)
    return x + y

