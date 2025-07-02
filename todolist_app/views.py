from django.shortcuts import render,redirect
from . models import todolist
from datetime import timedelta,datetime

def add_task(request):
    if request.method=="POST":
        title=request.POST.get("title")
        description=request.POST.get("description")
        obj=request.POST.get("id")
        object=todolist.objects.all()
        for item in object:
            if item.id ==obj:
              todolist.save(title=title,description=description)
        todolist.objects.create(title=title,description=description)
        print(todolist)
        return redirect("/plan")
    return render(request,"todolist_app/add.html",{})


def list_task_not_done(request):
    list_task=todolist.objects.filter(situation=False)
    return render(request,"todolist_app/do_not.html",context={"list_task":list_task})
   

def delete(request,task_id):
    delete_object=todolist.objects.get(id=task_id)
    delete_object.delete()
    return redirect("/plan")



def edit(request,task_id):
    if request.method=="POST":
          title=request.POST.get("title")
          description=request.POST.get("description")
          object=todolist.objects.get(id=task_id)
          object.title=title
          object.description=description
          object.save()
          return redirect("/plan")

    object=todolist.objects.get(id=task_id)
    title=object.title
    description=object.description
    return render (request,"todolist_app/edit.html",{"title":title,'description':description})


def start_task(request,task_id):
    object=todolist.objects.get(id=task_id)
    object.datetime_start=datetime.now()
    object.save()
    return render(request,"home_app/home.html")


def end_task(request,task_id):
     object=todolist.objects.get(id=task_id)
     object.datetime_end=datetime.now()
     object.save()
     return render(request,"home_app/home.html")



def complete_task(request,task_id):
    object=todolist.objects.get(id=task_id)
    object.situation=True
    object.save()
    list_task=todolist.objects.filter(situation=False)
    return render(request,"todolist_app/do_not.html",context={"list_task":list_task})
    


def list_task_done(request):
    durations=[]
    objects=todolist.objects.filter(situation=True)
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
    total_time=[]      
    for item in durations:
        if item !=("زمان تسک ثبت نشده"):
          total_time.append(item)
    total_time=sum(total_time,timedelta())
    objects=zip(objects,durations)
    return render(request,"todolist_app/complete.html",context={"objects":objects,"total_time":total_time})


    
