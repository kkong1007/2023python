from django import forms

op_code = [
    ('출고', False),
    ('입고', True),
]


class NewItemForm(forms.Form):
    name = forms.CharField(max_length=100)
    weight = forms.FloatField()
    minimum_weight = forms.FloatField()
    category_id = forms.IntegerField()
    stocked_date = forms.DateField(input_formats=['%Y-%m-%dT%H:%M'])


class NewStockForm(forms.Form):
    op_code = forms.BooleanField()
    weight = forms.FloatField()
    stock_date = forms.DateField(input_formats=['%Y-%m-%dT%H:%M'])
