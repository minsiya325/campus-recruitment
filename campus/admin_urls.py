from django.urls import path
from django.contrib.auth import views as auth_views

from campus.admin_views import IndexView,  RejectView, NewCompany, ApproveView, ViewCompany, \
    AddPlacement, ViewPlacements, RejectPlacement, NewStudents, ViewStudents, AddCourse, Chat,PlacedStudents, CommonMessage

urlpatterns = [
    path('', IndexView.as_view()),
    path('AddCourse', AddCourse.as_view()),
    path('NewCompany', NewCompany.as_view()),
    path('ViewCompany', ViewCompany.as_view()),
    path('NewStudents', NewStudents.as_view()),
    path('ViewStudents', ViewStudents.as_view()),
    path('Chat', Chat.as_view()),
    path('CommonMessage', CommonMessage.as_view()),



    path('RejectView', RejectView.as_view()),
    path('ApproveView', ApproveView.as_view()),
    path('AddPlacement', AddPlacement.as_view()),
    path('PlacedStudents', PlacedStudents.as_view()),
    path('ViewPlacements', ViewPlacements.as_view()),
    path('RejectPlacement', RejectPlacement.as_view()),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='/'
        ),
        name='logout'
    ),





]

def urls():
    return urlpatterns, 'admin', 'admin'