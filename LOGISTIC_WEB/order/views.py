from django.shortcuts import render
from order.forms import Order_form,Receiving_location_form,Destination_location_form,Vehicle_form,Cargo_form,Bill_form

def Form_view(request):
    if request.method=='POST':
        a = Order_form(data=request.POST)
        b = Receiving_location_form(data=request.POST)
        c = Destination_location_form(data=request.POST)
        d = Vehicle_form(data=request.POST)
        e = Cargo_form(data=request.POST)
        f = Bill_form(data=request.POST)

        if a.is_valid() and b.is_valid() and c.is_valid() and d.is_valid() and e.is_valid() and f.is_valid():
            order = a.save()
            b=b.save(commit=False)
            b.order = order
            c=c.save(commit=False)
            c.order = order
            d=d.save(commit=False)
            d.order = order
            e=e.save(commit=False)
            e.order = order
            f=f.save(commit=False)
            f.order = order

            b.save()
            c.save()
            d.save()
            e.save()
            f.save()
        else:
            print("form not valid if error") 
    else:
        a = Order_form()
        b = Receiving_location_form()
        c = Destination_location_form()
        d = Vehicle_form()
        e = Cargo_form()
        f = Bill_form()
    
    return render(request,'order/form.html',{'Order_form':a,'Receiving_location_form':b,'Destination_location_form':c,'Vehicle_form':d,'Cargo_form':e,'Bill_form':f})