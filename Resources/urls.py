from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.AddResourcesPageView.as_view(),
         name="AddResourcesView"),
    # path('calculations/<pk>/',
    #      views.CalculationsPageView.as_view(),
    #      name="calculationsView"),
]
