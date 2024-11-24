from celery import shared_task
from django.core.mail import send_mail
from smtplib import SMTPException

@shared_task(bind=True, max_retries=3)
def send_email_task(self, recipient, subject, body):
    try:
        send_mail(
            subject=subject,
            message=body,
            from_email='mursalbekov.merey@gmail.com',
            recipient_list=[recipient],
        )
        return f"Email успешно отправлен на {recipient}"
    except SMTPException as exc:
        raise self.retry(exc=exc, countdown=10)
    except Exception as exc:
        raise self.retry(exc=exc, countdown=10)

from celery import shared_task
import pandas as pd

@shared_task
def process_file(file_path):
    data = pd.read_csv(file_path)
    # Обработка данных
    return {"status": "Обработка завершена"}