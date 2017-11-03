from django.shortcuts import render

import datetime
def signcalc(request):
    today = datetime.datetime.now().date()
    return render(request, 'SignCalcApp/index.html', {'today':today})