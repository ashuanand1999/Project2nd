from django.shortcuts import render
from .models import CustomerData
from .forms import CreationForm,UpdationForm,DeletionForm
from django.http import HttpResponse


def home_view(request):
    return render(request,'CURDhome.html')

def creation_view(request):
    if request.method == "POST":
        cform = CreationForm(request.POST)
        if cform.is_valid():
            cus_id = request.POST.get('customer_id', '')
            cus_name = request.POST.get('customer_name', '')
            cus_mobile = request.POST.get('customer_mobile', '')
            cus_email = request.POST.get('customer_email', '')
            pro_id = request.POST.get('product_id', '')
            pro_name = request.POST.get('product_name', '')
            pro_cost = request.POST.get('product_cost', '')
            num_prod = request.POST.get('Number_of_products', '')
            data = CustomerData(
                customer_id=cus_id,
                customer_name=cus_name,
                customer_mobile=cus_mobile,
                customer_email=cus_email,
                product_id=pro_id,
                product_name=pro_name,
                product_cost=pro_cost,
                Number_of_products=num_prod,
            )
            data.save()
            cform = CreationForm()
            return render(request,'Creatingform.html',{'cform': cform})
        else:
            return HttpResponse('<h1>Please give the data to all fields</h1>')
    else:
        cform = CreationForm()
        return render(request,'Creatingform.html',{'cform': cform})

def updating_view(request):
    if request.method == "POST":
        uform = UpdationForm(request.POST)
        if uform.is_valid():
            pid = request.POST.get('product_id')
            pcost = request.POST.get('product_cost')
            prod = CustomerData.objects.filter(product_id=pid)
            if not prod:
                return HttpResponse("<h1>Product does not exists</h1>")
            else:
                prod.update(product_cost=pcost)
                uform = UpdationForm()
                return render(request,'Updatingform.html',{'uform': uform})
        else:
            return HttpResponse('<h1>Please give the data to all fields</h1>')
    else:
        uform = UpdationForm()
        return render(request,'Updatingform.html',{'uform': uform})

def retrieving_view(request):
    rform = CustomerData.objects.all()
    return render(request,'Retrievingform.html',{'rdata': rform})

def deletion_view(request):
    if request.method == "POST":
        dform = DeletionForm(request.POST)
        if dform.is_valid():
            pid = request.POST.get('product_id')
            prod = CustomerData.objects.filter(product_id=pid)
            if not prod:
                return HttpResponse('<h1>Prduct does not exists</h1>')
            else:
                prod.delete()
                dform = DeletionForm()
                return render(request,'Deletingform.html',{'dform': dform})
        else:
            dform = DeletionForm()
            return render(request,'Deletingform.html',{'dform': dform})
    else:
        dform = DeletionForm()
        return render(request,'Deletingform.html',{'dform': dform})







