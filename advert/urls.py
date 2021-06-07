from django.urls import path
from .views import AnnouncementsList, AnnouncementDetail, AnnouncementCreate

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно почему
    path('', AnnouncementsList.as_view()), # т.к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', AnnouncementDetail.as_view(), name='announcement'),
    path('create/', AnnouncementCreate.as_view(), name='announcement_create'),
]

