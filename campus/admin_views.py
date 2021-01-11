
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
import datetime




from campus.filter import AcademicFilter, PlaceFilter, CompnayFilter

from campus.models import Reg, Placement, Stud_Reg, Course, ChatStudent, PlacedStudent, Academic


class IndexView(LoginRequiredMixin,TemplateView):
    template_name = 'admin/admin_index.html'
    login_url = '/'
    def get_context_data(self, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        Sent = ChatStudent.objects.filter(status='Sent').count()

        context['Sent'] = Sent

        return context



class Chat(LoginRequiredMixin,TemplateView):
    template_name = 'admin/chat.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(Chat,self).get_context_data(**kwargs)
        student = Stud_Reg.objects.filter(user__last_name='1',user__is_staff='0')

        # for std in student:
        #     # c = ChatStudent.objects.filter(student=std.id,status='Sent').count()
        #     print(c)
        #
        #     # context['c'] = c
        context['student'] = student

        try:
            id = self.request.GET['id']
            chat = ChatStudent.objects.filter(student=id).order_by('time')
            context['chat'] = chat
            context['id'] = id
        except:
            return context
        return context

    def post(self,request,*args,**kwargs):
        message = request.POST['message']


        try:
            stud = request.POST['stud']
        except:
            return  redirect('/admin/Chat')

        student = Stud_Reg.objects.get(pk=stud)
        ch = ChatStudent.objects.filter(student=student.id)

        for d in ch:
            d.status = 'Recived'
            d.save()

        chat = ChatStudent()
        chat.sender = 'Admin'
        chat.message = message
        chat.time = datetime.datetime.today()
        chat.student = student
        chat.status = 'Replay'
        chat.save()
        return  redirect('/admin/Chat?id='+stud)






class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='0'
        user.is_active='0'
        user.save()
        return render(request,'admin/admin_index.html',{'message':"Account Removed"})

class NewCompany(LoginRequiredMixin,TemplateView):
    template_name = 'admin/new_company.html'
    login_url = '/'
    def get_context_data(self, **kwargs):
        context = super(NewCompany,self).get_context_data(**kwargs)
        com = Reg.objects.filter(user__last_name='0',user__is_staff='0',type='Company')
        context['com'] =  com
        return context

class NewStudents(TemplateView):
    template_name = 'admin/new_students.html'
    def get_context_data(self, **kwargs):
        context = super(NewStudents,self).get_context_data(**kwargs)
        stu = Stud_Reg.objects.filter(user__last_name='0',user__is_staff='0')
        context['stu'] =  stu
        return context


class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'

        user.save()
        return render(request,'admin/admin_index.html',{'message':"Account Activated"})

class ViewCompany(TemplateView):
    template_name = 'admin/view_company.html'
    def get_context_data(self, **kwargs):
        context = super(ViewCompany,self).get_context_data(**kwargs)
        com = Reg.objects.filter(user__last_name='1',user__is_staff='0',type='Company')
        myFilter = CompnayFilter(self.request.GET, queryset=com)
        com = myFilter.qs
        context['myFilter'] =  myFilter
        context['com'] =  com
        return context

class ViewStudents(TemplateView):
    template_name = 'admin/view_students.html'
    def get_context_data(self, **kwargs):
        context = super(ViewStudents,self).get_context_data(**kwargs)
        stu = Academic.objects.filter(student__user__last_name='1',student__user__is_staff='0')


        stud = stu.all()
        myFilter = AcademicFilter(self.request.GET, queryset=stu)
        stu = myFilter.qs

        # context = {'stu':stu, 'myFilter': myFilter }
        context['stu'] =  stu
        context['myFilter'] =  myFilter
        return context



class AddPlacement(TemplateView):
    template_name = 'admin/add_placements.html'

    def post(self,request,*args,**kwargs):
        event_name = request.POST['name']


        phone = request.POST['phone']
        addr = request.POST['addr']
        date = request.POST['pdate']
        ptime = request.POST['ptime']
        image = request.FILES['broche']
        pl  = Placement()
        pl.p_name = event_name
        pl.p_address = addr
        pl.p_contact = phone

        pl.p_date = date
        pl.p_time = ptime
        pl.brochure = image
        pl.save()
        return  render(request,'admin/admin_index.html',{'message':"Placement Drive Added"})

class AddCourse(TemplateView):
    template_name = 'admin/add_course.html'

    def post(self,request,*args,**kwargs):
        event_name = request.POST['name']

        gradu = request.POST['gradu']

        pl  = Course()
        pl.co_name = event_name
        pl.graduate = gradu
        pl.save()
        return  render(request,'admin/admin_index.html',{'message':"Course Added"})


class ViewPlacements(TemplateView):
    template_name = 'admin/view_placements.html'
    def get_context_data(self, **kwargs):
        context = super(ViewPlacements,self).get_context_data(**kwargs)
        com = Placement.objects.all()
        context['com'] =  com
        return context

class RejectPlacement(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = Placement.objects.get(pk=id)

        user.delete()
        return render(request,'admin/admin_index.html',{'message':"Drive Removed"})

class PlacedStudents(TemplateView):
    template_name = 'admin/placedstudents.html'

    def get_context_data(self, **kwargs):

        context = super(PlacedStudents,self).get_context_data(**kwargs)
        ap = PlacedStudent.objects.all()
        up = 'OK'
        stud = ap.all()
        myFilter = PlaceFilter(self.request.GET, queryset=ap)
        ap = myFilter.qs

        # context = {'stu':stu, 'myFilter': myFilter }

        context['myFilter'] =  myFilter


        context['ap'] =  ap
        return context

class CommonMessage(View):
    def post(self,request,*args,**kwargs):
        message = request.POST['message']

        c = Stud_Reg.objects.filter(user__last_name='1',user__is_staff='0')
        for s in c:


            chat = ChatStudent()
            chat.sender = 'Admin'
            chat.message = message
            chat.time = datetime.datetime.today()
            chat.student = s
            chat.status = 'Replay'
            chat.save()




        return  render(request,'admin/chat.html',{'message':"Course Added"})
