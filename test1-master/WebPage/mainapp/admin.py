from django.contrib import admin

# Register your models here.
from .models import Company_Data,Product,Category
# Create your views here.

@admin.register(Company_Data)
class Data_Admin(admin.ModelAdmin):
    list_display = (
    'company_name',
    'ceo_of_company',
    'year_of_establishment',
    'area',
    'number',
    'email_address',
    'homepage',
    )
    search_fields = ['company_name']

@admin.register(Product)
class product_list(admin.ModelAdmin):
    list_display =(
        'product_name',
        'price',
        'category',
        'post'
    )
    search_fields = ['product_name']


@admin.register(Category)
class category(admin.ModelAdmin):
    category =(
        'name',
    )