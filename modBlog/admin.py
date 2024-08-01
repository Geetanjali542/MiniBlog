from django.contrib import admin
from modBlog.models import Blog# Register your models here.


 #it Employee displays the table created whereas Emp_display will display the fields on the outer side of the Employee table
class Blog_display(admin.ModelAdmin):
  list_display = ['name', 'tag', 'created_at']
admin.site.register(Blog, Blog_display)