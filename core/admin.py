from django.contrib import admin
from django.utils.html import format_html

from core.models import (
    About, 
    Address, 
    Career,
    CareerCsv, 
    CategoryDesign,
    Contact, Innovations, 
    Korporativ, KorporativCategory,  
    RehberlikCategory, 
    Sector,
)

# Register your models here.

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ['position',]
    
    

@admin.register(Innovations)
class InnovationsAdmin(admin.ModelAdmin):
    list_display = ['title','description','image_tag','created_at','updated_at','is_published','main_news',]
    list_filter = ['title','description','created_at','updated_at','is_published',]
    search_fields = ('title',)


# @admin.register(CategorySektor)
# class CategorySektorAdmin(admin.ModelAdmin):
#     list_display = ['name','image_tag','slug',]
    

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ['count','title','description','image_tag',]
    
@admin.register(CategoryDesign)
class CategoryDesignAdmin(admin.ModelAdmin):
    list_display = ['title','description','image_tag',]
    
    
@admin.register(Korporativ)
class KorporativAdmin(admin.ModelAdmin):
    list_display = ['description',]


# @admin.register(KorporativCategory)
# class KorporativCategoryAdmin(admin.ModelAdmin):
#     list_display = ['category']

admin.site.register(KorporativCategory)


@admin.register(CareerCsv)
class CareerCsvAdmin(admin.ModelAdmin):
    list_display = ['career','full_name','email','cv',]
    list_filter = ['career__position','full_name','email','cv',]
    search_fields = ['career__position','full_name','email','cv',]
    



    
    
@admin.register(RehberlikCategory)
class RehberlikCategoryAdmin(admin.ModelAdmin):
    list_display = ['position','korporativcategory','full_name','facebook_link','linkedin_link','image_tag',]

    




    





@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['address','phone_number1','phone_number2','phone_number3']
    list_filter = ['address',]
    search_fields = ('address',)
    
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','phone','email','message',]
    list_filter = ['name',]
    search_fields = ('name',)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['haqqımızda',]