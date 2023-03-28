from django import forms
from .models import Ticket


class NewTicketForm(forms.ModelForm):
    ticket_number = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Ticket Number", "class": "form-control"}), label="")
    contact_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Contact Name", "class": "form-control"}), label="")
    contact_email = forms.CharField(required=True, widget=forms.widgets.EmailInput(attrs={"placeholder": "Contact Email", "class": "form-control"}), label="")
    description = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Description", "class": "form-control"}), label="")
    notes = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"placeholder": "Notes", "class": "form-control"}), label="")

    class Meta:
        model = Ticket
        fields = ("ticket_number", "contact_name", "contact_email", "description", "notes")
