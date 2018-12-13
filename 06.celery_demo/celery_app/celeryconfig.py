from datetime import timedelta
from celery.schedules import crontab


#指定broker和backend
BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'


#指定时区
CELERY_TIMEZONE='Asia/Shanghai'

#指定导入的任务模块
CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2',
)

#定时
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds':{
        'task': 'celery_app.task1.add',
        'schedule': timedelta(seconds=30),  # 每 30 秒执行一次
        'args':(5, 8)
    },
    'multiply-at-some-time':{
        'task': 'celery_app.task2.multiply',
        'schedule':crontab(hour=9, minute=50), # m每天9:50执行
        'args':(3,7)
    }
}