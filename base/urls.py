from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('events/',views.events,name="events"),
    path('events/<slug:slug>/',views.eventDetail,name="event_detail"),
    #path('events/join-event/',views.eventForm,name="join-event"),
    path('causes/',views.causes,name="causes"),
    path('causes/<slug:slug>/',views.causeDetail,name="cause_detail"),
    path('contact/',views.contact,name="contact"),
    path('donate/',views.donate,name="donate"),
    path('volunteer/',views.volunteer,name="volunteer"),
    path('volunteer-list/',views.volunteerList,name="volunteer-list"),
]
