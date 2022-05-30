from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

Authenticated_User = get_user_model()


class SourceData(models.Model):
    """
    Using individual model fields for each ( columns for each where all are on a single row ) is so much easier to query seperatly  
    These are obviously made up values, just change them

    <active_user> is not really necessary but i think you might find it useful to link whoever the logged in user wass who entered that record that day was, in the long run

    """
    # active_user = models.ForeignKey(
    #     Authenticated_User,
    #     on_delete=models.CASCADE,
    #     verbose_name="auth_user",
    #     related_name="user_data",
    #     blank=False
    # )
    # This time the decription is used to
    description = models.CharField(
        max_length=1000,
        null=False,
        blank=False
    )
    labour_per_day = models.IntegerField(
        default=0,
        null=True,
        blank=True,
    )
    artisan_per_day = models.IntegerField(
        default=0,
        null=True,
        blank=True,
    )
    cal_DB_per_day = models.IntegerField(
        default=0,
        null=True,
        blank=True,
    )
    diesel_price_per_liter = models.IntegerField(
        default=0,
        null=True,
        blank=True,
    )
    petrol_price_per_liter = models.IntegerField(
        default=0,
        null=True,
        blank=True,
    )
    extractor_per_day = models.IntegerField(
        default=0,
        null=True,
        blank=True,
    )
    dieldrex_per_liter = models.IntegerField(
        default=0,
        null=True,
        blank=True,
    )
    laterite_per_m3 = models.IntegerField(
        default=0,
        null=True,
        blank=True,
    )
    hand_roller_per_day = models.IntegerField(
        default=0,
        null=True,
        blank=True,
    )
    hardcore_per_m3 = models.IntegerField(
        default=0,
        null=True,
        blank=True,
        help_text="broken blks"
    )
    tipper_per_day = models.IntegerField(
        default=0,
        null=True,
        blank=True,
        help_text="3.82m3"
    )
    polythene_per_roll = models.IntegerField(
        default=0,
        null=True,
        blank=True,
    )
    cement_per_bag = models.IntegerField(
        default=0,
        null=True,
        blank=True,
    )
    sharp_sand_per_m3 = models.IntegerField(
        default=0,
        null=True,
        blank=True,
    )
    so_sand_per_m3 = models.IntegerField(
        default=0,
        null=True,
        blank=True,
    )
    granite_per_m3 = models.IntegerField(
        default=0,
        null=True,
        blank=True,
    )
    mixer_poker_operator_per_day = models.IntegerField(
        default=0,
        null=True,
        blank=True,
    )
    HT_bars_per_ton = models.IntegerField(
        default=0,
        null=True,
        blank=True,
    )
    MS_bars_per_ton = models.IntegerField(
        default=0,
        null=True,
        blank=True,
    )
    binding_wire_per_kg = models.IntegerField(
        default=0,
        null=True,
        blank=True,
    )
    BRC_65 = models.IntegerField(
        default=0,
        null=True,
        blank=True,
    )
    A142_per_m2 = models.IntegerField(
        default=0,
        null=True,
        blank=True,
    )
    record_date = models.DateTimeField(
        # default=timezone.now,
        auto_now_add=True,  # I found this is actually better
    )

    # def __str__(self):
    #     return "{user} Entered this on: {record_date}".format(user=self.active_user, record_date=date)


    def __str__(self):
        return "Entered this on: {record_date}".format(record_date=self.record_date)

    # def diesel_per_day(self):
    #     return self.diesel_price_per_liter * 24

    # def petrol_per_day(self):
    #     return self.petrol_price_per_liter * 24
