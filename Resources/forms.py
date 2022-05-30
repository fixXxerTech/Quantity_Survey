from django import forms
from django.apps import apps
from .models import SourceData

class ResourceForm(forms.ModelForm):

    description = forms.CharField(
        label='Description',
        widget=forms.TextInput(
            attrs={

                'type': 'text',
                'id': 'description',
                'name': 'description',
                'placeholder': '',
                'class': 'form-control form-control-lg',
            }
        )
    )

    labour_per_day = forms.DecimalField(
        label='labour per day',
        widget=forms.NumberInput(
            attrs={

                'id': 'labour',
                'name': 'labour',
                'type': 'number',
                'placeholder': "",
                'class': 'form-control form-control-lg',


            }
        )
    )

    artisan_per_day = forms.DecimalField(
        label='artisan per day',
        widget=forms.NumberInput(
            attrs={

                'id': 'artisan',
                'name': 'artisan',
                'type': 'number',
                'placeholder': "",
                'class': 'form-control form-control-lg',

            }
        )
    )

    cal_DB_per_day = forms.DecimalField(
        label='cal DB per day',
        widget=forms.NumberInput(
            attrs={

                'id': 'cal_DB',
                'name': 'cal_DB',
                'type': 'number',
                'placeholder': "",
                'class': 'form-control form-control-lg',

            }
        )
    )

    diesel_price_per_liter = forms.DecimalField(
        label='diesel price per liter',
        widget=forms.NumberInput(
            attrs={

                'id': 'diesel',
                'name': 'diesel',
                'type': 'number',
                'placeholder': "",
                'class': 'form-control form-control-lg',

            }
        )
    )

    petrol_price_per_liter = forms.DecimalField(
        label='petrol price per liter',
        widget=forms.NumberInput(
            attrs={

                'id': 'petrol',
                'name': 'petrol',
                'type': 'number',
                'placeholder': "",
                'class': 'form-control form-control-lg',

            }
        )
    )

    extractor_per_day = forms.DecimalField(
        label='extractor per day',
        widget=forms.NumberInput(
            attrs={

                'id': 'extractor',
                'name': 'extractor',
                'type': 'number',
                'placeholder': "",
                'class': 'form-control form-control-lg',

            }
        )
    )

    dieldrex_per_liter = forms.DecimalField(
        label='dieldrex per liter',
        widget=forms.NumberInput(
            attrs={

                'id': 'dieldrex',
                'name': 'dieldrex',
                'type': 'number',
                'placeholder': "",
                'class': 'form-control form-control-lg',

            }
        )
    )

    laterite_per_m3 = forms.DecimalField(
        label='laterite per m3',
        widget=forms.NumberInput(
            attrs={

                'id': 'laterite',
                'name': 'laterite',
                'type': 'number',
                'placeholder': "",
                'class': 'form-control form-control-lg',

            }
        )
    )

    hand_roller_per_day = forms.DecimalField(
        label='hand roller per day',
        widget=forms.NumberInput(
            attrs={

                'id': 'handroller',
                'name': 'handroller',
                'type': 'number',
                'placeholder': "",
                'class': 'form-control form-control-lg',

            }
        )
    )

    hardcore_per_m3 = forms.DecimalField(
        label='hardcore per m3',
        widget=forms.NumberInput(
            attrs={

                'id': 'hardcore',
                'name': 'hardcore',
                'type': 'number',
                'placeholder': "",
                'class': 'form-control form-control-lg',

            }
        )
    )

    tipper_per_day = forms.DecimalField(
        label='tipper per day',
        widget=forms.NumberInput(
            attrs={

                'id': 'tipper',
                'name': 'tipper',
                'type': 'number',
                'placeholder': "",
                'class': 'form-control form-control-lg',

            }
        )
    )

    polythene_per_roll = forms.DecimalField(
        label='polythene per roll',
        widget=forms.NumberInput(
            attrs={

                'id': 'polythene',
                'name': 'polythene',
                'type': 'number',
                'placeholder': "",
                'class': 'form-control form-control-lg',

            }
        )
    )

    cement_per_bag = forms.DecimalField(
        label='cement per bag',
        widget=forms.NumberInput(
            attrs={

                'id': 'cement',
                'name': 'cement',
                'type': 'number',
                'placeholder': "",
                'class': 'form-control form-control-lg',

            }
        )
    )

    sharp_sand_per_m3 = forms.DecimalField(
        label='Sharp sand per m3',
        widget=forms.NumberInput(
            attrs={

                'id': 'sharp_sand',
                'name': 'sharp_sand',
                'type': 'number',
                'placeholder': "",
                'class': 'form-control form-control-lg',

            }
        )
    )

    so_sand_per_m3 = forms.DecimalField(
        label='SO sand per m3',
        widget=forms.NumberInput(
            attrs={

                'id': 'so_sand',
                'name': 'so_sand',
                'type': 'number',
                'placeholder': "",
                'class': 'form-control form-control-lg',

            }
        )
    )

    granite_per_m3 = forms.DecimalField(
        label='granite per m3',
        widget=forms.NumberInput(
            attrs={

                'id': 'granite',
                'name': 'granite',
                'type': 'number',
                'placeholder': "",
                'class': 'form-control form-control-lg',

            }
        )
    )

    mixer_poker_operator_per_day = forms.DecimalField(
        label='mixer poker operator per day',
        widget=forms.NumberInput(
            attrs={

                'id': 'mixer_poker_operator',
                'name': 'mixer_poker_operator',
                'type': 'number',
                'placeholder': "",
                'class': 'form-control form-control-lg',

            }
        )
    )

    HT_bars_per_ton = forms.DecimalField(
        label='HT bars per ton',
        widget=forms.NumberInput(
            attrs={

                'id': 'HT_bars',
                'name': 'HT_bars',
                'type': 'number',
                'placeholder': "",
                'class': 'form-control form-control-lg',

            }
        )
    )

    MS_bars_per_ton = forms.DecimalField(
        label='MS bars per ton',
        widget=forms.NumberInput(
            attrs={

                'id': 'MS_bars',
                'name': 'MS_bars',
                'type': 'number',
                'placeholder': "",
                'class': 'form-control form-control-lg',

            }
        )
    )

    binding_wire_per_kg = forms.DecimalField(
        label='binding wire per kg',
        widget=forms.NumberInput(
            attrs={

                'id': 'binding_wire',
                'name': 'binding_wire',
                'type': 'number',
                'placeholder': "",
                'class': 'form-control form-control-lg',

            }
        )
    )

    BRC_65 = forms.DecimalField(
        label='BRC 65',
        widget=forms.NumberInput(
            attrs={

                'id': 'BRC_65',
                'name': 'BRC_65',
                'type': 'number',
                'placeholder': "",
                'class': 'form-control form-control-lg',

            }
        )
    )

    A142_per_m2 = forms.DecimalField(
        label='A142 per m2',
        widget=forms.NumberInput(
            attrs={

                'id': 'A142',
                'name': 'A142',
                'type': 'number',
                'placeholder': "",
                'class': 'form-control form-control-lg',

            }
        )
    )

    class Meta:
        model = SourceData
        exclude = (
            # "active_user",
            "record_date",
        )

    # Overriding the .save() method is not really necessary, Ive just made a habit of doing it so i can put my own logic if need be
    # def save(self, commit=True):
    #     ResourceForm_instance = super(ResourceForm, self).save(commit=False)
    #     ResourceForm_instance.description = self.cleaned_data['description']
    #     ResourceForm_instance.labour_per_day = self.cleaned_data['labour_per_day']
    #     ResourceForm_instance.artisan_per_day = self.cleaned_data['artisan_per_day']
    #     ResourceForm_instance.cal_DB_per_day = self.cleaned_data['cal_DB_per_day']
    #     ResourceForm_instance.diesel_price_per_liter = self.cleaned_data['diesel_price_per_liter']
    #     ResourceForm_instance.petrol_price_per_liter = self.cleaned_data['petrol_price_per_liter']
    #     ResourceForm_instance.extractor_per_day = self.cleaned_data['extractor_per_day']
    #     ResourceForm_instance.dieldrex_per_liter = self.cleaned_data['dieldrex_per_liter']
    #     ResourceForm_instance.laterite_per_m3 = self.cleaned_data['laterite_per_m3']
    #     ResourceForm_instance.hand_roller_per_day = self.cleaned_data['hand_roller_per_day']
    #     ResourceForm_instance.hardcore_per_m3 = self.cleaned_data['hardcore_per_m3']
    #     ResourceForm_instance.tipper_per_day = self.cleaned_data['tipper_per_day']
    #     ResourceForm_instance.polythene_per_roll = self.cleaned_data['polythene_per_roll']
    #     ResourceForm_instance.cement_per_bag = self.cleaned_data['cement_per_bag']
    #     ResourceForm_instance.sharp_sand_per_m3 = self.cleaned_data['sharp_sand_per_m3']
    #     ResourceForm_instance.so_sand_per_m3 = self.cleaned_data['so_sand_per_m3']
    #     ResourceForm_instance.granite_per_m3 = self.cleaned_data['granite_per_m3']
    #     ResourceForm_instance.mixer_poker_operator_per_day = self.cleaned_data[
    #         'mixer_poker_operator_per_day']
    #     ResourceForm_instance.HT_bars_per_ton = self.cleaned_data['HT_bars_per_ton']
    #     ResourceForm_instance.MS_bars_per_ton = self.cleaned_data['MS_bars_per_ton']
    #     ResourceForm_instance.binding_wire_per_kg = self.cleaned_data['binding_wire_per_kg']
    #     ResourceForm_instance.BRC_65 = self.cleaned_data['BRC_65']
    #     ResourceForm_instance.A142_per_m2 = self.cleaned_data['A142_per_m2']


# active_user
# description
# labour_per_day
# artisan_per_day
# cal_DB_per_day
# diesel_price_per_liter
# petrol_price_per_liter
# extractor_per_day
# dieldrex_per_liter
# laterite_per_m3
# hand_roller_per_day
# hardcore_per_m3
# tipper_per_day
# polythene_per_roll
# cement_per_bag
# sharp_sand_per_m3
# so_sand_per_m3
# granite_per_m3
# mixer_poker_operator_per_day
# HT_bars_per_ton
# MS_bars_per_ton
# binding_wire_per_kg
# BRC_65
# A142_per_m2
# record_date
