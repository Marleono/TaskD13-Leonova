from django.forms import ModelForm
from .models import Announcement, AnnounCategory, Category, User, Response
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group

class AnnouncementForm(ModelForm):
    # в класс мета как обычно надо написать модель по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Announcement
        fields = ['title', 'text', 'category', 'media']

class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ['response_text']



class CommonSignupForm(SignupForm):

    def save(self, request):
        user = super(CommonSignupForm, self).save(request)
        return user

