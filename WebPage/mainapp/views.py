from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Company_Data, Product


def mainpage(request):
    return render(request,'mainpage.html')


def company_list(request):
    company_list_all = Company_Data.objects.all()
    context={'company_list_all':company_list_all}
    return render(request ,'company_list.html' , context)


def company_detail(request,id):
    company_id = Company_Data.objects.get(id=id)
    context ={'company_id':company_id}
    return render(request, 'company_product.html', context) 


'''def products(request,id):
    product_id=get_object_or_404(Product,id=id)
    product=Product.objects.all()
    context = {'product':product, 'product_id':product_id}
    return render(request , 'product.html' , context)

    # 여기서 약간 헷갈림. detail처럼 구현하려고 했는데 어쨰서인지 구현이 잘 안됨.'''

def product_list(request ):
    pass 