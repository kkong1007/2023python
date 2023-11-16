from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Item, Category, ItemStoredHistory
from .forms import NewItemFrom


def main(request):
    find_item_list = Item.objects.all()
    return render(request, 'main.html', context={
        'item_list': find_item_list
    })


def detail(request, id):
    histories = ItemStoredHistory.objects.filter(item_id=id).order_by("-id")

    date_list = [
        {
            "id": history.id,
            "weight": history.weight,
            "created_at": history.created_at,
        }
        for history in histories
    ]

    response_data = {
        "histories": date_list
    }

    return JsonResponse(response_data)


def create(request):
    if request.method == 'GET':
        new_form = NewItemFrom()
        return render(request, 'create.html', context={
            'form': new_form
        })
    elif request.method == 'POST':
        form = NewItemFrom(request.POST)

        if form.is_valid():
            Item.objects.create(name=form.cleaned_data.get('name'), weight=form.cleaned_data.get('weight'),
                                category_id=form.cleaned_data.get('category_id'),
                                stocked_date=form.cleaned_data.get('stocked_date'))
            return redirect(to="item:list")
