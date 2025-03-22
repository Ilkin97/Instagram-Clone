from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Django'nun settings modülünü yükleyin
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Celery uygulamasını oluşturun
app = Celery('stories')

# Django ayarlarını yükle
app.config_from_object('django.conf:settings', namespace='CELERY')

# Tüm uygulama modüllerinden task'ları yükleyin
app.autodiscover_tasks()

# app.conf.update(
#     task_default_queue='default',
#     task_default_retry_delay=60,
#     task_routes={
#         'myapp.tasks.some_task': {'queue': 'my_queue'},
#     },
#     task_track_started=True,
#     task_send_sent_event=True,
# )