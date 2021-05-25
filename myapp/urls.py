from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('brand/',views.brand,name='brand'),
    path('special/',views.special,name='special'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('seller_add_product/',views.seller_add_product,name='seller_add_product'),
    path('seller_index/',views.seller_index,name='seller_index'),
]
