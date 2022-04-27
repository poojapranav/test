from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import product,orders,customer
from .forms import customerform,orderform
# Create your views here.
def home(request):
    o=orders.objects.all()
    c=customer.objects.all()
    total_customers=c.count()
    total_orders=o.count()
    delivered=o.filter(status='delivered').count()
    pending=o.filter(status='pending').count()
    return render(request,'cop/dashboard.html',{'o':o,'c':c,'t':total_orders,'d':delivered,'p':pending})
def customer1(request,pk):
    c=customer.objects.get(id=pk)
    o=c.orders_set.all()
    return render(request,'cop/customer.html',{'o':o,'c':c})
def product1(request):
    p=product.objects.all()
    return render(request,'cop/product.html',{'p':p})
def createcustomer(request):
    form=customerform()
    if request.method=='POST':
        form=customerform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'cop/createcustomerform.html',{'form':form})
def createorders(request):
    form=orderform()
    if request.method=='POST':
        form=orderform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ho')
    return render(request,'cop/createorderform.html',{'form':form})
def updateorder(request,pk):
    o=orders.objects.get(id=pk)
    form=orderform(instance=o)
    if request.method=='POST':
        form=orderform(request.POST,instance=o)
        if form.is_valid():
            form.save()
            return redirect('ho')
    return render(request,'cop/createorderform.html',{'form':form})
def deleteorder(request,pk):
    o=orders.objects.get(id=pk)
    if request.method=='POST':
        o.delete()
        return redirect('ho')
    return render(request,'cop/delete.html',{'item':o})
