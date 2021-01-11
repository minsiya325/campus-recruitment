from django.views.generic import TemplateView, View
from campus.models import Placement, Reg, Job, Course, Jobapply, Academic, PlacedStudent, Stud_Reg
from django.shortcuts import render, redirect
import datetime
class IndexView(TemplateView):
    template_name = 'company/com_index.html'

class ViewPlacements(TemplateView):
    template_name = 'company/view_placements.html'
    def get_context_data(self, **kwargs):
        context = super(ViewPlacements,self).get_context_data(**kwargs)
        com = Placement.objects.all()
        context['com'] =  com
        return context

class PlacementDetails(TemplateView):
    template_name = 'company/placement_details.html'
    def get_context_data(self, **kwargs):
        id = self.request.GET['id']
        context = super(PlacementDetails,self).get_context_data(**kwargs)
        com = Placement.objects.get(pk=id)
        context['com'] =  com
        return context

class AddJob(TemplateView):
    template_name = 'company/add_job.html'
    def get_context_data(self, **kwargs):
        context = super(AddJob,self).get_context_data(**kwargs)
        id = self.request.GET['did']
        com = Placement.objects.get(pk=id)
        co = Course.objects.all()

        context['com'] =  com
        context['co'] =  co
        return context

    def post(self,request,*args,**kwargs):

        r = Reg.objects.get(user_id=self.request.user.id)
        name = request.POST['name']

        no = request.POST['no']
        dept = request.POST['dept']
        salary = request.POST['salary']
        course = request.POST['course']
        sem = request.POST['sem']
        percent = request.POST['percent']
        descri = request.POST['descri']
        drive = request.POST['drive']
        d = Placement.objects.get(pk=drive)
        c = Course.objects.get(pk=course)

        pdate =d.p_date



        date_time_obj = datetime.datetime.strptime(pdate, '%Y-%m-%d')
        s = date_time_obj.date() - datetime.timedelta(days=1)



        j = Job()
        j.drive = d
        j.company = r
        j.p_name = name
        j.no_vacan = no
        j.department = dept
        j.salary = salary
        j.p_course = c
        j.p_sem = sem
        j.last_date = s
        j.job_desc = descri
        j.p_per = percent
        j.save()
        return  render(request,'company/com_index.html',{'message':"Job Added"})

class ViewJob(TemplateView):
    template_name = 'company/view_jobs.html'

    def get_context_data(self, **kwargs):
        id = self.request.GET['id']
        context = super(ViewJob,self).get_context_data(**kwargs)
        pl = Placement.objects.get(pk=id)

        com = Job.objects.filter(drive=id,company__user_id=self.request.user.id)
        context['com'] =  com
        context['pl'] =  pl
        return context


class StudApplication(TemplateView):
    template_name = 'company/stud_application.html'

    def get_context_data(self, **kwargs):
        id = self.request.GET['id']
        context = super(StudApplication,self).get_context_data(**kwargs)
        ap = Jobapply.objects.filter(job=id)


        context['ap'] =  ap
        return context

class ViewAcademic(TemplateView):
    template_name = 'company/view_academic.html'

    def get_context_data(self, **kwargs):
        id = self.request.GET['did']
        context = super(ViewAcademic,self).get_context_data(**kwargs)
        ap = Academic.objects.filter(student=id)


        context['ap'] =  ap
        return context

class AcceptApply(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['did']
        ap = Jobapply.objects.get(pk=id)
        ap.a_status = 'Accept'
        ap.save()

        return  render(request,'company/com_index.html',{'message':"Application Accepted"})

class AddPlacedStud(View):
    def dispatch(self, request, *args, **kwargs):
        did = self.request.GET['did']
        joba = self.request.GET['joba']
        j = self.request.GET['j']

        pal = PlacedStudent.objects.filter(student=did,place_status='Placed').count()
        if pal>0:
            return  render(request,'company/com_index.html',{'message':"Student Already Placed!"})
        else:

            a = Stud_Reg.objects.get(pk=did)
            aj = Jobapply.objects.get(pk=joba)
            j = Job.objects.get(pk=j)
            tv = j.no_vacan
            fv = int(tv)-1
            j.no_vacan = fv
            j.save()
            asc = Reg.objects.get(user_id=self.request.user.id)
            ap = PlacedStudent()
            ap.student = a
            ap.jobapply = aj
            ap.company = asc
            ap.place_status = 'Placed'
            ap.save()

            return  render(request,'company/com_index.html',{'message':"Student Added as Placed"})
class AddNotPlacedStud(View):
    def dispatch(self, request, *args, **kwargs):
        did = self.request.GET['did']
        joba = self.request.GET['joba']
        j = self.request.GET['j']

        pal = PlacedStudent.objects.filter(student=did,place_status='Placed').count()
        if pal>0:
            return  render(request,'company/com_index.html',{'message':"Student Already Placed!"})
        else:

            a = Stud_Reg.objects.get(pk=did)
            aj = Jobapply.objects.get(pk=joba)
            # j = Job.objects.get(pk=j)
            # tv = j.no_vacan
            # fv = int(tv)-1
            # j.no_vacan = fv
            # j.save()
            asc = Reg.objects.get(user_id=self.request.user.id)
            ap = PlacedStudent()
            ap.student = a
            ap.jobapply = aj
            ap.company = asc
            ap.place_status = 'Not Placed'
            ap.save()

            return  render(request,'company/com_index.html',{'message':"Student Added as Placed"})


class PlacedStudents(TemplateView):
    template_name = 'company/placedstudents.html'

    def get_context_data(self, **kwargs):

        context = super(PlacedStudents,self).get_context_data(**kwargs)
        ap = PlacedStudent.objects.filter(company__user_id=self.request.user.id,place_status='Placed')


        context['ap'] =  ap
        return context


