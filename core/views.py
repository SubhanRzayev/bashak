from django.views.generic.edit import FormMixin
from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import ListView,CreateView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from .models import About, Career, CareerCsv, Contact,Address, Innovations, Korporativ, KorporativCategory, RehberlikCategory, Sector
from .forms import  CareerCvForm, CareerForm, ContactForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
# from .forms import CareerForm






# def index(request,category_slug=None):
#     category=None
#     categories_sektor = []
    
    
#     categories_list = CategorySektor.objects.all()
    
    
    
#     if category_slug:
#         categories_sektor=CategorySektor.objects.all()
#         category=get_object_or_404(CategorySektor,slug=category_slug)
#         categories_sektor=CategorySektor.objects.filter(name=category)
    

        
#     context = {
#         'categories_sektor':categories_sektor,
#         'categories_list':categories_list,
#     }
        
    
#     return render(request,'index.html',context)


class IndexListView(ListView):
    model = Sector
    template_name = 'index.html'
    context_object = 'sector_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sector_list"] = Sector.objects.all()
        context["innovations_list"] = Innovations.objects.all()
        context["address_list"] = Address.objects.all()[:1]
        
        
        
        
        return context
    

    
    
class SectorDetailView(DetailView):
    model = Sector
    template_name = 'sectors.html'
    success_url = reverse_lazy("core:index")
    




class CareerListView(ListView):
    model = Career
    template_name = 'career.html'
    
    


class CareerDetailView(SuccessMessageMixin,FormMixin,DetailView):
    template_name = 'vacancy-details.html'
    model = Career
    form_class = CareerForm
    success_message = 'Your resume has been accepted and will be returned to you!'
    error_message = 'Invalid form submission.'


    def get_success_url(self):
        return reverse('core:career_detail', kwargs={'slug': self.object.slug})    


       
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about_list"] = About.objects.all()[:1]
        context["forms"] = CareerForm(initial={'career':self.object})
        context["for"] = CareerCvForm(initial={'career':self.object.position})
        
        
        
        return context
        
        
        
        
    
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_valid(self, form):
        form.save()
        return super(CareerDetailView, self).form_valid(form)
    
    def form_invalid(self,form):
        context = super().form_invalid(form)
        return context
    
        
    
    


# def upload_file(request):
#     if request.method == 'POST':
#         form = CareerForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('core:contact')
#     else:
#         form = CareerForm()
#     return render(request, 'vacancy-details.html', {'form': form})




class InnovationsListView(ListView):
    model = Innovations
    template_name = 'innovations.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["main_news_list"] = Innovations.objects.filter(main_news=True)
        return context
    
    
class InnovationsDetailView(DetailView):
    model = Innovations
    template_name = 'innovations-details.html'
    success_url = reverse_lazy("core:innovations_details")
    
    
    





# Create your views here.

class ContactCreateView(SuccessMessageMixin,CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_message = 'Contact request submitted successfully!'
    error_message = 'Invalid form submission.'
    success_url = reverse_lazy('core:contact')
    
    
    def form_valid(self, form):
    #     message = "{name} / {email} said: ".format(
    #     name=form.cleaned_data.get('name'),
    #     email=form.cleaned_data.get('email'))
    #     message += "\n\n{0}".format(form.cleaned_data.get('message'))
        
        
        
    #     subject = 'Message subject'
    #     send_mail(
    #     subject,
    #     message=message,
    #     from_email='elish777888999@gmail.com',
    #     recipient_list=[settings.EMAIL_HOST_USER],
    #     fail_silently=False
        
    # )
        form.save()
        context =  super().form_valid(form)
        return context
    
    def form_invalid(self,form):
        self.messages.error(self.request,self.error_message)
        context = super().form_invalid(form)
        return context
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["address_list"] = Address.objects.all()[:1]
        return context    

    
    
class KorporativCategoryListView(ListView):
    model = KorporativCategory
    template_name='corporative.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["korporativ_list"] = Korporativ.objects.all()
        context["rehberlikcategory_list"] = RehberlikCategory.objects.all()
        
        
        return context
    
    
 
class KorporativCategoryDetailView(DetailView):
    model = KorporativCategory
    template_name='team.html'
    success_url = reverse_lazy("core:korporative_detail")
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rehberlikcategory"] = RehberlikCategory.objects.all()
        context["rehberlikcategory_list"] = RehberlikCategory.objects.all()
        
        
        return context
    
      
    
