from django.shortcuts import render,HttpResponse
from .models import Order
# Create your views here.
def page_main(request):
    obj_lst = Order.objects.all()
    return render(request, './index.html', { 'obj_lst': obj_lst })

def page_secret(request):
    return render(request, './index2.html')