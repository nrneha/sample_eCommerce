from django.urls import path
from WebApp import views


urlpatterns = [
    path('',views.Homepage,name="home"),
    path('About/',views.AboutPage,name="About"),
    path('Contact/',views.ContactPage,name="Contact"),
    path('Products/',views.Show_Products,name="Products"),
    path('Support/',views.Save_CustomerMessages,name="Support"),
    path('FilterProduct/<ctg>',views.Show_FilterdProucts,name="FilterProduct"),
    path('Single_Products/<int:p_id>',views.Single_Products,name="Single_Products"),
    path('user_registration/',views.user_registration,name="user_registration"),
    path('Save_UserAccount/',views.Save_UserAccount,name="Save_UserAccount"),
    path('UserLogin/',views.UserLogin,name="UserLogin"),
    path('UserLogout/',views.UserLogout,name="UserLogout"),
    path('Save_Cart/',views.Save_Cart,name="Save_Cart"),
    path('View_Cart/',views.View_Cart,name="View_Cart"),
    path('Remove_CartedItem/<int:p_id>',views.Remove_CartedItem,name="Remove_CartedItem"),
    path('user_loginpage/',views.user_loginpage,name="user_loginpage"),
    path('checkout_page/',views.checkout_page,name="checkout_page"),
    path('payment_page/',views.payment_page,name="payment_page"),
]