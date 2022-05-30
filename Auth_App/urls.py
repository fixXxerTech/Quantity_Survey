from django.urls import path
from . import views

urlpatterns = [
    path('login/',
         views.LoginView.as_view(),
         name="LoginView"),
    path('register/',
         views.RegisterView.as_view(),
         name="RegisterView"),
    path('datatable/',
         views.DataTablePageView.as_view(),
         name="DataTableView"),
    path('regulartable/',
         views.RegularTablePageView.as_view(),
         name="RegularTableView"),
    path('calculations/<pk>/',
         views.CalculationsPageView.as_view(),
         name="calculationsView"),
]
