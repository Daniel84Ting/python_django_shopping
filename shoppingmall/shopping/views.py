from shopping.models import Shopping
from shopping.forms import ShoppingForm
from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.
def views_index(request):
    form = ShoppingForm()

    if request.method == 'POST':
        form = ShoppingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product has been added")
            return redirect('shopping_index')
        else:
            messages.error(request, "Product has not been added")
            return redirect('shopping_index')
    
    #Shopping.find() (from node js)
    shopping = Shopping.objects.all()

    return render(request, 'shopping/index.html', 
    {"form": form, "shopping": shopping})

def views_show(request, pk):
    try:
        shopping = Shopping.objects.get(pk=pk)
    except Shopping.DoesNotExist:
        return redirect('shopping_index')
    form = ShoppingForm(intance=shopping)

    if request.GET.get('action') == 'edit' and request.method == 'POST':
        return render(request, 'shopping/show.html', 
        form = ShoppingForm(request.POST, request.FILES, intance=shopping)

        if form.is_valid():
            form.save()
            return redirect('shopping_show', shopping.id)

    if request.GET.get('action') == 'edit':
        return render(request, 'shopping/show.html', 
        {"form":form, "shopping":shopping, "edit": True})
    
    if request.GET.get('action') == 'del':
        shopping.delete()
        return redirect('shopping_index')

    return render(request, 'shopping/show.html', 
    {"form":form, "shopping":shopping, "edit": False})
