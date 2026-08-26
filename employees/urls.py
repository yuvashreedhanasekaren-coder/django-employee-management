from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_employee, name='add_employee'),
    path('list/', views.employee_list, name='employee_list'),  
    path("edit/<str:emp_id>/", views.edit_employee, name="edit_employee"),
    path('delete/<str:emp_id>/', views.delete_employee, name='delete_employee'),
    path('search/', views.search_options, name='search_options'),
    path('search/id/', views.search_by_id, name='search_by_id'),
    path('search/role/', views.search_by_role, name='search_by_role'),

]

