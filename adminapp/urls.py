from django.urls import path
from adminapp import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('add_admin/', views.add_admin, name="add_admin"),
    path('save_admin/', views.save_admin, name="save_admin"),
    path('view_admin/', views.view_admin, name="view_admin"),
    path('display_ad/', views.display_ad, name="display_ad"),
    path('edt_adm/<int:dataid>/', views.edt_adm, name="edt_adm"),
    path('upd_adm/<int:dataid>/', views.upd_adm, name="upd_adm"),
    path('del_adm/<int:dataid>/', views.del_adm, name="del_adm"),
    path('add_categ/', views.add_categ, name="add_categ"),
    path('save_categ/', views.save_categ, name="save_categ"),
    path('view_categ/', views.view_categ, name="view_categ"),
    path('display_categ/', views.display_categ, name="display_categ"),
    path('edit_categ/<int:dataid>/', views.edit_categ, name="edit_categ"),
    path('update_categ/<int:dataid>/', views.update_categ, name="update_categ"),
    path('delete_categ/<int:dataid>/', views.delete_categ, name="delete_categ"),
    path('add_prod/', views.add_prod, name="add_prod"),
    path('save_prod/', views.save_prod, name="save_prod"),
    path('view_prod/', views.view_prod, name="view_prod"),
    path('display_prod/', views.display_prod, name="display_prod"),
    path('edit_prod/<int:dataid>/', views.edit_prod, name="edit_prod"),
    path('update_prod/<int:dataid>/', views.update_prod, name="update_prod"),
    path('delete_prod/<int:dataid>/', views.delete_prod, name="delete_prod"),
    path('show/', views.show, name="show"),
    path('adminloginpage/', views.adminloginpage, name="adminloginpage"),
    path('adminloginsave/', views.adminloginsave, name="adminloginsave"),
    path('adminlogout/',views.adminlogout,name="adminlogout")
]
