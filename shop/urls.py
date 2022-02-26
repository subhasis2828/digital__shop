from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name='home'),
    path('product/',views.product,name='product'),
    path('gallery/',views.gallery,name='gallery'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    
]