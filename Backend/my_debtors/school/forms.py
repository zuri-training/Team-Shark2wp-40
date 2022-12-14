from django import forms

from .models import *



class SchoolAdminForm(forms.ModelForm):
    class Meta:
        model  = SchoolAdmin
        fields = [
            'name',
            'school',
            'school_address',
            'phone_no',
            'email'
        ]
class DebtorForm(forms.ModelForm):
    class Meta:
        model  = Debtor
        fields = [
            'debtor_name',
            'ward_name',
            'school',
            'debtor_class',
            'amount_indebted',
            'phone_no',
            'email',
            'debtor_image'
        ]

class MessageForm(forms.ModelForm):
    class Meta:
        model  = Message
        fields = [
            'name',
            'email',
            'message',
            'document'
        ]