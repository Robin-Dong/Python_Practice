#指定broker和backend
BROKER_URL = 'redis://localhost:6379/1'

CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'



#指定时区
CELERY_TIMEZONE='Asia/Shanghai'

#指定导入的任务模块
CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2',
)
