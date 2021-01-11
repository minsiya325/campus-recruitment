from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth.models import User
from django.views.generic import TemplateView
import datetime

from campus.models import Reg, Stud_Reg, UserType, PlacedStudent


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):

        context = super(IndexView,self).get_context_data(**kwargs)
        ap = PlacedStudent.objects.filter(place_status='Placed')
        context['ap'] =  ap
        return context

class StudRegister(TemplateView):
    template_name = 'stud_reg.html'


    def post(self, request,*args,**kwargs):
        fullname = request.POST['name']
        contact = request.POST['phone']
        email = request.POST['email']
        address = request.POST['addr']
        ad = request.POST['ad']
        file = request.FILES['image']



        username = request.POST['user']
        dob = request.POST['dob']
        gen = request.POST['gen']

        password = request.POST['pass']
        try:
            user = User.objects._create_user(username=username,password=password,first_name=fullname,email=email,last_name = 0)
            user.save()
            user_info = Stud_Reg()
            user_info.user=user
            user_info.scontact = contact
            user_info.saddress = address
            user_info.adno = ad
            user_info.image = file
            user_info.dob = dob
            user_info.gender = gen


            user_info.save()

            user_info.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = 'Student'
            usertype.save()


            messages = "Registration Successfull"
            return render(request,'index.html',{'message':messages})
        except:
            messages = "Enter Another Username"
            return render(request,'index.html',{'message':messages})


class Register(TemplateView):
    template_name = 'reg.html'

    def post(self, request,*args,**kwargs):
        fullname = request.POST['name']
        contact = request.POST['phone']
        email = request.POST['email']
        address = request.POST['addr']
        web = request.POST['web']


        username = request.POST['user']

        password = request.POST['pass']
        try:
            user = User.objects._create_user(username=username,password=password,first_name=fullname,email=email,last_name = 0)
            user.save()
            user_info = Reg()
            user_info.user=user
            user_info.contact = contact
            user_info.address = address
            user_info.website = web
            user_info.type = 'Company'
            user_info.joindate = datetime.datetime.today()


            user_info.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = 'Company'
            usertype.save()

            messages = "Registration Successfull"
            return render(request,'index.html',{'message':messages})
        except:
            messages = "Enter Another Username"
            return render(request,'index.html',{'message':messages})



class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password= request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('admin/')
                elif UserType.objects.get(user_id=user.id).type == "Student":
                    return redirect('/student')
                else:
                    return redirect('/company')
            else:
                return render(request,'login.html',{'message':" User Account Not Authenticated"})
        else:
            return render(request,'login.html',{'message':"Invalid Username or Password"})
