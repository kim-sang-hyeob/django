from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Company_Data, Product


def mainpage(request):
    return render(request,'mainpage.html')


def company_list(request):
    company_list_all = Company_Data.objects.all()
    context={'company_list_all':company_list_all}
    return render(request ,'company_list.html' , context)

# 여기서 막힘.
def company_detail(request,id):
    company_id = Company_Data.objects.get(id=id)
    product = Product.objects.all()
    context ={'company_id':company_id ,'product':product}
    return render(request, 'company_product.html', context) 


def product_list(request):
    pass 