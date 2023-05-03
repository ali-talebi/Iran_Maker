from django.contrib import admin
from .models import Service_Category , Contact , Members , Posts , Testimonial , Category_Person  , Blogs  , Category_for_Blogs , Work_in_Building 
# Register your models here.

@admin.register(Service_Category)
class Service_Category_admin(admin.ModelAdmin):
    list_display = ("name" , "slug" , "status")
    search_fields  = ("name" , "slug" )  
    list_editable = ("status" , )
    prepopulated_fields = { 'slug' : ('name' , ) } 



@admin.register(Members)
class Members_admin(admin.ModelAdmin) : 
    list_display = ("firstname" , "lastname" , "birthday" , "phone_number" , "code_melli" , "education_level" , "level") 

    search_fields = ("fisrtname" , "lastname" , "phone_number" , "code_melli" , "level" )
    list_editable = ("level" , )


@admin.register(Contact)
class Contact_admin(admin.ModelAdmin) : 
    list_display = ("full_name" , "title" , "email"  ) 

    search_fields = ("full_name" , "title" , "email"  )


@admin.register(Posts)
class Posts_admin(admin.ModelAdmin) : 
    list_display = ("title" , "category" , "slug"  , "author"  , "created" , "status" ) 
    prepopulated_fields = {'slug':('title' ,)}
    search_fields = ("title" , "category" , "slug" , "author"  )



@admin.register(Testimonial)
class Testimonial_admin(admin.ModelAdmin) : 
    list_display = ("person" , "rate" )
    search_fields = ("person" ,  )
    
    
@admin.register(Category_Person)
class Category_Person_admin(admin.ModelAdmin) : 
    list_display = ("name" , )
    search_fields = ("name" ,  )
    
    
@admin.register(Blogs)
class Blogs_admin(admin.ModelAdmin) : 
    list_display = ("title" , "slug" , "author" , "time_created" , "status" , "get_tags")
    search_fields = ("title" , "slug" , "author" , "status"  )
    list_editable = ("author" , "status" )
    prepopulated_fields = {'slug':('title' , )}
    
    def get_tags(self, obj):
        return " | ".join([p.name for p in obj.tags.all()])
    
    
    
@admin.register(Category_for_Blogs)
class Category_for_Blogs_admin(admin.ModelAdmin) :  
    list_display = ("name" , "slug" ) 
    search_fields = ("name" , ) 
    prepopulated_fields = {'slug' : ('name' , )}



@admin.register(Work_in_Building)
class Work_in_Building_admin(admin.ModelAdmin) :  
    list_display = ("title" , "status" )
    search_fields = ("title" , )
    list_editable = ("status" , )
