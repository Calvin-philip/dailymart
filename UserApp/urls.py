from django.urls import path
from . import views

urlpatterns = [
    path('',views.userindex,name = 'userindex'),
    path('register',views.register,name = 'register'),
    path('userreg',views.userreg,name = 'userreg'),
    path('userlogin',views.userlogin,name = 'userlogin'),
    path('login',views.login,name = 'login'),
    path('logout',views.logout,name = 'logout'),
    path('products',views.products,name = 'products'),
    path('categories',views.categories,name = 'categories'),
    path('contact',views.contact,name = 'contact'),
    path('about',views.about,name = 'about'),
    path('message',views.message,name = 'message'),
    path('cart',views.cart,name = 'cart'),
    path('checkout',views.checkout,name = 'checkout'),
    path('checkoutdata',views.checkoutdata,name = 'checkoutdata'),
    path('profile',views.profile,name = 'profile'),
    path('sucess',views.sucess,name = 'sucess'),
    path('editprofile',views.editprofile,name = 'editprofile'),
    path('singledetails/<int:id>',views.singledetails,name = 'singledetails'),
    path('addtocart/<int:id>',views.addtocart,name = 'addtocart'),
    path('removepro/<int:id>',views.removepro,name = 'removepro'),
    path('viewcatpro/<str:category>',views.viewcatpro,name = 'viewcatpro'),
    path('updateprofile',views.updateprofile,name = 'updateprofile'),



]