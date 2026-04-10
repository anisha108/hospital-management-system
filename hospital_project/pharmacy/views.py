from django.shortcuts import render, redirect
from .models import Medicine,Cart
from .forms import MedicineForm

# Show all medicines
def medicine_list(request):
    medicines = Medicine.objects.all()

    cart_items = Cart.objects.all()
    total = 0
    for item in cart_items:
        total += item.medicine.price * item.quantity

    return render(request, 'pharmacy/medicine_list.html', {
        'medicines': medicines,
        'cart_items': cart_items,
        'cart_total': total
    })

# Add medicine
def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm()

    return render(request, 'pharmacy/add_medicine.html', {'form': form})


# Delete medicine (optional but good for exam)
def delete_medicine(request, id):
    med = Medicine.objects.get(id=id)
    med.delete()
    return redirect('medicine_list')


# Add to cart
def add_to_cart(request, id):
    med = Medicine.objects.get(id=id)

    # ❌ Prevent adding if stock is 0
    if med.quantity <= 0:
        return redirect('medicine_list')

    cart_item, created = Cart.objects.get_or_create(medicine=med)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    # ✅ Reduce stock
    med.quantity -= 1
    med.save()

    return redirect('medicine_list')


# View cart
def view_cart(request):
    items = Cart.objects.all()

    total = 0
    for item in items:
        total += item.medicine.price * item.quantity

    tax = total * 0.08
    final_total = total + tax

    return render(request, 'pharmacy/cart.html', {
        'items': items,
        'total': total,
        'tax': tax,
        'final_total': final_total
    })


def checkout(request):
    Cart.objects.all().delete()
    return redirect('medicine_list')