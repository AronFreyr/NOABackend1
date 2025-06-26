from django.urls import path, include
from dad_jokes import views

app_name = 'dad_jokes'
urlpatterns = [
    path('store-dad-joke-from-api/', views.store_dad_joke_from_api , name='store_dad_joke_from_api'),
]
