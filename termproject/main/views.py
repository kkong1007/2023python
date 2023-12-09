from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Item, Category, ItemStoredHistory
from .forms import NewItemForm, NewStockForm


def main(request):
    find_item_list = Item.objects.all()
    return render(request, 'main.html', context={
        'item_list': find_item_list
    })


def detail(request, pk):
    histories = ItemStoredHistory.objects.filter(item_id=pk).order_by("-id")

    date_list = [
        {
            "id": history.id,
            "weight": history.weight,
            "op_code": history.op_code,
            "created_at": history.created_at,
        }
        for history in histories
    ]

    response_data = {
        "histories": date_list
    }

    return JsonResponse(response_data)


@transaction.atomic()
def create(request):
    if request.method == 'GET':
        new_form = NewItemForm()
        category_list = Category.objects.all()
        return render(request, 'create.html', context={
            'form': new_form,
            'category_list': category_list
        })
    elif request.method == 'POST':
        form = NewItemForm(request.POST)

        if form.is_valid():
            new_item = Item.objects.create(name=form.cleaned_data.get('name'),
                                           weight=form.cleaned_data.get('weight'),
                                           minimum_weight=form.cleaned_data.get('minimum_weight'),
                                           category=form.cleaned_data.get('category_id')
                                           )

            ItemStoredHistory.objects.create(item=new_item,
                                             weight=form.cleaned_data.get('weight'),
                                             created_at=form.cleaned_data.get('stocked_date'),
                                             op_code=True
                                             )

            return redirect(to="item:list")


@transaction.atomic()
@csrf_exempt
def stock(request, pk):
    if request.method == 'POST':
        form = NewStockForm(request.POST)
        if form.is_valid():
            find_item = get_object_or_404(Item, id=pk)

            op_code = form.cleaned_data.get('op_code')
            weight = form.cleaned_data.get('weight')

            if (op_code):
                find_item.weight += weight
            else:
                find_item.weight -= weight

            find_item.save()
            ItemStoredHistory.objects.create(item=find_item,
                                             weight=weight,
                                             op_code=op_code,
                                             created_at=form.cleaned_data.get('stock_date'))
            return JsonResponse(data={
                "message": "성공"
            }, status=200)
        else:
            return JsonResponse(data={
                "message": f"실패: {form.errors}"
            }, status=400)
    else:
        result = {
            'message': 'POST만 가능'
        }
        return JsonResponse(result, status=400)
