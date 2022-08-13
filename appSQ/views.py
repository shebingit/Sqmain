from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def home(request):
    clients_details_f=ClientsCompany.objects.filter(Work_status='Finished Works')
    clients_details_o=ClientsCompany.objects.filter(Work_status='Ongoing Works')
    return render(request,'index.html',{'clients_details_f':clients_details_f,'clients_details_o':clients_details_o})

def internship(request):
    colleges=Colleges.objects.all()
    return render(request,'internship.html',{'colleges':colleges})

def civilworks(request):
    services=Services.objects.all()
    return render(request,'civilworks.html',{'services':services})

def gallery(request):
    categorys=Category.objects.all()
    gallerylist=Gallery.objects.all()
    return render(request,'gallery.html',{'categorys':categorys,'gallerylist':gallerylist})

def contactus(request):
    return render(request,'contactus.html')

def work_updates(request):
    allworks=Works.objects.filter(w_status='Ongoing Works')
    return render(request,'workupdates.html',{'allworks':allworks})
    

def our_products(request):
    productlist=Products.objects.all()
    return render(request,'our_products.html',{'productlist':productlist})
    

def addtocart(request,prodt_id):
    produt=Products.objects.get(id=prodt_id)
    prodt_status="Pending"
    prodt_unit="1"
    prodt_price=produt.product_price
    cart_item=Cart(products_id=produt,prodt_unit=prodt_unit,product_amount=prodt_price,status=prodt_status)
    cart_item.save()
    cartlist=Cart.objects.all()
    return render(request,'addtocart.html',{'cartlist':cartlist})

def cartview(request):
    cartlist=Cart.objects.all()
    return render(request,'addtocart.html',{'cartlist':cartlist})

def checkout(request):
    return render(request,'checkout.html')

def ButabondSBR_moreinfo(request,productdet_id):
    prodt_details=Products.objects.get(id=productdet_id)
    allprodt=Products.objects.all()
    return render(request,'ButabondSBR_moreinfo.html',{'prodt_details':prodt_details,'allprodt':allprodt})

def construction_chemicals(request):
    procompany=ProductCompany.objects.all()
    return render(request,'chemicals.html',{'procompany':procompany})






#admin 

def dashboard(request):
    allworks=Works.objects.filter(w_status='New Works')
    allworks1=Works.objects.filter(w_status='Ongoing Works')
    return render(request,'Dashboard.html',{'allworks':allworks,'allworks1':allworks1})

def products(request):
    return render(request,'Products.html')

def companies(request):
    procompany=ProductCompany.objects.all()
    return render(request,'company.html',{'procompany':procompany})

def product_company_add(request):
     if request.method=="POST":
        pcomp_name=request.POST['pcname']
        pcomp_img=request.FILES.get('pclogo')

 #saving data

        procomp=ProductCompany(pro_comp_name=pcomp_name,pro_comp_logo=pcomp_img)

        procomp.save()
        message="Successfuly Data Saved"
        procompany=ProductCompany.objects.all()
        return render(request,'company.html',{'procompany':procompany,'message':message})


def our_product(request):
    company_names=ProductCompany.objects.all()
    return render(request,'our_product.html',{'company_names':company_names})

def product_add(request):
    if request.method=="POST":
        pro_name=request.POST['pro_name']
        pro_comp=request.POST['com_name']
        pro_price=request.POST['pro_price']
        pro_detail=request.POST['pro_discr']
        pro_img=request.FILES.get('pro_img')

 #saving data

        pro=Products(product_name=pro_name,product_company=pro_comp,product_price=pro_price,product_details=pro_detail,product_img=pro_img)

        pro.save()
        message="Successfuly Data Saved"
        company_names=ProductCompany.objects.all()
        return render(request,'our_product.html',{'company_names':company_names,'message':message})

def productslist(request):
    productlist=Products.objects.all()
    return render(request,'productlist.html',{'productlist':productlist})

def clients(request):
    clients_details=ClientsCompany.objects.all()
    return render(request,'Clients.html',{'clients_details':clients_details})

def client_add(request):
   if request.method=="POST":
        client_name=request.POST['clientcomp_name']
        status=request.POST['work_stauts']

        if(status=="0"):
            w_status='Ongoing Works'
        else:
             w_status='Finished Works'
        logo=request.FILES.get('comp_logo')

 #saving data

        clients=ClientsCompany(clientcomp_name=client_name,Work_status=w_status,comp_logo=logo)

        clients.save()
        message="Successfuly Data Saved"
        clients_details=ClientsCompany.objects.all()
        return render(request,'Clients.html',{'clients_details':clients_details,'message':message})


def services(request):
    services=Services.objects.all()
    return render(request,'services.html',{'services':services})

def services_add(request):
   if request.method=="POST":
        ser_name=request.POST['service_name']
        ser_content=request.POST['service_content']
        ser_img=request.FILES.get('service_imge')

 #saving data

        services=Services(service_name=ser_name,service_content=ser_content,service_img=ser_img)

        services.save()
        return redirect('services')

def admin_internship(request):
    college=Colleges.objects.all()
    return render(request,'Internships.html',{'college':college})

