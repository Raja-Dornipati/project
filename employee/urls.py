from django.urls import path
from employee.views import *

urlpatterns = [

    # path('', employee_list, name="employee_list"),
    # path('details/<int:id>/', employee_details, name="employee_details"),
    path('edit/<int:id>/', employee_edit, name="employee_edit"),
    path('add/', employee_add, name="employee_add"),
    path('delete/<int:id>/', employee_delete, name="employee_delete"),

]
