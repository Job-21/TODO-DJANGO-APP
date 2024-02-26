from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from ADD.models import ToDoData
# Create your views here.
def index(request):
    if request.method == 'POST':
        info = request.POST.get('add')
        data = ToDoData(task=info)
        data.save()
        return redirect('index')
    my_data = ToDoData.objects.all().values()
    context = {
            "data":my_data
        }

    return render(request, 'index.html', context)

def data_to_delete(request,pk):
    obj = ToDoData.objects.get(id=pk)
    obj.delete()
    return redirect('index')

def login_form(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        passwd = request.POST.get('pwd')
        user = authenticate(request, username=uname, password=passwd)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            context = {
                "info":"USERNAME OR PASSWORD IS INCORRECT"
            }
            return render(request, 'login.html', context)
    return render(request, 'login.html')
    