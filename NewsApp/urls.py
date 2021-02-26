from django.urls import path
from .views import NewsP,Home,Contact,Newsdate,register,addUser,modelform,addModalForm
urlpatterns = [
    path('', Home, name='home'),
    path('news/', NewsP, name='news'),
    path('contact/', Contact, name='contact'),
    path('newsdate/<int:year>', Newsdate, name='newsdate'),
    path('signup/', register, name='register'),
    path('addUser/', addUser, name='addUser'),
    path('modalform/', modelform, name='form'),
    path('addModalform/', addModalForm, name='modalform'),

]

