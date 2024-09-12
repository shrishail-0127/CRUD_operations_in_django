from django.urls import path
from . import views


urlpatterns = [

    path('',views.item_list, name='item-list' ),
    path('item/create/',views.item_create, name='item-create'),
    path('item/<int:pk>/',views.item_detail, name='item-detail'),
    path('item/<int:pk>/update/',views.item_update, name='item-update'),
    path('item/<int:pk>/delete/',views.item_delete, name='item-delete'),
]