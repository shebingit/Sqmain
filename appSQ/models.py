from django.db import models

#admin

class Services(models.Model):
    service_name=models.CharField(max_length=60)
    service_content=models.TextField()
    service_img=models.ImageField(upload_to="services", null=True)

class Colleges(models.Model):
    college_names=models.CharField(max_length=100)

class ClientsCompany(models.Model):
    clientcomp_name=models.CharField(max_length=80)
    Work_status=models.CharField(max_length=20)
    comp_logo=models.ImageField(upload_to="client", null=True)

class ProductCompany(models.Model):
    pro_comp_name=models.CharField(max_length=80)
    pro_comp_logo=models.ImageField(upload_to="productcompany", null=True)

class Products(models.Model):
    product_name=models.CharField(max_length=60)
    product_company=models.CharField(max_length=60)
    product_price=models.CharField(max_length=20)
    product_details=models.TextField()
    product_img=models.ImageField(upload_to="product", null=True)

class Works(models.Model):
    w_category=models.CharField(max_length=60)
    w_status=models.CharField(max_length=20)
    w_details=models.TextField()
    w_img=models.ImageField(upload_to="works", null=True)

class Category(models.Model):
    work_category=models.CharField(max_length=80)


class Gallery(models.Model):
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    category_name=models.CharField(max_length=80)
    image_url=models.ImageField(upload_to="gallery", null=True)

class Cart(models.Model):
    products_id=models.ForeignKey(Products,on_delete=models.CASCADE,null=True,blank=True)
    prodt_unit=models.CharField(max_length=20)
    product_amount=models.CharField(max_length=20)
    status=models.CharField(max_length=20)
    
