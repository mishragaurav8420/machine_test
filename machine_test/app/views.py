from django.shortcuts import render
from app.task import my_task
def my_view(request):
    data=[1,2,3,4,5]
    result=process_data.delay(data)
    return HttpResponse('task trigrred sucessfully')

# Create your views here.
