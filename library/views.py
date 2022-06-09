from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from . import forms,models
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib import auth
from library.models import Book, CustomUser
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.core.mail import send_mail
from librarymanagement.settings import EMAIL_HOST_USER
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

def home_view(request):
    return render(request,'library/index.html')



def adminlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user) 
            return redirect('viewbook')
        else:
            messages.error(request, 'invalid credentials')
    
    return render(request,'library/adminlogin.html')


def adminsignup_view(request):
    return render(request,'library/adminsignup.html')

def registerview(request):
    
    
    if request.method == "POST":
        
         
        email = request.POST.get('email')
        Password = request.POST.get('password')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        
        user = CustomUser()
        user.email = email
        user.first_name = firstname
        user.last_name = lastname
        user.set_password(Password)
        user.save()
        
       
            
        login(request,user)
    
    return redirect('viewbook')










def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()

def afterlogin_view(request):
    if is_admin(request.user):
        return render(request,'library/adminafterlogin.html')
    else:
        return render(request,'library/studentafterlogin.html')



def addbook_view(request):
    #now it is empty book form for sending to html
    form=forms.BookForm()
    if request.method=='POST':
        #now this form have data from html
        form=forms.BookForm(request.POST)
        if form.is_valid():
            user=form.save()
            return render(request,'library/bookadded.html')
    return render(request,'library/addbook.html',{'form':form})


def viewbook_view(request):
    books=models.Book.objects.all()
    return render(request,'library/viewbook.html',{'books':books})

def editbook(request,id):
    book = Book.objects.get(id =id)
    context = {
        'book':book,
    }
    
    return render(request,'library/updatebook.html',context)
def editbk(request,id):
    
    if request.method == "POST":
        bookname = request.POST.get('bookname')
        authorname = request.POST.get('authorname')
        
        course = Book.objects.get(id = id)
        course.name = bookname
        course.author = authorname
        course.save()
    return redirect('viewbook')
def deletebook(request,id):
    
    bk = Book.objects.get(id = id)
    bk.delete()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    