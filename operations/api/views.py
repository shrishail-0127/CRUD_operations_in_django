from django.shortcuts import render, redirect
from django.contrib import messages
from operations.forms import ItemForm
from operations.models import Item




def item_list(request):
    items = Item.objects.all()
    return render(request, 'operations/item_list.html', {'items':items})


def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Item created Successfuly")
            return redirect('item-list')
        else:
            messages.error(request, 'Please enter valid details')
            
    else:
        forms = ItemForm()

    return render(request, 'operations/item_create.html', {'forms': forms})



def item_detail(request,pk):
    item = Item.objects.get(pk=pk)
    return render(request, 'operations/item_detail.html', {'item':item})


def item_update(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'item updated successfully')
            return redirect('item-list')

    form = ItemForm(instance=item)
    return render(request, 'operations/item_update.html', {'form':form})
    

def item_delete(request, pk):
    item = Item.objects.get(pk=pk)
    item.delete()
    messages.success(request, 'item deleted successfully')
    return redirect('item-list')