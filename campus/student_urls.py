from django.urls import path
from django.contrib.auth import views as auth_views

from campus.student_views import IndexView, AddAcademic, UpdateProfile, ViewPlacements, DriveDetails, JobDetails, \
    ApplyJob, MyApply,Chat, PlacedStudents

urlpatterns = [
    path('', IndexView.as_view()),
    path('AddAcademic', AddAcademic.as_view()),
    path('UpdateProfile', UpdateProfile.as_view()),
    path('ViewPlacements', ViewPlacements.as_view()),
    path('DriveDetails', DriveDetails.as_view()),
    path('JobDetails', JobDetails.as_view()),
    path('ApplyJob', ApplyJob.as_view()),
    path('MyApply', MyApply.as_view()),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='/'
        ),
        name='logout'
    ),
    path('changepassword',auth_views.PasswordChangeView.as_view(template_name='student/change_password.html',success_url='/')),
    path('Chat',Chat.as_view()),
    path('PlacedStudents',PlacedStudents.as_view()),



]

def urls():
    return urlpatterns, 'student', 'student'