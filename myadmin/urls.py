from django.urls import path,include
from . import views
urlpatterns=[
    path('login/',views.Login,name='Login'),
    path('logout',views.Logout,name="logout_admin"),
    path('',views.index,name='admin_dashboard'),
    path('products/',views.getProduct,name="admin_product"),

    path('myprofile/',views.adminProfile,name="admin_myprofile"),
    path('product-form/',views.addProduct),
    # path('product-save/',views.addProduct),
    # path('product-delete/<int:pk>/',views.addProduct),

    # path('category-form/',views.addProduct),
    # path('category-save/',views.addProduct),
]