from django import forms
from .models import Schedule

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['date', 'title' , 'content']
        widgets = {
            'date': forms.TextInput(attrs={'type': 'date'}),
        }
        input_formats = ['%Y-%m-%d']