def college_add(request):
    if request.method=="POST":
        college_name=request.POST['college_name']

 #saving data

        college=Colleges(college_names=college_name)

        college.save()
        return redirect('admin_internship')
    

def admin_gallery(request):
    category=Category.objects.all()
    gallery=Gallery.objects.all()
    return render(request,'workGallery.html',{'category':category,'gallery':gallery})

def category_add(request):
    if request.method=="POST":
        category_name=request.POST['cate_name']

 #saving data

        category=Category(work_category=category_name)

        category.save()
        return redirect('admin_gallery')

def gallery_add(request):
    if request.method=='POST':
        name=request.POST['cate_name']
        images=request.FILES.getlist('work_img')
        catgoryid=Category.objects.get(work_category=name)
       
        for imag in images:
            print(imag)
            galery=Gallery(category_name=name,image_url=imag,category_id=catgoryid)
            galery.save()
        return redirect('admin_gallery')




def new_finised_works(request):
    allworks=Works.objects.all() 
    return render(request,'new_finished.html',{'allworks':allworks,})


def works_add(request):
    if request.method=="POST":
        w_category=request.POST['work_category']
        w_disc=request.POST['work_disc']
        status=request.POST['work_status']

        if(status=="0"):
            wk_status='New Works'
        elif(status=="1"):
             wk_status='Ongoing Works'
        else:
            wk_status="Finished Works"

        w_img=request.FILES.get('work_img')

 #saving data

        work=Works(w_category=w_category,w_status=wk_status,w_details=w_disc,w_img=w_img)

        work.save()
        message="Successfuly Data Saved"
        allworks=Works.objects.all()
        return render(request,'new_finished.html',{'allworks':allworks,'message':message})

def ongoing_works(request):
    allworks=Works.objects.filter(w_status='Ongoing Works')
    return render(request,'ongoingworks.html',{'allworks':allworks})

def workupdate(request,work_id):
    works=Works.objects.get(id=work_id)
    allworks=Works.objects.filter(w_status='Ongoing Works')
    return render(request,'workupdate.html',{'allworks':allworks,'works':works})

def worksave(request,worksave_id):
    if request.method=="POST":
        works=Works.objects.get(id=worksave_id)
        works.w_category=request.POST.get('wd_category')
        works.w_status=request.POST.get('wd_status')
        works.w_details=request.POST.get('wd_details')
        works.w_img=request.FILES.get('wd_img')
        works.save()
    return redirect('ongoing_works')




# All Delete Section 

def workdelete(request,work_deleteid):
    work=Works.objects.get(id=work_deleteid)
    work.delete()
    allworks=Works.objects.all()
    message="Successfuly Deleted"
    return render(request,'ongoingworks.html',{'allworks':allworks,'message':message})

def company_delete(request,pcomd_id):
    company=ProductCompany.objects.get(id=pcomd_id)
    company.delete()
    deletemessage="Successfuly Deleted"
    procompany=ProductCompany.objects.all()
    return render(request,'company.html',{'procompany':procompany,'deletemessage':deletemessage})

def item_delete(request,item_id):
    cartitem=Cart.objects.get(id=item_id)
    cartitem.delete()
    cartlist=Cart.objects.all()
    return render(request,'addtocart.html',{'cartlist':cartlist})

def product_delete(request,prod_id):
    pro=Products.objects.get(id=prod_id)
    pro.delete()
    deletemessage="Successfuly Deleted"
    productlist=Products.objects.all()
    return render(request,'productlist.html',{'productlist':productlist,'deletemessage':deletemessage})

def client_delete(request,client_id):
    clients=ClientsCompany.objects.get(id=client_id)
    clients.delete()
    deletemessage="Successfuly Deleted"
    clients_details=ClientsCompany.objects.all()
    return render(request,'Clients.html',{'clients_details':clients_details,'deletemessage':deletemessage})

def service_delete(request,service_id):
    servicelist=Services.objects.get(id=service_id)
    servicelist.delete()
    deletemessage="Successfuly Deleted"
    services=Services.objects.all()
    return render(request,'services.html',{'services':services,'deletemessage':deletemessage})

def category_delete(request,cate_id):
    categ=Category.objects.get(id=cate_id)
    categ.delete()
    deletemessage="Successfuly Deleted"
    category=Category.objects.all()
    gallery=Gallery.objects.all()
    return render(request,'workGallery.html',{'category':category,'gallery':gallery,'deletemessage':deletemessage})

def college_delete(request,college_id):
    collegelist=Colleges.objects.get(id=college_id)
    collegelist.delete()
    deletemessage="Successfuly Deleted"
    college=Colleges.objects.all()
    return render(request,'Internships.html',{'college':college,'deletemessage':deletemessage})

def gallerylist_delete(request,imgdelete_id):
    imgs=Gallery.objects.get(id=imgdelete_id)
    imgs.delete()
    deletemessage="Successfuly Deleted"
    category=Category.objects.all()
    gallery=Gallery.objects.all()
    return render(request,'workGallery.html',{'category':category,'gallery':gallery,'deletemessage':deletemessage})



