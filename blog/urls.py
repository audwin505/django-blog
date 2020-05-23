from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('blog/<int:blog_id>', views.detail, name = "detail"),
    path('blog/new',views.new, name = "new"),
    path('blog/create',views.create, name = "create"),
    path('edit/<int:blog_id>',views.edit, name = "edit"),
    path('update/<int:blog_id>',views.update, name = "update"),
    path('delete/<int:blog_id>',views.delete, name = "delete"),
]
