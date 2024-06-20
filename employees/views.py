from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {"employees":employees})

def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/create_employee.html', {'form': form})

