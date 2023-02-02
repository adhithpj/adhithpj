from django.urls import path
from electroapp import views

urlpatterns = [
    path('home_pg/', views.home_pg, name="home_pg"),
    path('about_pg/', views.about_pg, name="about_pg"),
    path('about_d/<int:dataid>', views.about_d, name="about_d"),
    path('contact_pg/', views.contact_pg, name="contact_pg"),
    path('products_pg/', views.products_pg, name="products_pg"),
    path('dispCateg/<itemCateg>', views.dispCateg, name="dispCateg"),
    path('displayProd/<int:dataid>/', views.displayProd, name="displayProd"),
    path('login/',views.login,name='login'),
    path('loginsave/',views.loginsave,name='loginsave'),
    path('Customer_login/', views.Customer_login, name='Customer_login'),
    path('logout/', views.llogout, name='logout')

]