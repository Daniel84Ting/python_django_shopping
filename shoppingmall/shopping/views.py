from shopping.models import Shopping
from shopping.forms import ShoppingForm
from django.shortcuts import redirect, render

# Create your views here.
def views_index(request):
    form = ShoppingForm()

    if request.method == 'POST':
        form = ShoppingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shopping_index')
    
    #Shopping.find() (from node js)
    shopping = Shopping.objects.all()

    return render(request, 'shopping/index.html', {"form": form})
