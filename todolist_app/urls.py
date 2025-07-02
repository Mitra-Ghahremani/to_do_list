from django.urls import path
from . import views

app_name="todolist_app"
urlpatterns=[path("add",views.add_task,name="add"),
             path("list_task_not_done",views.list_task_not_done,name="list_not_done"),
             path("delete/<int:task_id>",views.delete,name="delete"),
             path("edit/<int:task_id>",views.edit,name="edit"),
             path("start/<int:task_id>",views.start_task,name="start"),
             path("end/<int:task_id>",views.end_task,name="end"),
             path("complete_task/<int:task_id>",views.complete_task,name="complete_task"),
             path("list_task_done",views.list_task_done,name="list_done")]
