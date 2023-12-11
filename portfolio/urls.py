from django.urls import path
from .views import CustomLoginView, portfolio, donner_avis, contact
from portfolio.views import donner_avis
from portfolio import views

app_name = 'portfolio'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('portfolio/', portfolio, name='portfolio'),
    path('portfolio/avis/', donner_avis, name='avis'),
    path('donner-avis/', donner_avis, name='donner_avis'),
    path('logout/', views.logout_view, name='logout'),
]