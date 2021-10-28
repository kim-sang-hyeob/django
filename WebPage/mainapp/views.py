from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from .models import Company_Data, Product ,Category


def mainpage(request):
    return render(request,'mainpage.html')


def company_list(request):
    company_list_all = Company_Data.objects.all()
    category = Category.objects.all()
    context={'company_list_all':company_list_all, 'category':category}
    return render(request ,'company_list.html' , context)


def company_detail(request,id):
    company_id = Company_Data.objects.get(id=id)
    product = Product.objects.all()
    context ={'company_id':company_id ,'product':product , }
    return render(request, 'company_product.html', context)


# 이부분이 제일 마음에 안듬
def checkbox(request):
    '''want=[]
    want_id=Category.objects.all()
    for i in want_id: 
        want.append(str(i))'''
    # want에 전체 카테고리의 이름이 리스트에 저장되어 있음. 

    product=Product.objects.all()
    if request.method == 'POST':
        c_id=[]
        product_name=[]
        checkbox_data=request.POST.getlist('checks[]') # 선택한체크박스의 id 가 들어있음
        for c in checkbox_data:
            c=c.split('.')
            product_name.append(c[0])
            c_id.append(int(c[1]))

        context = {'checkbox_data':checkbox_data , 'product':product ,'product_name':product_name ,'c_id':c_id }
        return render(request,'checkbox_data.html' , context)
    else:
        return redirect('/')