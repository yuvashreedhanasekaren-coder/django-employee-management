from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee

# HOME PAGE
def home(request):
    return render(request, 'employees/home.html')


# ADD EMPLOYEE
from django.db import IntegrityError

def add_employee(request):
    if request.method == "POST":
        emp = Employee(
            emp_id=request.POST.get("emp_id"),
            name=request.POST.get("name"),
            designation=request.POST.get("designation"),
            experience=request.POST.get("experience"),
        )

        if request.FILES.get("image"):
            emp.image = request.FILES["image"]

        emp.save()
        return redirect("employee_list")

    return render(request, "employees/add_employee.html")

# SEARCH EMPLOYEE
# def search_employee(request):
#     if request.method == "POST":
#         emp_id = request.POST.get('emp_id')
#         try:
#             emp = Employee.objects.get(emp_id=emp_id)
#             return render(request, 'employees/profile.html', {'emp': emp})
#         except Employee.DoesNotExist:
#             return render(request, 'employees/search.html', {
#                 'error': 'Employee not found'
#             })

#     return render(request, 'employees/search.html')

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {
        'employees': employees
    })

def edit_employee(request, emp_id):
    emp = Employee.objects.get(emp_id=emp_id)

    if request.method == "POST":
        emp.name = request.POST.get("name")
        emp.designation = request.POST.get("designation")
        emp.experience = request.POST.get("experience")

        # Update image only if a new image is selected
        if request.FILES.get("image"):
            emp.image = request.FILES["image"]

        emp.save()

        return redirect("employee_list")

    return render(
        request,
        "employees/edit_employee.html",
        {"emp": emp}
    )

def delete_employee(request, emp_id):
    employee = get_object_or_404(Employee, emp_id=emp_id)

    if request.method == "POST":
        employee.delete()
        return redirect('employee_list')

    return render(request, 'employees/delete_confirm.html', {
        'employee': employee
    })

def search_options(request):
    return render(request, "employees/search_options.html")


def search_by_id(request):
    if request.method == "POST":
        emp_id = request.POST.get("emp_id")
        employees = Employee.objects.filter(emp_id=emp_id)

        if not employees.exists():
            return render(request, "employees/search_by_id.html", {
                "error": "No employee found"
            })

        return render(request, "employees/employee_list.html", {
            "employees": employees
        })

    return render(request, "employees/search_by_id.html")


def search_by_role(request):
    if request.method == "POST":
        designation = request.POST.get("designation")
        employees = Employee.objects.filter(designation__iexact=designation)

        if not employees.exists():
            return render(request, "employees/search_by_role.html", {
                "error": "No employee found"
            })

        return render(request, "employees/employee_list.html", {
            "employees": employees
        })

    return render(request, "employees/search_by_role.html")
