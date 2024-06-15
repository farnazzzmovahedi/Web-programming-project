from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Banner
from django.contrib.sessions.models import Session


# Create your views here.

# def home_page(request):
#     return render(request, 'electro_shop/home-page.html')


# class HomePageView(CreateView):
#     model = User
#     form_class = UserSignup
#     template_name = 'electro_shop/home-page.html'
#     success_url = reverse_lazy('login')

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

# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['mainBanner'] = Banner.objects.get(banner_type='mainBanner')
#     context['adBanner'] = Banner.objects.get(banner_type='adBanner')
#     return context


class HomePageView(TemplateView):
    template_name = 'home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mainBanner'] = Banner.objects.get(banner_type='mainBanner')
        context['adBanner'] = Banner.objects.get(banner_type='adBanner')
        context['signup_form'] = CustomUserCreationForm()
        context['login_form'] = AuthenticationForm()
        context['user_logged_in'] = None
        return context

    def post(self, request, *args, **kwargs):
        print(request.POST)
        type1 = request.POST.get('type')
        print(type1)
        if type1 == 'signup':
            print(type1)
            # if request == request.POST:
            #     print("signup")
            signup_form = CustomUserCreationForm(request.POST)
            if signup_form.is_valid():
                print("valid")
                signup = signup_form
                signup_form.save()
                # print(signup_form)
                # After successful signup, redirect to success URL
                return render(request, self.template_name, {
                    'signup_form': signup,
                    'mainBanner': Banner.objects.get(banner_type='mainBanner'),
                    'adBanner': Banner.objects.get(banner_type='adBanner')
                })
            else:
                # If form is not valid, re-render the template with the form errors
                return render(request, self.template_name, {
                    'signup_form': signup_form,
                    'login_form': AuthenticationForm(),
                    'mainBanner': Banner.objects.get(banner_type='mainBanner'),
                    'adBanner': Banner.objects.get(banner_type='adBanner')
                })
        elif type1 == 'login':
            # login_form = AuthenticationForm(data=request.POST)
            # if login_form.is_valid():
            #     user = login_form.get_user()
            #     login(request, user)
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            request.session['username'] = username
            request.session.save()
            # After successful login, redirect to success URL

            return render(request, self.template_name, {
                'user_logged_in': user,
                'signup_form': CustomUserCreationForm(),
                'login_form': AuthenticationForm(),
                'mainBanner': Banner.objects.get(banner_type='mainBanner'),
                'adBanner': Banner.objects.get(banner_type='adBanner')
            })
        else:
            # If login form is not valid, re-render the template with the form errors
            return render(request, self.template_name, {
                'signup_form': CustomUserCreationForm(),
                'login_form': AuthenticationForm(),
                'mainBanner': Banner.objects.get(banner_type='mainBanner'),
                'adBanner': Banner.objects.get(banner_type='adBanner')
            })
        # Ensure a default response is returned if neither 'signup' nor 'login' is in request.POST
        # In this case, redirect to the success URL or render the template with initial context

    # def get_success_url(self):
    #     return reverse_lazy('home')


# def login_view(request):
#     login_form = AuthenticationForm(data=request.POST)
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         print(user)
#         if user[username] != "":
#             print("ada")
#             login(request, user)
#             request.session['username'] = username
#             request.session.save()
#             return render(request, 'home-page.htm')

class DetailPageView(LoginRequiredMixin, TemplateView):
    template_name = 'product-detail-page.html'
    login_url = 'login'
    redirect_field_name = 'next'
