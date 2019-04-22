from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='submit-home'),
    path('about/', views.about, name='submit-about'),
    path('submissions/', views.submissions, name='submit-about'),
    path('submit/', views.submit, name='submit-submit'),
]
