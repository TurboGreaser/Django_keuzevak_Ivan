from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("", include('django.contrib.auth.urls')),
    path('profile', views.profile, name='profile'),
    path("logout_user/", views.logout_user, name="logout_user"),
    path("register/", views.register, name="register"),
    path("openstaande_afhaalacties/", views.openstaande_afhaalacties, name="openstaande_afhaalacties"),
    path('mark_collected/<int:collection_id>/', views.mark_collected, name='mark_collected'),
    path('add_collection/', views.add_collection, name='add_collection'),
    path('all_collections/', views.all_collections, name='all_collections'),
    path('approve_collection/<int:collection_id>/', views.approve_collection, name='approve_collection'),
    path('delete_collection/<int:collection_id>/', views.delete_collection, name='delete_collection'),
    path('list_medicines/', views.list_medicines, name='list_medicines'),
    path('edit_medicine/<int:medicine_id>/', views.edit_medicine, name='edit_medicine'),
    path('delete_medicine/<int:medicine_id>/', views.delete_medicine, name='delete_medicine'),
    path('add_medicine/', views.add_medicine, name='add_medicine'),
]
