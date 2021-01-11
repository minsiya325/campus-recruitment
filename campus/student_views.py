from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
import datetime

from campus.models import Course,Stud_Reg, Academic, Placement, Job, Jobapply, ChatStudent, PlacedStudent


class Chat(View):

    def post(self,request,*args,**kwargs):
        message = request.POST['message']

        stud = Stud_Reg.objects.get(user=self.request.user.id)
        name = stud.user.first_name
        chat = ChatStudent()
        chat.sender = name
        chat.message = message
        chat.time = datetime.datetime.today()
        chat.student = stud
        chat.status = 'Sent'
        chat.save()
        return  redirect('/student')

class IndexView(LoginRequiredMixin,TemplateView):
    template_name = 'student/stud_index.html'
    login_url = '/'
    def get_context_data(self, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        s = Stud_Reg.objects.get(user_id=self.request.user.id)
        up = 'OK'
        pl = 'Yes'
        ap = PlacedStudent.objects.filter(student__user_id=self.request.user.id).count()
        if ap>0:

            context['pl'] =  pl

        a = Academic.objects.filter(student__user_id=self.request.user.id).count()
        if a>0:

            context['up'] =  up

        chat = ChatStudent.objects.filter(student=s).order_by('time')
        context['chat'] = chat
        context['s'] = s
        return context


class AddAcademic(TemplateView):
    template_name = 'student/add_academic.html'

    def get_context_data(self, **kwargs):
        context = super(AddAcademic,self).get_context_data(**kwargs)
        co = Course.objects.all()
        up = 'OK'
        a = Academic.objects.filter(student__user_id=self.request.user.id).count()
        if a>0:

            context['up'] =  up
        context['co'] =  co
        s = Stud_Reg.objects.get(user_id=self.request.user.id)
        chat = ChatStudent.objects.filter(student=s).order_by('time')
        context['chat'] = chat
        context['s'] = s
        return context

    def post(self,request,*args,**kwargs):


        ten = request.POST['ten']

        two = request.POST['two']
        course = request.POST['course']
        csem = request.POST['csem']
        batch = request.POST['batch']

        cv = request.FILES['cv']
        try:
            percent = request.POST['percent']
            c = Course.objects.get(pk=course)
            s = Stud_Reg.objects.get(user_id=self.request.user.id)

            a = Academic.objects.filter(student__user_id=self.request.user.id).count()
            if a<=0:

                a =  Academic()
                a.ten_p = ten
                a.twe_p = two
                a.sem = csem
                a.course = c
                a.student = s
                a.cv = cv
                a.batch = batch
                a.ug = percent
                a.save()
                return  render(request,'student/stud_index.html',{'message':"Details Added"})
            else:
                return  render(request,'student/stud_index.html',{'message':"You Already  Added"})
        except:

            c = Course.objects.get(pk=course)
            s = Stud_Reg.objects.get(user_id=self.request.user.id)

            a = Academic.objects.filter(student__user_id=self.request.user.id).count()
            if a<=0:

                a =  Academic()
                a.ten_p = ten
                a.twe_p = two
                a.sem = csem
                a.course = c
                a.student = s
                a.cv = cv
                a.batch = batch
                a.ug = 'Null'
                a.save()
                return  render(request,'student/stud_index.html',{'message':"Details Added"})
            else:
                return  render(request,'student/stud_index.html',{'message':"You Already  Added"})


class UpdateProfile(TemplateView):
    template_name = 'student/update_profile.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateProfile,self).get_context_data(**kwargs)
        co = Stud_Reg.objects.get(user_id=self.request.user.id)
        up = 'OK'
        a = Academic.objects.filter(student__user_id=self.request.user.id).count()
        if a>0:

            context['up'] =  up

        sid= co.id
        ac = Academic.objects.get(student=sid)


        context['co'] =  co
        context['ac'] =  ac
        s = Stud_Reg.objects.get(user_id=self.request.user.id)
        chat = ChatStudent.objects.filter(student=s).order_by('time')
        context['chat'] = chat
        context['s'] = s
        return context

    def post(self,request,*args,**kwargs):


        address = request.POST['address']
        pimage = request.POST['pimage']

        contact = request.POST['contact']

        sem = request.POST['sem']



        try:
            profile = request.FILES['profile']
            s = Stud_Reg.objects.get(user_id=self.request.user.id)
            s.image = profile
            s.saddress = address
            s.scontact = contact
            s.save()
            ac = Academic.objects.get(student__user_id=self.request.user.id)
            ac.sem = sem
            ac.save()


        except:
            s = Stud_Reg.objects.get(user_id=self.request.user.id)
            s.image = pimage
            s.saddress = address
            s.scontact = contact
            s.save()
            ac = Academic.objects.get(student__user_id=self.request.user.id)
            ac.sem = sem
            ac.save()
        return  render(request,'student/stud_index.html',{'message':"Details Updated"})
        # if password == "":
        #     user = User.objects.get(pk=self.request.user.id)
        #     user.username = username
        #     user.save()
        #     return  render(request,'student/stud_index.html',{'message':"Profile Updated"})
        #
        #
        # else:
        #     user = User.objects.get(pk=self.request.user.id)
        #     user.username = username
        #     user.password = password
        #     user.save()
        #     return  render(request,'student/stud_index.html',{'message':"Profile"})


class ViewPlacements(TemplateView):
    template_name = 'student/view_placements.html'
    def get_context_data(self, **kwargs):
        context = super(ViewPlacements,self).get_context_data(**kwargs)
        com = Placement.objects.all()
        s = Stud_Reg.objects.get(user_id=self.request.user.id)
        chat = ChatStudent.objects.filter(student=s).order_by('time')

        up = 'OK'
        a = Academic.objects.filter(student__user_id=self.request.user.id).count()
        if a>0:

            context['up'] =  up
        context['com'] =  com
        context['chat'] = chat
        context['s'] = s

        return context

class DriveDetails(TemplateView):
    template_name = 'student/drive_details.html'

    def get_context_data(self, **kwargs):
        id = self.request.GET['id']
        context = super(DriveDetails,self).get_context_data(**kwargs)

        pl = Placement.objects.get(pk=id)
        ps = pl.id

        up = 'OK'
        a = Academic.objects.filter(student__user_id=self.request.user.id).count()
        if a>0:

            context['up'] =  up
        ac = Academic.objects.get(student__user_id=self.request.user.id)

        se = ac.sem
        cou = ac.course.id

        print(se)
        print(cou)


        com = Job.objects.filter(drive=id,p_course=cou,p_sem=se)
        s = Stud_Reg.objects.get(user_id=self.request.user.id)
        chat = ChatStudent.objects.filter(student=s).order_by('time')
        context['com'] =  com
        context['pls'] = pl
        context['pl'] = ps
        context['chat'] = chat
        context['s'] = s
        return context

class JobDetails(TemplateView):
    template_name = 'student/job_details.html'

    def get_context_data(self, **kwargs):
        id = self.request.GET['id']
        pl = self.request.GET['pl']
        context = super(JobDetails,self).get_context_data(**kwargs)
        up = 'OK'
        a = Academic.objects.filter(student__user_id=self.request.user.id).count()
        if a>0:

            context['up'] =  up

        com = Job.objects.get(pk=id)
        context['com'] =  com
        s = Stud_Reg.objects.get(user_id=self.request.user.id)
        chat = ChatStudent.objects.filter(student=s).order_by('time')
        context['chat'] = chat
        context['s'] = s
        context['pl'] = pl
        context['id'] = id
        return context

class ApplyJob(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        pl = request.GET['pl']
        try:
            today = datetime.date.today()

            ac = Academic.objects.get(student__user_id=self.request.user.id)

            ssem = ac.sem
            scourese = ac.course.name

            jobcount = Job.objects.filter(pk=id,p_sem=ssem,p_course__name=scourese).count()
            print("hi")
            if jobcount<=0:
                # return redirect('/student/DriveDetails?id='+pl)
                return render(request,'student/stud_index.html',{'message':"You Not Eligible To Apply This Job!.."})
            else:

                job = Job.objects.get(pk=id)
                jobid = job.id
                ldate = job.last_date

                a = Stud_Reg.objects.get(user_id=self.request.user.id)

                j = Jobapply.objects.filter(student__user_id=self.request.user.id,job__id=jobid).count()

                if j>0:
                    return render(request,'student/stud_index.html',{'message':"You Already Apply This Job!.."})
                else:
                    date_time_obj = datetime.datetime.strptime(ldate, '%Y-%m-%d')
                    if today <= date_time_obj.date():
                        ja = Jobapply()
                        ja.job = job
                        ja.student = a
                        ja.a_status = 'Apply'
                        ja.save()
                        return render(request,'student/stud_index.html',{'message':"Apply Success."})
                    else:
                        return render(request,'student/stud_index.html',{'message':"Your Are Late Apply Over."})
        except:
            return render(request,'student/stud_index.html',{'message':"Please Upload Your Academic Details!."})




class MyApply(TemplateView):
    template_name = 'student/my_apply.html'

    def get_context_data(self, **kwargs):
        context = super(MyApply,self).get_context_data(**kwargs)
        s = Stud_Reg.objects.get(user_id=self.request.user.id)
        chat = ChatStudent.objects.filter(student=s).order_by('time')
        ap = Jobapply.objects.filter(student__user_id=self.request.user.id)

        up = 'OK'
        a = Academic.objects.filter(student__user_id=self.request.user.id).count()
        if a>0:

            context['up'] =  up
        context['ap'] =  ap

        context['chat'] = chat
        context['s'] = s
        return context

class PlacedStudents(TemplateView):
    template_name = 'student/placedstudents.html'

    def get_context_data(self, **kwargs):

        context = super(PlacedStudents,self).get_context_data(**kwargs)
        ap = PlacedStudent.objects.filter(student__user_id=self.request.user.id)
        up = 'OK'
        a = Academic.objects.filter(student__user_id=self.request.user.id).count()
        if a>0:

            context['up'] =  up


        context['ap'] =  ap
        return context