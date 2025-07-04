from django.shortcuts import render,redirect
from . models import Task
from datetime import timedelta,datetime
from django.core.paginator import Paginator

def add_task(request):
    if request.method=="POST":
        title=request.POST.get("title")
        description=request.POST.get("description")
        obj=request.POST.get("id")
        object=Task.objects.all()
        for item in object:
            if item.id ==obj:
              Task.save(title=title,description=description)
        Task.objects.create(title=title,description=description)
      
        return redirect("/plan")
    return render(request,"todolist_app/add.html",{})


def list_task_not_done(request):
    list_task=Task.objects.filter(situation=False).order_by('-id') 
    page=request.GET.get('page')
    paginator=Paginator(list_task,4)
    page_obj=paginator.get_page(page)
    return render(request,"todolist_app/do_not.html",context={"page_obj":page_obj})
def delete(request,task_id):
    delete_object=Task.objects.get(id=task_id)
    delete_object.delete()
    return redirect("/plan")


def edit(request,task_id):
    if request.method=="POST":
          title=request.POST.get("title")
          description=request.POST.get("description")
          object=Task.objects.get(id=task_id)
          object.title=title
          object.description=description
          object.save()
          return redirect("/plan")


    object=Task.objects.get(id=task_id)
    title=object.title
    description=object.description
    return render (request,"todolist_app/edit.html",{"title":title,'description':description})


def start_task(request,task_id):
    object=Task.objects.get(id=task_id)
    object.datetime_start=datetime.now()
    object.save()
    return render(request,"home_app/index.html")


def end_task(request,task_id):
     object=Task.objects.get(id=task_id)
     object.datetime_end=datetime.now()
     object.save()
     return render(request,"home_app/index.html")



def complete_task(request,task_id):
    object=Task.objects.get(id=task_id)
    print(object)
    object.situation=True
    object.save()
    list_task=Task.objects.filter(situation=False).order_by("-id")
    page=request.GET.get("page")
    paginator=Paginator(list_task,4)
    page_obj=paginator.get_page(page)
    return render(request,"todolist_app/do_not.html",context={"page_obj":page_obj})
    


def list_task_done(request):
    durations=[]
    objects=Task.objects.filter(situation=True).order_by("-id")
    page=request.GET.get('page')
    print("page:",page)
    for item in objects:
        start_time=item.datetime_start
        end_time=item.datetime_end
        if start_time and end_time:
                  start_time = item.datetime_start.replace(second=0, microsecond=0)
                  end_time = item.datetime_end.replace(second=0, microsecond=0)
                  duration=end_time-start_time
                  durations.append(duration)
        else:
          durations.append("زمان تسک ثبت نشده")
    objects=list(zip(objects,durations))
    paginator=Paginator(objects,3)
    page_obj=paginator.get_page(page)
    return render(request,"todolist_app/complete.html",context={"page_obj":page_obj})


    
