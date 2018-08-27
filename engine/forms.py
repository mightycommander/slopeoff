from __future__ import unicode_literals

from django import forms
from django.forms.formsets import BaseFormSet, formset_factory
from django.forms.widgets import NumberInput


RADIO_CHOICES = (("1", "Radio 1"), ("2", "Radio 2"))

MEDIA_CHOICES = (
    ("Audio", (("vinyl", "Vinyl"), ("cd", "CD"))),
    ("Video", (("vhs", "VHS Tape"), ("dvd", "DVD"))),
    ("unknown", "Unknown"),
)

class RangeInput(NumberInput):
    input_type = 'range'


class ContactBaseFormSet(BaseFormSet):
    def add_fields(self, form, index):
        super(ContactBaseFormSet, self).add_fields(form, index)

    def clean(self):
        super(ContactBaseFormSet, self).clean()
        raise forms.ValidationError(
            "This error was added to show the non form errors styling"
        )



class FilesForm(forms.Form):

    Size = forms.IntegerField(widget=NumberInput(attrs={'type':'range', 'step': '1', 'min': '1', 'max': '5'}))
    Price = forms.IntegerField(widget=NumberInput(attrs={'type':'range', 'step': '1', 'min': '1', 'max': '5'}))
    Ability = forms.IntegerField(widget=NumberInput(attrs={'type':'range', 'step': '1', 'min': '1', 'max': '5'}))

    '''text1 = forms.CharField()

    file1 = forms.FileField()
    file24 = forms.FileField(required=False)
    file3 = forms.FileField(widget=forms.ClearableFileInput)
    file5 = forms.ImageField()
    file4 = forms.FileField(required=False, widget=forms.ClearableFileInput)'''



class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()

    def clean(self):
        cleaned_data = super(ArticleForm, self).clean()
        raise forms.ValidationError(
            "This error was added to show the non field errors styling."
        )
        return cleaned_data
