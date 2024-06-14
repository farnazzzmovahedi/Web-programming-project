from django.shortcuts import render
from django.views.generic import CreateView

from electro_shop.models import Product
from django.shortcuts import render
from json import dumps
from django.views.generic import ListView, TemplateView, CreateView
from .models import User
from .models import Banner
from .forms import UserSignup
from django.urls import reverse_lazy


# Create your views here.

def home_page(request):
    return render(request, 'electro_shop/home-page.html')


class HomePageView(CreateView):
    model = User
    form_class = UserSignup
    template_name = 'electro_shop/home-page.html'
    success_url = reverse_lazy('login')

    # def form_valid(self, form):
    #     user_username = form.cleaned_data.get('username')
    #     user_email = form.cleaned_data.get('email')
    #     user_password = form.cleaned_data.get('password')
    #     is_exist_email = User.objects.filter(email__iexact=user_email).exists()
    #     if is_exist_email:
    #         form.add_error('email', 'Email already registered')
    #         return self.form_invalid(form)
    #     else:
    #         new_user = form.save(commit=False)
    #         new_user.username = user_username
    #         new_user.email = user_email
    #         new_user.set_password(user_password)
    #         new_user.save()
    #         response = super().form_valid(form)
    #         return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mainBanner'] = Banner.objects.get(banner_type='mainBanner')
        context['adBanner'] = Banner.objects.get(banner_type='adBanner')
        return context
