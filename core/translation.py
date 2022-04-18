from modeltranslation.translator import translator, TranslationOptions
from .models import About, Address, Career, CategoryDesign, Innovations, Korporativ,KorporativCategory, RehberlikCategory, Sector


class KorporativTranslationOptions(TranslationOptions):
    fields = ('description',)
    
translator.register(Korporativ,KorporativTranslationOptions)


class KorporativCategoryTranslationOptions(TranslationOptions):
    fields = ('title','content',)
    
translator.register(KorporativCategory,KorporativCategoryTranslationOptions)


class RehberlikCategoryTranslationOptions(TranslationOptions):
    fields = ('position','full_name',)
    
translator.register(RehberlikCategory,RehberlikCategoryTranslationOptions)

class AddressTranslationOptions(TranslationOptions):
    fields = ('address',)
    
translator.register(Address,AddressTranslationOptions)


class CareerTranslationOptions(TranslationOptions):
    fields = ('position','requirements','obligations','working_conditions',)
    
translator.register(Career,CareerTranslationOptions)


class AboutTranslationOptions(TranslationOptions):
    fields = ('haqqımızda',)
    
translator.register(About,AboutTranslationOptions)



class InnovationsTranslationOptions(TranslationOptions):
    fields = ('title','description','content',)
    
translator.register(Innovations,InnovationsTranslationOptions)


class SectorTranslationOptions(TranslationOptions):
    fields = ('title','description','general',)
    
translator.register(Sector,SectorTranslationOptions)


class CategoryDesignTranslationOptions(TranslationOptions):
    fields = ('title','description',)
    
translator.register(CategoryDesign,CategoryDesignTranslationOptions)









