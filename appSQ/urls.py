from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.home,name='home'),

    path('internship',views.internship,name='internship'),
    path('civilworks',views.civilworks,name='civilworks'),
    path('gallery',views.gallery,name='gallery'),
    path('contactus',views.contactus,name='contactus'),
    path('work_updates',views.work_updates,name='work_updates'),
    path('our_products',views.our_products,name='our_products'),
    path('cartview',views.cartview,name='cartview'),
    path('checkout',views.checkout,name='checkout'),
    path('ButabondSBR_moreinfo/<int:productdet_id>',views.ButabondSBR_moreinfo,name='ButabondSBR_moreinfo'),
    path('construction_chemicals',views.construction_chemicals,name='construction_chemicals'),

   



    # admin dashboard

                path('dashboard',views.dashboard,name='dashboard'),
                path('products',views.products,name='products'),
                path('companies',views.companies,name='companies'),
                path('product_company_add',views.product_company_add,name='product_company_add'),
                path('our_product',views.our_product,name='our_product'),
                path('product_add',views.product_add,name='product_add'),
                path('productslist',views.productslist,name='productslist'),


                path('clients',views.clients,name='clients'),
                path('client_add',views.client_add,name='client_add'),

                path('admin_internship',views.admin_internship,name='admin_internship'),
                path('college_add',views.college_add,name='college_add'),


                path('services',views.services,name='services'),
                path('services_add',views.services_add,name='services_add'),

                path('admin_gallery',views.admin_gallery,name='admin_gallery'),
                path('category_add',views.category_add,name='category_add'),
                path('gallery_add',views.gallery_add,name='gallery_add'),


                path('new_finised_works',views.new_finised_works,name='new_finised_works'),
                path('works_add',views.works_add,name='works_add'),
                path('ongoing_works',views.ongoing_works,name='ongoing_works'),
                path('workupdate/<int:work_id>',views.workupdate,name='workupdate'),
                path('worksave/<int:worksave_id>',views.worksave,name='worksave'),

                # all delete section  

                path('addtocart/<int:prodt_id>',views.addtocart,name='addtocart'),
                path('item_delete/<int:item_id>',views.item_delete,name='item_delete'),

                path('workdelete/<int:work_deleteid>',views.workdelete,name='workdelete'),
                path('company_delete/<int:pcomd_id>',views.company_delete,name='company_delete'),
                path('product_delete/<int:prod_id>',views.product_delete,name='product_delete'),
                path('client_delete/<int:client_id>',views.client_delete,name='client_delete'),
                path('service_delete/<int:service_id>',views.service_delete,name='service_delete'),
                path('category_delete/<int:cate_id>',views.category_delete,name='category_delete'),
                path('college_delete/<int:college_id>',views.college_delete,name='college_delete'),
                 path('gallerylist_delete/<int:imgdelete_id>',views.gallerylist_delete,name='gallerylist_delete'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)