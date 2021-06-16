from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, UpdateView
from .models import Announcement, Category, Response
from .forms import AnnouncementForm, ResponseForm
from django.utils.decorators import method_decorator
from .filters import AnnouncementFilter
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
# Create your views here.


class AnnouncementsList(ListView):
    model = Announcement  # указываем модель, объекты которой мы будем выводить
    template_name = 'announcements.html'  # указываем имя шаблона, в котором будет лежать html, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'announcements'
    ordering = ['-created']
    paginate_by = 10
    form_class = AnnouncementForm

    def get_context_data(self,
                         **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = AnnouncementFilter(self.request.GET,
                                          queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        context['form'] = AnnouncementForm()
        return context

    def post(request):
        # берём значения для нового товара из POST-запроса отправленного на сервер
        if request.method == 'POST':
            form = AnnouncementForm(request.POST, request.FILES)

        if form.is_valid():
            advert_post = True
            advert = form.save(commit=False)
            advert.owner = request.user
            advert.save()

            return redirect('announcements')
        else:
            form = AnnouncementForm()

        return redirect('/')

class ResponseList(ListView):
    model = Response  # указываем модель, объекты которой мы будем выводить
    template_name = 'profile.html'  # указываем имя шаблона, в котором будет лежать html, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'responses'
    ordering = ['-response_datetime']
    paginate_by = 10

class AnnouncementDetail(DetailView):
    template_name = 'announcement.html' # название шаблона будет product.html
    queryset = Announcement.objects.all()


@method_decorator(login_required, name='dispatch')
class AnnouncementCreate(CreateView):
    template_name = 'announcement_create.html'
    form_class = AnnouncementForm
    success_url = '/announcements/'
    
    def media_create(request):
    if request.method == "POST":
        form = Announcement(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('media-list'))
    else:
        form = Announcement()
    return render('media/create/html', {'form': form})




@method_decorator(login_required, name='dispatch')
class AnnouncementDelete(DeleteView):
    template_name = 'announcement_delete.html'
    queryset = Announcement.objects.all()
    success_url = '/announcements/'


@method_decorator(login_required, name='dispatch')
class ResponseCreate(CreateView):
    template_name = 'response_create.html'
    queryset = Announcement.objects.all()
    success_url = '/announcements/'
    form_class = ResponseForm


@method_decorator(login_required, name='dispatch')
class AddAnnouncement(PermissionRequiredMixin, CreateView):
    permission_required = ('advert.announcement_add', 'advert.announcement_delete')


class CategoryView(ListView):
    model = Category
    template_name = 'announcements.html'
    context_object_name = 'category'
    queryset = Category.objects.all()


