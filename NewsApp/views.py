from django.shortcuts import render, redirect
from .models import News
from .forms import RegistrationForm,RegistrationModal
from .models import RegistrationData
from django.contrib import messages
# Create your views here.

def Home(request):
    context = {
        "name":"Jasur Abdusalomov",
        "number":7645
    }
    return render(request,'home.html',context)

def NewsP(request):
    obj = News.objects.get(id=1)
    context = {
        "data":obj
        # "list":["Python","Java","C++","C#","Kotlin","Ruby"],
        # "mynum":40
    }
    return render(request,'news.html',context)


def Contact(request):
    return render(request, 'contact.html')


def Newsdate(request,year):
    article_list = News.objects.filter(pub_date__year = year)
    context = {
        "year":year,
        'article_list':article_list
    }
    return render(request, 'newsdate.html',context)
# def News(request):
#     return HttpResponse("<h1>This is our latest news</h1>")




def register(request):
    context = {
        "form":RegistrationForm
    }
    return render(request,'signup.html',context)


def addUser(request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        myregister = RegistrationData(username = form.cleaned_data['username'],
                                      password=form.cleaned_data['password'],
                                      email=form.cleaned_data['email'],
                                      phone=form.cleaned_data['phone'])
        myregister.save()
        messages.add_message(request,messages.SUCCESS,"You have signup successfully")


    return redirect('register')


def modelform(request):
    context = {
        "modalform":RegistrationModal
    }

    return render(request,'modalform.html',context)


def addModalForm(request):
    mymodalform = RegistrationModal(request.POST)
    if mymodalform.is_valid():
        mymodalform.save()
        return redirect('form')


# def News(request):
#     context = {
#         "list":['Python','C++','C','Kotlin','Ruby'],
#         "mynum":50
#     }
#     return render(request, "news.html",context)