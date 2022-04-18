from distutils.command.upload import upload
from itertools import count
import re
from tkinter import N
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe

from django.urls import reverse
from django.utils import timezone


# Create your models here.



class Korporativ(models.Model):
    description = models.TextField(max_length=3000)
    
    def __str__(self):
        return self.description
    
    
    class Meta:
        verbose_name_plural = 'Korporativ'
        
        


class KorporativCategory(models.Model):
    #relations 
    category=models.ForeignKey('self',db_index=True,blank=True,null=True,related_name='categories',on_delete=models.CASCADE)
    
    
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='media',default='IMG.JPG', blank=True,null=True)
    content = RichTextUploadingField(blank=True, null=True)
    slug = models.CharField(max_length=300, verbose_name='Slug', unique=True, blank=True, null=True)
    
    
    
    def __str__(self):
        if self.category:
            return f"{self.category.title} > {self.title}"
        return self.title 
            
    
    
    def get_absolute_url(self):
        return reverse("core:korporative_detail", kwargs={"slug": self.slug})
    
    
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="100" width="100"/>'.format(self.image.url))
    
    class Meta:
        verbose_name_plural = 'Esas Category'
        
    class Meta:
       ordering = ('id',)
    
    

        
        
    
    
        
        
class RehberlikCategory(models.Model):
    
    korporativcategory = models.ForeignKey('KorporativCategory',on_delete=models.SET_NULL,related_name='team_detail',blank=True,null=True)
    position = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    
    facebook_link  = models.CharField(max_length=120,blank=True,null=True)
    linkedin_link  = models.CharField(max_length=120,blank=True,null=True)
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="100" width="100"/>'.format(self.image.url))
        
    
    def __str__(self):
        return self.full_name
    
    def get_absolute_url(self):
        return reverse("core:korporative_detail", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name_plural = 'Rehberlik Team'
        
        
    
    
    


        
    



    
    
    
    





class Address(models.Model):
    address = models.CharField(max_length=200,default='Bakı şəhəri, Ziya Bünyadov prospekti 3105-ci məhəllə')
    phone_number1 = models.CharField(max_length=200,default='+994 70 252 11 16')
    phone_number2 = models.CharField(max_length=200,default='+994 50 888 18 88')
    phone_number3 = models.CharField(max_length=200,default='+994 12 511 51 57')
    email = models.EmailField(default='info@bashakgroup.az',blank=True)
    
    
    def __str__(self):
        return self.address

    class Meta:
        verbose_name_plural = 'Address'
        
        

class Career(models.Model):
    
    
    position = models.CharField(max_length=200,verbose_name='vəzifə')
    requirements = RichTextUploadingField()
    obligations = RichTextUploadingField()
    working_conditions = RichTextUploadingField()
    slug = models.SlugField(max_length=300, verbose_name='Slug', unique=True, blank=True, null=True,allow_unicode = True,)

    
    def __str__(self):
        return self.position
    
    
    def get_absolute_url(self):
        return reverse("core:career_detail", kwargs={
            "slug": self.slug
        })
    
    
    class Meta:
        verbose_name_plural = 'Karyera'
        
        

    
class CareerCsv(models.Model):
    career = models.ForeignKey('Career',on_delete=models.CASCADE,related_name='careers',blank=True,null=True)
    
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=120)
    
    cv = models.FileField(upload_to='career/cvler/',blank=True,null=True)
    
    
    def __str__(self):
        return str(self.career) 
    
    
    

class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=120)
    phone = models.CharField(max_length=80)
    message = models.TextField(max_length=1000)
    
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Əlaqə'



class About(models.Model):
    haqqımızda = models.TextField(max_length=3000)
    
    def __str__(self):
        return self.haqqımızda
    
    
    
    class Meta:
        verbose_name_plural = 'Haqqımızda'

    
    
class Innovations(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    content = RichTextUploadingField()
    news_image = models.ImageField(upload_to='media')
    slug = models.CharField(max_length=300, verbose_name='Slug', unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    is_published = models.BooleanField(default=False)
    main_news = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = 'Innovations'
    
    
    
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="100" width="100"/>'.format(self.news_image.url))


    def get_absolute_url(self):
        return reverse("core:innovations_details", kwargs={"slug": self.slug})
    

    def __str__(self):
        return self.title
    
    
        
    
  

class Sector(models.Model):
    #relations
    count = models.IntegerField()
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=2000)
    general = RichTextUploadingField()
    slug = models.CharField(max_length=300, verbose_name='Slug', unique=True, blank=True, null=True)
    
    sector_image = models.ImageField(upload_to='media')
    

    
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse("core:sector_detail", kwargs={
            "slug": self.slug
        })
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="100" width="100"/>'.format(self.sector_image.url))
    
    
    
    class Meta:
       ordering = ['count',]



    
    
    
class CategoryDesign(models.Model):
    category_design = models.ForeignKey('Sector',on_delete=models.CASCADE,blank=True,null=True,related_name='categories_design')
    
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=1000)
    
    image = models.ImageField(upload_to='media')
    
    class Meta:
        verbose_name_plural = 'CategoriesDesign'
        
        
    def __str__(self):
        return self.title
    
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="100" width="100"/>'.format(self.image.url))
    



    