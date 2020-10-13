from django.http import request
from django.shortcuts import render

# Create your views here.
def createfunc(request):
    # POST method
    if request.method == 'POST':
        pass

    # GET method
    return render(request, 'create_deliverable_info.html', {})
