from datetime import datetime

from django import forms

from main.models import Category

op_code = [
    ('출고', False),
    ('입고', True),
]


class NewItemForm(forms.Form):
    name = forms.CharField(max_length=100, label='상품명', widget=forms.TextInput(attrs={
        'placeholder': '상품명을 입력해주세요',
        'class': 'form-control',
        'autofocus': 'autofocus'
    }))
    weight = forms.FloatField(label='재고(KG)', widget=forms.NumberInput(attrs={
        'placeholder': '재고(KG)를 입력해주세요',
        'class': 'form-control'
    }))
    minimum_weight = forms.FloatField(label='최소 유지 재고(KG)', widget=forms.NumberInput(attrs={
        'placeholder': '최슈 유지 재고(KG) 입력해주세요',
        'class': 'form-control'
    }))
    category_id = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='카테고리',
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    stocked_date = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        label='최초 입고 날짜',
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        initial=datetime.now()
    )


class NewStockForm(forms.Form):
    op_code = forms.BooleanField()
    weight = forms.FloatField()
    stock_date = forms.DateField(input_formats=['%Y-%m-%dT%H:%M'])
