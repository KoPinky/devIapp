from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import WorkList
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# получение данных из бд
def index(request):
    data = serializers.serialize('json', WorkList.objects.all())
    return HttpResponse(data, content_type='application/json')

# сохранение данных в бд
# @csrf_exempt
def create(request):
    if request.method == "POST":
        print(request.POST.get("work"))
        work_list = WorkList()
        
        work_list.work = request.POST.get("work")
        work_list.complete = False
        work_list.save()
    data = serializers.serialize('json', WorkList.objects.all())
    return HttpResponse(data, content_type='application/json')
 
# изменение данных в бд
def edit(request, id):
    try:
        work_list = WorkList.objects.get(id=id)
 
        if request.method == "POST":
            work_list.name = request.POST.get("name")
            work_list.age = request.POST.get("age")
            work_list.save()
            data = serializers.serialize('json', WorkList.objects.all())
            return HttpResponse(data, content_type='application/json')
        else:
            data = serializers.serialize('json', WorkList.objects.all())
            return HttpResponse(data, content_type='application/json')
    except WorkList.DoesNotExist:
        data = serializers.serialize('json', WorkList.objects.all())
        return HttpResponse(data, content_type='application/json')
     
# удаление данных из бд
def delete(request, id):
    try:
        work_list = WorkList.objects.get(id=id)
        work_list.delete()
        data = serializers.serialize('json', WorkList.objects.all())
        return HttpResponse(data, content_type='application/json')
    except WorkList.DoesNotExist:
        data = serializers.serialize('json', WorkList.objects.all())
        return HttpResponse(data, content_type='application/json')