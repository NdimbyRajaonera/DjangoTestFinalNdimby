from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from .models import Avis,User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import logout

from portfolio.models import User

@login_required(login_url='portfolio:login')
def portfolio(request):
    return render(request, 'portfolio.html')

@login_required(login_url='portfolio:login')
def donner_avis(request):
    return render(request, 'avis.html')

@login_required(login_url='portfolio:login')
def contact(request):
    if request.method == 'POST':
        return redirect('portfolio:portfolio')
    return render(request, 'contact.html')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('portfolio:portfolio')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        try:
            user = User.objects.get(username=username, password=password)
            messages.info(self.request, 'Vous êtes déjà inscrit. Veuillez vous connecter pour consulter le portfolio de Ndimby Rajaonera.')
        except User.DoesNotExist:
            user = User(username=username, password=password)
            user.save_to_database()
            messages.success(self.request, 'Vous avez été enregistré avec succès. Veuillez vous connecter pour consulter le portfolio de Ndimby Rajaonera.')

        return super().form_valid(form)
    
@login_required(login_url='portfolio:login')
def donner_avis(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        poste = request.POST.get('poste')
        message = request.POST.get('message')

        avis = Avis(nom=nom, email=email, poste=poste, message=message)
        avis.save()

        #subject = 'Nouvel avis reçu'
        #content = f"Nom: {nom}\nEmail: {email}\nPoste: {poste}\nMessage: {message}"
        #from_email = settings.DEFAULT_FROM_EMAIL
        #recipient_list = ['ndimbyrajaonera@gmail.com']

        #send_mail(subject, content, from_email, recipient_list, fail_silently=False)

        return redirect('portfolio:portfolio')

    return render(request, 'avis.html')

def logout_view(request):
    logout(request)
    request.session.clear()
    return redirect('portfolio:login')
