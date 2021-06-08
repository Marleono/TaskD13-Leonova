from django_filters import FilterSet  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Announcement, User, Category, AnnounCategory
import django_filters

class AnnouncementFilter(FilterSet):
    # Здесь в мета классе надо предоставить модель и указать поля по которым будет фильтроваться (т.е. подбираться) информация о товарах
    class Meta:
        model = Announcement
        fields = {
            'title': ['icontains'],
            'category': ['exact'],
            'created': ['gt'],
        }
