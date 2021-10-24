from django.shortcuts import render

# Create your views here.
from .models import Company_Data



def mainpage(request):
    return render(request,'mainpage.html')


def company_list(request):
    company_list_all = Company_Data.objects.all()
    context={'company_list_all':company_list_all}
    return render(request ,'company_list.html' , context)