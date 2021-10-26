from django.shortcuts import redirect, render

# Create your views here.
from django.db.models import Q
from mainapp.models import Company_Data

def search(request):
    company_list = Company_Data.objects.all()
    search_key = request.GET.get('search_key')

    if search_key :
        c_list=Company_Data.objects.filter(
        Q(company_name=search_key) |
        Q(number=search_key) |
        Q(area=search_key)
    )
        return render(request , 'search.html' , c_list)
    else :
        redirect('mainpage')