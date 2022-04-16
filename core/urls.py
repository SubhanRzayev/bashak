from django.urls import path
from . import views
from core.views import (
    IndexListView,
    SectorDetailView,
    ContactCreateView,
    CareerListView,
    CareerDetailView,
    InnovationsListView,
    InnovationsDetailView,
    KorporativCategoryListView,
    KorporativCategoryDetailView,
    
)

app_name = 'core'

urlpatterns = [
    path("career/", CareerListView.as_view(), name="career"),
    path("career/<slug:slug>/", CareerDetailView.as_view(), name="career_detail"),
    path("innovations/", InnovationsListView.as_view(), name="innovations"),
    path("innovations/<slug:slug>/", InnovationsDetailView.as_view(), name="innovations_details"),
    # path("", views.index,name='index'),
    path("", IndexListView.as_view(), name="index"),
    path("corporative/", KorporativCategoryListView.as_view(), name="korporative"),
    
    path("sector/<slug:slug>/", SectorDetailView.as_view(), name="sector_detail"),
    path("corporative/team/<slug:slug>/", KorporativCategoryDetailView.as_view(), name="korporative_detail"),
    
    
    
    path("contact/", ContactCreateView.as_view(), name="contact"),
    
    
]
