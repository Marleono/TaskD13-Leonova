from django.urls import path
from .views import AnnouncementsList, AnnouncementDetail, AnnouncementCreate, AnnouncementDelete, ResponseCreate, ResponseList, AnnouncementUpdate


urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно почему
    path('', AnnouncementsList.as_view()), # т.к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', AnnouncementDetail.as_view(), name='announcement'),
    path('create/', AnnouncementCreate.as_view(), name='announcement_create'),
    path('update/', AnnouncementUpdate.as_view(), name='announcement_create'),
    path('<int:pk>/delete/', AnnouncementDelete.as_view(), name='announcement_delete'),
    path('<int:pk>/response/', ResponseCreate.as_view(), name='response_create'),
    path('profile/', ResponseList.as_view(), name='profile'),
]

