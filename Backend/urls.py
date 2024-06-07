from django.urls import path
from Backend import views


urlpatterns = [
    path('view_indexPage/',views.view_indexPage,name="view_indexPage"),
    path('Category_Page/',views.Category_Page,name="Category_Page"),
    path('Save_Categories_Data/',views.Save_Categories_Data,name="Save_Categories_Data"),
    path('Display_CategoryTable/',views.Display_CategoryTable,name="Display_CategoryTable"),
    path('Edit_Category/<int:c_id>',views.Edit_Category,name="Edit_Category"),
    path('Save_Updations/<int:c_id>',views.Save_Updations,name="Save_Updations"),
    path('Delete_Data/<int:c_id>',views.Delete_Data,name="Delete_Data"),
    path('view_loginPage/',views.view_loginPage,name="view_loginPage"),
    path('Do_AdminLogin/',views.Do_AdminLogin,name="Do_AdminLogin"),
    path('Admin_logout/',views.Admin_logout,name="Admin_logout"),
    path('Add_Products/',views.Add_Products,name="Add_Products"),
    path('Save_ProductData/',views.Save_ProductData,name="Save_ProductData"),
    path('Show_Products/',views.Show_Products,name="Show_Products"),
    path('EditPage_Products/<int:p_id>',views.EditPage_Products,name="EditPage_Products"),
    path('Save_ProductUpdations/<int:p_id>',views.Save_ProductUpdations,name="Save_ProductUpdations"),
    path('Delete_Product/<int:p_id>',views.Delete_Product,name="Delete_Product"),



    path('Customer_support/',views.Customer_support,name="Customer_support"),
    path('delete_queries/<int:c_id>',views.delete_queries,name="delete_queries"),
]