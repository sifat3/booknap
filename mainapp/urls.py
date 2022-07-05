from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_books', views.all_books, name='books'),
    path('details/<str:id>', views.details, name='details'),
    path('borrowed', views.borrowed, name='borrowed'),
    path('lent', views.lent, name='lent'),
]