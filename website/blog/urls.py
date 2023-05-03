from django.urls import path
from .views import home , about  , projects  , contact  , detail_post  , detail_blogs , weblogs , detail_services , service 

app_name = "blog"
urlpatterns = [
    path('' , home , name ="home" ) ,
    path('about/' , about , name ="about" ) , 
    path("projects/" , projects , name = "projects"  )  , 
    path("contact/" , contact , name ="contact" ) , 
    path('detail_post/<slug:slug>/<int:id>' , detail_post , name = "detail_post" ) , 
    path('detail_blogs/<slug:slug>/<int:id>' , detail_blogs , name = "detail_blogs" ) , 
    path("weblogs/" , weblogs , name = "weblogs" ) , 
    path("detail_services/<slug:slug>/<int:id>" , detail_services  , name = "detail_services" ) , 
    path("service/" , service , name = "service" ) , 
    
   
]
