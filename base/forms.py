from django.forms import ModelForm
from .models import Volunteer,JoinEvent

class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        fields = '__all__'

class EventForm(ModelForm):
    class Meta:
        model = JoinEvent
        fields = '__all__'
