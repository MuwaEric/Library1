from django import forms
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
    
    def clean_renewal_date(self):
        data = self.cleaned_data["renewal_date"]
        
        # checking if date is not in the past
        if data < datetime.date.today():
            raise ValidationError(_("Invalid date-Renewal in the past"))
        
        # checking if date is within the allowed range
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_("Invalid date-Renewal more than 4 weeks ahead"))
        
        return data
    
