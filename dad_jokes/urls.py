from django.urls import path, include
from dad_jokes import views

app_name = 'dad_jokes'
urlpatterns = [
    path('store-dad-joke-from-api/', views.store_dad_joke_from_api , name='store_dad_joke_from_api'),
    path('locally-stored-dad-joke/<int:joke_id>/', views.locally_stored_dad_joke, name='locally_stored_dad_joke'),
    path('store-new-dad-joke/', views.store_new_dad_joke, name='store_new_dad_joke'),
]
