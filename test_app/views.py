from django.shortcuts import render
from django.http import HttpResponse
from test_app.models import Application
from test_app.forms import ApplicationForm
import json
from datetime import datetime


def home(request):
    form = ApplicationForm()
    message = None
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            appl = Application.objects.latest('id')
            message = u'{0}, запись к врачу оформлена успешно! Врач: {1}, дата: {2}, время: {3} часов'.format(
                appl.name_pacient, appl.doctor, appl.date_of_receipt, appl.time_of_receipt)
            return render(request, 'index.html', {'form': form, 'message': message, })
    return render(request, 'index.html', {'form': form})


def get_time(request, *args, **kwargs):
    date = request.GET['date']
    date = datetime.strptime(date, '%m/%d/%Y')
    doctor = request.GET['doctor']
    applications = Application.objects.filter(doctor=doctor, date_of_receipt=date)
    time_list = dict(Application.TIME)
    for application in applications:
        try:
            del time_list[application.time_of_receipt]
        except:
            pass
    return HttpResponse(json.dumps(time_list), content_type="application/json")
