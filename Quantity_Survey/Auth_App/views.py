from . import forms
from . import models
from django.apps import apps
from os.path import join as join_path
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
"""
The import below is so you can specify what happens in your get and post requests your self. If you check the django source code, /
you will find that all the other class based views inherit this one so to avoid the confusion of queryset and all those extra stuff'
I just use this. Feel free to use what ever you want

"""
from django.views.generic.base import View as custom_view

from django.contrib.auth import views as auth_views

# To get the model from the other app
sourcedata_model = apps.get_model("Resources", "SourceData")


def excavate_oversite(cal_CB, petrol, labour, number_of_m3, number_of_ptrol_liter):
    pertol_day = petrol * number_of_ptrol_liter
    labour = labour * 1
    total_resources = (cal_CB + pertol_day + labour)
    resources_per_m3 = total_resources / number_of_m3

    print(resources_per_m3)
    return resources_per_m3


def hand_excavation(labour, percentage, number_of_m3):
    # (15/100)*(1500.00/1)
    forman = (percentage / 100) * (labour / 1)
    labour = labour * 1
    total_resources = (forman + labour)
    resources_per_m3 = total_resources / number_of_m3

    print(resources_per_m3)
    return resources_per_m3


def machine_excavation(excavator, petrol, labour, number_of_m3, number_of_ptrol_liter):
    excavator_per_day = excavator * 1
    petrol_day = petrol * number_of_ptrol_liter
    labour = labour * 1
    total_resources = (petrol_day + excavator_per_day + labour)
    resources_per_m3 = total_resources / number_of_m3

    print(resources_per_m3)
    return resources_per_m3


def backfill_and_compact(labour, output_m3_per_day):
    labour = labour * 1
    total_resources = labour
    resources_per_m3 = total_resources / output_m3_per_day

    print(resources_per_m3)
    return resources_per_m3


def level_and_compact(labour, output_m2_per_day):
    labour = labour * 1
    total_resources = labour
    resources_per_m3 = total_resources / output_m2_per_day

    print(resources_per_m3)
    return resources_per_m3


class DataTablePageView(custom_view):
    template_name = join_path("filtertableview.html")

    def get(self, request):
        all_records = sourcedata_model.objects.all()
        # date_filtered_records = sourcedata_model.objects.filter(
        # 	record_date__range=[from_date, to_date]
        # )

        context = {
            "survey_records": all_records,
            # "filtered_records":date_filtered_records,
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        all_records = sourcedata_model.objects.all()
        # date_filtered_records = sourcedata_model.objects.filter(
        #     record_date__range=[from_date, to_date]
        # )

        context = {
            "survey_records": all_records,
            # "filtered_records": date_filtered_records,
        }
        return render(request, self.template_name, context=context)


class RegularTablePageView(custom_view):
    template_name = join_path("regulartableview.html")

    def get(self, request):
        all_records = sourcedata_model.objects.all()

        context = {
            "survey_records": all_records,
        }

        return render(request, self.template_name, context=context)

    def post(self, request):
        all_records = sourcedata_model.objects.all()

        # date_filtered_records = sourcedata_model.objects.filter(
        #     record_date__range=[from_date, to_date]
        # )

        context = {
            "survey_records": all_records,
            # "filtered_records": date_filtered_records,
        }

        return render(request, self.template_name, context=context)


class RegisterView(custom_view):
    template_name = join_path("Auth_templates", "register.html")

    def get(self, request):
        form = forms.RegisterForm()
        profile_form = forms.UserProfileForm()

        context = {
            "form": form,
            "profile_form": profile_form,
        }

        return render(request, self.template_name, context=context)

    def post(self, request):
        form = forms.RegisterForm(request.POST)
        profile_form = forms.UserProfileForm(request.POST)

        context = {
            "form": form,
            "profile_form": profile_form,
        }

        try:
            if form.is_valid() and profile_form.is_valid():
                new_surveyor = form.save(commit=False)
                # Old habits die hard. In newer django, you do not need to declear this
                new_surveyor.is_active = True
                new_surveyor.save()

                new_surveyor_profile = profile_form.save(commit=False)
                new_surveyor_profile.user = new_surveyor
                new_surveyor_profile.save()

            messages.success(request, f'Account created for {username}!')

            # You can add some logic here to send email to the surveyor(s)
        except Exception as Error:
            raise Error

        return render(request, self.template_name, context=context)


class LoginView(auth_views.LoginView):

    form_class = forms.LoginForm
    redirect_authenticated_user = True
    authentication_form = forms.LoginForm
    # success_url = reverse_lazy('DataTableView')
    template_name = join_path('Auth_templates', 'login.html')

    # def get_success_url(self):
    # url = self.get_redirect_url()
    # if url:
    #     return url
    # elif self.request.user.is_superuser:
    #     return reverse("admin")
    # else:
    #     return reverse("profile")

    def form_valid(self, form):

        checkbox = form.cleaned_data['remember_me']
        return super().form_valid(form)


print('Done with auth views')


class CalculationsPageView(custom_view, ):
    template_name = join_path("calculations.html")

    def get(self, request, pk):

        sourcedata_instance = sourcedata_model.objects.get(pk=pk)
        # form = forms.ResourceForm()
        excavate_oversite_value = excavate_oversite(cal_CB=sourcedata_instance.cal_DB_per_day, petrol=sourcedata_instance.petrol_price_per_liter,
                                                    labour=sourcedata_instance.labour_per_day, number_of_m3=200, number_of_ptrol_liter=70.00)

        hand_excavation_value = hand_excavation(labour=sourcedata_instance.labour_per_day,
                                                percentage=15, number_of_m3=1.5)

        machine_excavation_value = machine_excavation(excavator=sourcedata_instance.extractor_per_day,
                                                      petrol=sourcedata_instance.petrol_price_per_liter, labour=sourcedata_instance.labour_per_day, number_of_m3=125, number_of_ptrol_liter=70.00)

        backfill_and_compact_value = backfill_and_compact(
            labour=sourcedata_instance.labour_per_day, output_m3_per_day=4)

        level_and_compact_value = level_and_compact(
            labour=sourcedata_instance.labour_per_day, output_m2_per_day=10)

        context = {
            # "resource_form": form,
            "hand_excavation": hand_excavation_value,
            "level_and_compact": level_and_compact_value,
            "excavate_oversite": excavate_oversite_value,
            "machine_excavation": machine_excavation_value,
            "backfill_and_compact": backfill_and_compact_value,
        }

        print(context["excavate_oversite"])
        return render(request, self.template_name, context=context)

    # def post(self, request, pk):
    #     for i in request.POST:
    #         print(i)
    #     form = forms.ResourceForm(request.POST)
    #     if form.is_valid():
    #         # form.save(commit=False)
    #         # form.active_user = request.user
    #         form.save()
    #         print("Valid form")
    #         return redirect(reverse_lazy("calculationsView"))
    #     else:
    #         print("Invalid form")

    #     context = {
    #         "resource_form": form,
    #     }
    #     print("Success")

    #     return render(request, self.template_name, context=context)
