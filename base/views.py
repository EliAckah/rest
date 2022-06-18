from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from .models import Volunteer,Executive,Cause,Event,JoinEvent
from .forms import VolunteerForm,EventForm

def home(request):
    executives = Executive.objects.all()
    causes = Cause.objects.all()
    if request.method == 'POST':

        new_volunteer = Volunteer(
            name=request.POST['name'],
            email=request.POST['email'],
            phone_number=request.POST['contact'],
            Why_you_want_to_volunteer=request.POST['reason'],
            
            )
        new_volunteer.save()
        return redirect('volunteer-list')
    context = {'executives':executives,'causes':causes}
    return render(request,'base/home.html',context)

def about(request):
    executives = Executive.objects.all()
    context = {'executives':executives}
    return render(request,'base/about.html',context)

def events(request):
    events = Event.objects.all()
    context = {'events':events}
    return render(request,'base/event.html',context)

# def eventForm(request):
#     form = EventForm()
#     events = Event.objects.all()
#     if request.method == 'POST':
#         event_name = request.POST.get('event_title')
#         event = Event.objects.get(event_title=event_name)

#         join_event = JoinEvent(
#             name=request.POST['name'],
#             email=request.POST['email'],
#             phone_number=request.POST['contact'],
#             event_to_join=event,
            
#             )
#         join_event.save()
#         return redirect('join-event')
#     context = {'form':form,'events':events}
#     return render(request,'base/event-form.html',context)
def eventDetail(request,slug):
    event = get_object_or_404(Event,slug=slug)
    if request.method == 'POST':
        join_event = JoinEvent(
            name = request.POST['name'],
            email = request.POST['email'],
            phone_number = request.POST['contact'],
            event_to_join = event
            )
        join_event.save()
        return redirect('events')
    context = {'event':event}
    return render(request,'base/event-detail.html',context)

def causes(request):
    causes = Cause.objects.all()
    context = {'causes':causes}
    return render(request,'base/causes.html',context)

def causeDetail(request,slug):
    cause = get_object_or_404(Cause,slug=slug)
    context = {'cause':cause}
    return render(request,'base/cause-detail.html',context)

def contact(request):
    return render(request,'base/contact.html')

def donate(request):
    return render(request,'base/donate.html')

def volunteer(request):
    if request.method == 'POST':

        new_volunteer = Volunteer(
            name=request.POST['name'],
            email=request.POST['email'],
            phone_number=request.POST['contact'],
            Why_you_want_to_volunteer=request.POST['reason'],
            
            )
        new_volunteer.save()
        return redirect('volunteer-list')

    return render(request, 'base/volunteer.html')

def volunteerList(request):
    volunteer_list = Volunteer.objects.all()
    volunteer_count = volunteer_list.count()
    context = {'volunteer_list':volunteer_list,'volunteer_count':volunteer_count}
    return render(request,'base/volunteer-list.html',context)