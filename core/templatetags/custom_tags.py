from atexit import register
from django.template import Library

from core.models import KorporativCategory, Sector
# from core.models import CategorySektor

register = Library()


@register.simple_tag
def header_category():
    return Sector.objects.all()

@register.simple_tag
def header_categories():
    

    b = KorporativCategory.objects.order_by('-title').filter(category__isnull=True)
    context = {
        "korporativcategory":b
    }
            
    return context
