from django.http import HttpResponse
from django.shortcuts import render
import joblib
import math
from datetime import datetime
from datetime import timedelta


def home(request):
    return render(request, "home.html")


def result(request):
    model = joblib.load('finalized_model.sav')

    lis = []

    lis.append(request.GET['noh'])
    lis.append(request.GET['avg'])
    lis.append(request.GET['nod'])

    print(lis)

    ans = model.predict([lis])
    ans = math.floor(ans)

    today = datetime.today().strftime('%Y-%m-%d')
    todaystring = str(today)
    begindate = datetime.strptime(todaystring, "%Y-%m-%d")
    enddate = begindate+timedelta(days=ans)
    enddatestring = str(enddate)
    maintenancedate = enddatestring[0:10:]

    return render(request, "result.html", {'ans': ans,'todaystring': todaystring, 'maintenancedate': maintenancedate })
