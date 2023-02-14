from django.shortcuts import render,redirect              
from django.http import HttpResponse
from .models import Registrationform
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
import string
from django.contrib.auth.models import User


# Create your views here.

def login(request):
    return render(request,'login/login.html')

def signup(request):  
        return render(request,'registration/register.html')
def register(request):
        context={}
        Firstname=request.POST['firstname']
        Lastname = request.POST['lastname']
        Email = request.POST['email']
        Gender = request.POST['gender']
        Course = request.POST['course']
        Batch= request.POST['batch']
        Password= request.POST['forgetpwd']


        obj = Registrationform.objects.create(firstname=Firstname,lastname=Lastname,email=Email,gender=Gender,course=Course,batch=Batch,password=Password)
        obj.save()
        subject = 'welcome to the  world'
        message = f'Hi thank you for registering.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['tvsaiteja1661@gmail.com']
        send_mail( subject, message, email_from, recipient_list )
        #messages.success(request,'account is registered',Firstname)
        #send_mail('admin','hello world','kalyanikuppa1107@gmail.com',['tvsaiteja1661@gmail.com'])
        
        return redirect('login')

#needs to use
def loginuser(request):
        username=request.POST['username']
        password=request.POST['pwd']
        
        obj=Registrationform.objects.filter(password=password, email=username)
        if len(obj)!= False:
            print(obj)
            return render(request,'login/homepage.html')
       

        else:
            return render(request,'login/login.html')
             

                
            
    
def adminform(request):
        context={}
        data=Registrationform.objects.all()
        context['words']=data
         #if  username.is_superuser:
        #        messages.info(request, f"You are now logged in as {username}.")
         #       return redirect('registration/adminpage.html')
        #else:
         #       messages.info(request, f"You are now logged in as {username}.")
        #      return render(request,'student/home.html')
     
        return render(request,'registration/adminpage.html',context)




"""def forgetpassword(request):
        if request.method == "POST":
                uname = request.POST['username']
                obj =Registrationform.objects.get(email=uname)
                if obj.is_valid():
                        subject = 'forget passwordmail'
                        message = f'Hi thank you .'
                        email_from = settings.EMAIL_HOST_USER
                        recipient_list = ['kalyanikuppa1107@gmail.com']
                        send_mail( subject, message, email_from, recipient_list )
                else:
                        print('no user found ')         

                
        
        return render(request,'login/forgetpwd.html')"""



        



"""if username is not None:
            #login(request,user)
           if username.is_superuser:
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('registration/adminpage.html')

                
            else:
                messages.info(request, f"You are now logged in as {username}.")
                return render(request,'student/home.html')
        else:
            messages.info(request,'Enter Valid Username and Password')"""
             
def userrequest(request):
    context={}
    
    if Registrationform.objects.filter(status='pending'):
        Userrequest = Registrationform.objects.all()
        
        context['users']= Userrequest
        context['header']=['First_name','Gender','Email']
        if request.method == 'POST':
            context_msg ={}
            print(request.POST)
            if 'approvebtn' in request.POST:
                print(request.POST)
                Registrationform.objects.filter(id=request.POST['chk']).update(status = 'Approved')
                
                subject = 'welcome to the world'
                message = f'Hi thank you for registering.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = ['tvsaiteja1661@gmail.com']
                send_mail( subject, message, email_from, recipient_list )
                #messages.success(request,'account is registered',Firstname)
                #send_mail('admin','hello world','kalyanikuppa1107@gmail.com',['tvsaiteja1661@gmail.com'])
               

                return HttpResponse('success')

            elif 'rejectbtn' in request.POST:
               Registrationform.objects.filter(id=request.POST['chk']).update(status = 'Rejected')
               return HttpResponse("You are rejected")
    return render(request,'registration/adminpage.html',context)
    


