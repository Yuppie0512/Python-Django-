from django.shortcuts import render
from django.http import HttpResponse
#from yourapp.models import TaskSuite  # 假设你有一个名为TaskSuite的模型

def create_task_suite(request):
    if request.method == 'POST':
        task_suite_name = request.POST.get('task_suite_name')  # 获取从前端传递过来的任务套件名称
        #new_task_suite = TaskSuite(name=task_suite_name)
        #new_task_suite.save()  # 在数据库中保存任务套件名称
        return HttpResponse('任务套件已成功创建和保存！任务套件名称为'+task_suite_name)
    else:
        return render(request, 'index.html')