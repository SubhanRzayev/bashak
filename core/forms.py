from turtle import position
from django import forms
from .models import Career, CareerCsv, Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'phone',
            'message',
        )
        
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'name-surname'
                }),
            
            
            'email': forms.EmailInput(attrs={
                'class':'email1'
                
                }),
            
            'phone':forms.TextInput(attrs={
                'class':'phone'
                
                }),

            
            
            'message': forms.Textarea(attrs={
                'class': 'textarea'
            })
        }
        
        
        



class CareerCvForm(forms.ModelForm):

    class Meta:
        model = CareerCsv
        fields = [
            'career',
           
        ]
        
        widgets = {
            
            'career':forms.TextInput(attrs={
                        'class':'vakant',
                        'placeholder': 'VAKANT YER',
                        'empty_label':"VAKANT YER",
                    }),
        }
        


class CareerForm(forms.ModelForm):
    
    
    
    
    class Meta:
        model = CareerCsv
        fields = [
            'career',
            'full_name',
            'email',
            'cv',
        ]
        
        

        
        
    
        widgets = {
            
            'career':forms.HiddenInput(attrs={
                        'class':'vakant',
                        'placeholder': 'VAKANT YER',
                    }),
            
            'full_name':forms.TextInput(attrs={
                        'class':'vakant',
                        'placeholder': 'Ad,Soyad, Ata adı',
                        
                        
                    }),
            
            'email':forms.EmailInput(attrs={
                        'class':'vakant',
                        'placeholder': 'E-mail'
                    }),
        }

            
            

        
        
    
    
        
