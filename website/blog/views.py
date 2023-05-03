from django.shortcuts import render , get_object_or_404 
from django.http import HttpResponse 
from .models import Posts , Members , Testimonial , Blogs , Category_for_Blogs   , Work_in_Building , Service_Category 
# Create your views here.

def home(request):
    obj = Posts.objects.all() 
    test = Testimonial.objects.all()
    article = Blogs.objects.filter(status = "p" )
    works = Work_in_Building.objects.filter(status = True )
    services = Service_Category.objects.filter(status = True )
    context = {'obj' : obj , 'test' : test , 'article' : article  , 'works' : works , 'services':services } 
    return render(request , 'construction/index.html' , context  )






def about(request) :
    obj = Members.objects.all()
    test = Testimonial.objects.all()
    context = {'obj' : obj , 'test' : test } 
    context = {'member':obj , "test":test}

    return render(request , 'construction/about.html' , context   )





def projects(request) : 
    obj = Posts.objects.all()
    context = {'obj' : obj }
    return render(request , 'construction/projects.html' , context )


def contact(request) : 
    return render(request , 'construction/contact.html' , {})




def introduce_projects(request) : 
    obj = Posts.objects.all()
    context = {'obj' : obj }
    return render(request , 'construction/our_project_section.html' , context )


def detail_post(request , slug , id  ) : 
    post = get_object_or_404(Posts , slug =slug  ,  id = id  ) 
    context = {'post':post }

    return render(request , 'construction/project-details.html'  , context )


def detail_blogs(request , slug , id  ) : 
    blog = get_object_or_404(Blogs , slug =slug  ,  id = id  ) 
    article = Blogs.objects.filter(status = "p" )
    category =  Category_for_Blogs.objects.all()
    context = {'blogs':blog , 'article' : article  , 'category' : category   }

    return render(request , 'construction/blog-details.html'  , context )



def weblogs(request) : 
    article = Blogs.objects.filter(status = "p" )
    context = {'article' : article }
    return render(request , 'construction/blog.html' , context )
    



def detail_services(request  , slug , id ) : 
    service = get_object_or_404(Service_Category , slug = slug , id = id )
    context = {'service':service} 
    return render(request , 'construction/service-details.html' , context )
    
    
def service(request) : 
    obj = Service_Category.objects.filter(status = True )
    context = {'obj':obj}
    return render(request , 'construction/services.html' , context )