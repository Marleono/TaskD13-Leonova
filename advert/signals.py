from django.db.models.signals import post_save
from django.dispatch import receiver # импортируем нужный декоратор
from django.core.mail import send_mail
from .models import Announcement, User
from datetime import datetime, timedelta
from django.utils import timezone

@receiver(post_save, sender=Announcement)
def notification_mail(sender, created, **kwargs):
    people = User.objects.all()
    people_email = list(User.objects.values_list('email', flat=True))
    new_announcements = Announcement.objects.filter(created__range=[timezone.now() - timedelta(weeks=1), timezone.now()])
    for person in people:
        for announcement in new_announcements:
            if created:
                 subject = f'{person.username}'

            send_mail(
                subject=subject,
                message=f'Новый пост на доске!',
                from_email= '',
                recipient_list = people_email,
            )