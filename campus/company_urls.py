from django.urls import path

from campus.company_views import IndexView, ViewPlacements, PlacementDetails, AddJob, ViewJob, StudApplication, \
    ViewAcademic, AcceptApply, AddPlacedStud,PlacedStudents, AddNotPlacedStud

urlpatterns = [
    path('', IndexView.as_view()),
    path('ViewPlacements', ViewPlacements.as_view()),
    path('PlacementDetails', PlacementDetails.as_view()),
    path('AddJob', AddJob.as_view()),
    path('ViewJob', ViewJob.as_view()),
    path('studapplication', StudApplication.as_view()),
    path('ViewAcademic', ViewAcademic.as_view()),
    path('AcceptApply', AcceptApply.as_view()),
    path('AddPlacedStud', AddPlacedStud.as_view()),
    path('AddNotPlacedStud', AddNotPlacedStud.as_view()),
    path('PlacedStudents', PlacedStudents.as_view()),






]

def urls():
    return urlpatterns, 'company', 'company'