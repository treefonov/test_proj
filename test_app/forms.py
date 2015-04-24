from django import forms
from test_app.models import Application
from datetime import datetime


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name_pacient', 'doctor', 'date_of_receipt', 'time_of_receipt']
        widgets = {
            'date_of_receipt': forms.DateInput(attrs={'class': 'datepicker'}),
        }

    def clean_date_of_receipt(self):
        date = self.cleaned_data['date_of_receipt']
        day = date.isoweekday()
        if day == 6 or day == 7:
            raise forms.ValidationError("Выберите будний день - с понедельника по пятницу")
        elif date < datetime.today().date():
            raise forms.ValidationError("Эта дата прошла!")
        return date
