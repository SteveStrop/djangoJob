import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _  # best practice for internationalisation


class JobForm(forms.Form):
    # the fields to display on the form
    # vendor - add extra vendor or update existing
    # extras - update or add depending on how the model stores them (todo check this)
    # appointment
    appointment = forms.SplitDateTimeField(help_text='YYYY-MM-DD')
    #vendor =
    # validate the field. This overrides clean_<fieldname>(self) in forms.Form
    def clean_appointment(self):
        # get the data to be validated
        data = self.cleaned_data['appointment']
        # Check if a date is not in the past.
        if data < datetime.datetime.now():
            raise ValidationError(_('You cannot make an appointment in the past'))
        return data

    floorplan = forms.BooleanField(required=False)
    photos = forms.IntegerField()
    ref = forms.CharField()

    # notes - update or add (see above)
    # history - possible add extra updates here
# -----------SAMPLE FROM LIBRARY---------------------------------
# renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
#
# def clean_renewal_date(self):
#     data = self.cleaned_data['renewal_date']
#
#     # Check if a date is not in the past.
#     if data < datetime.date.today():
#         raise ValidationError(_('Invalid date - renewal in past'))
#
#     # Check if a date is in the allowed range (+4 weeks from today).
#     if data > datetime.date.today() + datetime.timedelta(weeks=4):
#         raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
#
#     # Remember to always return the cleaned data.
#     return data
