from django.contrib import admin
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from django.db import models
from django import forms

# Register your models here.
from home.models import Contact
from product.models import Category, Product, ProductImage

class ImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status')
    list_filter = ('category', 'status')
    inlines = [ImageInline]

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image', 'create_at')

class Admin(models.Model):
    detail = RichTextField()

class AdminForm(forms.ModelForm):
    detail = forms.CharField(widget=CKEditorWidget())

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','status','create_at')
    list_filter = ('status','create_at')



admin.site.site_title = "Summer Project Admin Panel"
admin.site.site_header = "Summer Project Admin Panel"
admin.site.index_title = "Summer Project Admin Panel Home"

admin.site.register(Contact,ContactAdmin)
