from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def add(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'main/add.html', {'form': form})

@login_required(login_url='/login')
def index(request):
    employees = Employee.objects.all()
    return render(request, "main/index.html", {'employees': employees})

@login_required(login_url='/login')
def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'main/edit.html', {'employee': employee})

@login_required(login_url='/login')
def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'main/edit.html', {'employee': employee})

@login_required(login_url='/login')
def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/")
