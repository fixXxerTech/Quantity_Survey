from . import forms
from os.path import join as join_path
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import View as custom_view


# def excavate_oversite(cal_CB, petrol, labour, number_of_m3):
#     pertol_day = petrol * 70.00
#     labour = labour * 1
#     total_resources = (cal_CB + pertol_day + labour)
#     resources_per_m3 = total_resources / number_of_m3

#     print(resources_per_m3)
#     return resources_per_m3


# def hand_excavation(labour, percentage, number_of_m3):
#     # (15/100)*(1500.00/1)
#     forman = (percentage / 100) * (labour / 1)
#     labour = labour * 1
#     total_resources = (forman + labour)
#     resources_per_m3 = total_resources / number_of_m3

#     print(resources_per_m3)
#     return resources_per_m3


# def machine_excavation(excavator, petrol, labour, number_of_m3):
#     pertol_day = petrol * 70.00
#     excavator_per_day = excavator * 1
#     labour = labour * 1
#     total_resources = (pertol_day + excavator_per_day + labour )
#     resources_per_m3 = total_resources / number_of_m3

#     print(resources_per_m3)
#     return resources_per_m3


class AddResourcesPageView(custom_view):
    template_name = join_path("addresources.html")

    def get(self, request):

        form = forms.ResourceForm()

        context = {
            "resource_form": form,
        }

        return render(request, self.template_name, context=context)

    def post(self, request):
        for i in request.POST:
            print(i)
        form = forms.ResourceForm(request.POST)
        if form.is_valid():
            # form.save(commit=False)
            # form.active_user = request.user
            form.save()
            print("Valid form")
            return redirect(reverse_lazy("AddResourcesView"))
        else:
            print("Invalid form")

        context = {
            "resource_form": form,
        }
        print("Success")

        return render(request, self.template_name, context=context)


# class CalculationsPageView(custom_view, ):
#     template_name = join_path("calculations.html")

#     def get(self, request, pk):


#         # form = forms.ResourceForm()
#         excavate_oversite(cal_CB=pk.cal_DB_per_day, petrol=pk.petrol_per_liter,
#                           labour=labour_per_day, number_of_m3=200)

#         context = {
#             "resource_form": form,
#         }

#         return render(request, self.template_name, context=context)

#     def post(self, request, pk):
#         for i in request.POST:
#             print(i)
#         form = forms.ResourceForm(request.POST)
#         if form.is_valid():
#             # form.save(commit=False)
#             # form.active_user = request.user
#             form.save()
#             print("Valid form")
#             return redirect(reverse_lazy("AddResourcesView"))
#         else:
#             print("Invalid form")

#         context = {
#             "resource_form": form,
#         }
#         print("Success")

#         return render(request, self.template_name, context=context)
