from datetime import date
from django import forms
from django.forms import ModelForm, DateInput, TimeInput, TextInput, IntegerField
from django.core.exceptions import ValidationError
from .models import ServiceOffer
from offer_requests.models import OfferRequests


class ServiceOfferForm(ModelForm):
    class Meta:
        model = ServiceOffer
        fields = ["service_title", "service_category", "service_subcategory", "service_name", "service_description",
                  "service_date", "service_start_time", "service_duration", "service_spot", "service_city",
                  "service_district"]
        widgets = {
            "service_date": DateInput(attrs={"type": "date"}),
            "service_start_time": TimeInput(attrs={"type": "time"}),
            "service_duration": TextInput(attrs={"type": "number", "min": "1", "max": "3"})
        }

    def clean_date(self):
        d = self.cleaned_data.get("service_date")
        if d < date.today():
            raise ValidationError("This is a past date.")
        return d


class ServiceOfferEditForm(ModelForm):
    class Meta:
        model = ServiceOffer
        fields = ["service_title", "service_category", "service_subcategory", "service_name", "service_description",
                  "service_date", "service_start_time", "service_duration", "service_spot", "service_city",
                  "service_district"]
        widgets = {
            "service_date": DateInput(attrs={"type": "date"}),
            "service_start_time": TimeInput(attrs={"type": "time"}),
            "service_duration": TextInput(attrs={"type": "number", "min": "1", "max": "3"})
        }

    def clean_date(self):
        d = self.cleaned_data.get("service_date")
        if d < date.today():
            raise ValidationError("This is a past date.")
        return d


class OfferRequestForm(ModelForm):
    class Meta:
        model = OfferRequests
        fields = ['message']
        labels = {
            "message": "Mesaj"
        }
        widgets = {
            "message": forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, "placeholder": "mesajınızı yazın"})
        }


class ServiceOfferFinalForm(ModelForm):
    class Meta:
        model = ServiceOffer
        fields = ['service_new_duration']
        labels = {
            'service_new_duration': "Do you need to update duration:"
        }
        widgets = {
            'service_new_duration': TextInput(attrs={"type": "number", "min": "1", "max": "3"})
        }
