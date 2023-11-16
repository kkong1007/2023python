from django import forms


class NewItemFrom(forms.Form):
    name = forms.CharField(max_length=100)
    weight = forms.FloatField()
    category_id = forms.IntegerField()
    stocked_date = forms.DateField()
