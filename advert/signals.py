from django.db.models.signals import post_save
from django.dispatch import receiver # импортируем нужный декоратор
from django.core.mail import send_mail
from .models import Announcement, User
from datetime import datetime, timedelta
from django.utils import timezone

@receiver(post_save, sender=Announcement)
def notification_mail(sender, created, **kwargs):
    people = User.objects.all()
    people_email = User.objects.get(email='email')
    new_announcements = Announcement.objects.filter(created__range=[timezone.now() - timedelta(weeks=1), timezone.now()])
    for person in people:
            if created:
                 subject = f'{person.username}'
            else:
                 subject = f'Список объявлений изменен для {person.username} '

            send_mail(
                subject=subject,
                message= f'Новое объявление!',
                from_email= None,
                fail_silently = False,
                recipient_list = ['people_email'],
            )