from django.shortcuts import render, redirect
from .models import Bill, BillItem
from .forms import BillForm
from decimal import Decimal 

def billing_home(request):
    bills = Bill.objects.all().order_by('-date')
    return render(request, 'billing/home.html', {'bills': bills})


def create_bill(request):
    if request.method == 'POST':
        form = BillForm(request.POST)

        if form.is_valid():
            bill = form.save(commit=False)

            desc_list = request.POST.getlist('desc[]')
            qty_list = request.POST.getlist('qty[]')
            price_list = request.POST.getlist('price[]')

            total = Decimal('0')

            bill.save()  # save first to assign ID

            for desc, qty, price in zip(desc_list, qty_list, price_list):
                qty = int(qty)
                price = Decimal(price)

                item = BillItem.objects.create(
                    bill=bill,
                    description=desc,
                    quantity=qty,
                    price=price
                )

                total += qty * price

            tax = total * Decimal('0.18')
            final = total + tax

            bill.total_amount = total
            bill.tax = tax
            bill.final_amount = final
            bill.save()

            return redirect('view_bill', bill.id)

    else:
        form = BillForm()

    return render(request, 'billing/create_bill.html', {'form': form})



def view_bill(request, id):
    bill = Bill.objects.get(id=id)
    items = bill.items.all()

    return render(request, 'billing/view_bill.html', {
        'bill': bill,
        'items': items
    })