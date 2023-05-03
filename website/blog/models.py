from django.db import models
from django.utils import timezone  
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.
class Service_Category(models.Model) : 
    name = models.CharField(verbose_name= "نام" , max_length=200 , null= True , blank= True )
    slug = models.SlugField(verbose_name = "آدرس خدمت "  , max_length = 200 , null = True , unique= True  )
    description = RichTextField(verbose_name = "توضیحات در مورد خدمت " , null = True , blank = True )
    picture = models.FileField(verbose_name="عکس خدمت" , upload_to="Services/" , null = True , blank = True ) 
    status = models.BooleanField(verbose_name="منتشر شود " , default= False  )


    def __str__(self) : 
        return self.name 


    class Meta : 
        db_table = 'Service'
        verbose_name_plural = "خدمات"


    def get_absolute_url(self):
        return reverse("blog:detail_services", args = [self.slug , str(self.id) ] )
    





class Category_Person(models.Model): 
    name = models.CharField(verbose_name = "نام دسته بندی سازمانی " , max_length= 200 , unique= True )
    
    
    def __str__(self) : 
        return self.name 
    
    class Meta : 
        db_table = "Category_Person"
        
        verbose_name_plural = "دسته بندی سمت اعضا "
    
    





class Members(models.Model) : 
    level = models.ForeignKey('Category_Person' ,on_delete=models.CASCADE  ,  null = True , blank = True , verbose_name="سمت فرد " )
    EDUCATION_LEVEL = ( ('d','دیپلم')  ,  ('b' , 'لیسانس') ,  ('m' , 'فوق لیسانس') ,  ('p' , 'دکترا') )
    firstname = models.CharField(verbose_name = "نام"  , max_length = 200 ) 
    lastname  = models.CharField(verbose_name = "نام خانوادگی"  , max_length = 200 )

    birthday  = models.DateTimeField(verbose_name = "تاریخ تولد ")
    phone_number = models.IntegerField("شماره تلفن"  ) 
    code_melli = models.IntegerField('کد ملی ' ,  ) 
    picture = models.FileField(verbose_name = "عکس" , upload_to = "Image_person/" , null = True , blank = True )
    education_level = models.CharField('تحصیلات  ' , max_length = 1 , choices = EDUCATION_LEVEL )
    def __str__(self) : 
        return f'{self.firstname}  {self.lastname}' 
    
    class Meta :  
        db_table = 'Members'
        verbose_name_plural = 'اعضا'

    


    linkedin = models.CharField(verbose_name = "آدرس لینک دین " , max_length = 200 , unique = True , blank = True , null = True )
    instagram = models.CharField(verbose_name = "آدرس اینستاگرام " , max_length = 200 , unique = True , blank = True , null = True )
    discription_of_member = models.CharField(max_length = 200  , blank = True , null = True , verbose_name = 'متن درباره فرد '  )






class Contact(models.Model) : 
	full_name = models.CharField(verbose_name = 'نام و نام خانوادگی '  , max_length = 400 )
	title = models.CharField('عنوان' , max_length = 200 )
	email = models.EmailField(verbose_name = 'ایمیل' )
	message = RichTextField(verbose_name = 'پیام' , blank = True , null = True ) 
	file = models.FileField(verbose_name = 'فایل'  , upload_to = 'Cantact_with_me' )

	def __str__(self) : 
		return self.title   


	class Meta : 
		db_table = 'Contact'
		verbose_name_plural = 'ارتباط با ما '



class Posts(models.Model) : 
	STATUS = (
		('p' , 'منتشر شود ') , 
		('d'  , 'پیش نویس باقی بماند ')
		)
	title = models.CharField('عنوان' , max_length = 200 )
	category = models.ForeignKey('Service_Category' , verbose_name = 'دسته بندی ' , on_delete = models.CASCADE , blank = True , null = True )
	slug  = models.SlugField('آدرس  '  , max_length = 200 , unique = True  )
	picture = models.FileField('عکس سر تیتر ' , upload_to = "Article_picture" , blank = True , null = True )
	discription = RichTextField(blank = True , null = True , verbose_name = 'متن مقاله '  )
	author = models.ForeignKey('Members'  , verbose_name = 'نویسنده'  , on_delete = models.CASCADE , null = True , blank = True )
	created = models.DateTimeField('زمان انتشار ' , default = timezone.now )

	updated = models.DateTimeField(auto_now_add = True  ) 
	status  = models.CharField('وضعیت' , choices = STATUS  , default ='d' , max_length = 1  ) 
	class Meta : 
		db_table = 'Posts'
		verbose_name_plural  = 'محتوا سایت '


	def __str__(self) : 
		return self.title 


	def get_absolute_url(self) :
		return  reverse('blog:detail_post' , args = [self.slug , str(self.id)  ])


	self_idea = RichTextField(blank = True , null = True , verbose_name = ' نظرات طراح در مورد طرح  '  )
	picture1  = models.FileField('1عکس سر تیتر ' , upload_to = "Article_picture/" , blank = True , null = True )
	picture2  = models.FileField('2عکس سر تیتر ' , upload_to = "Article_picture/" , blank = True , null = True )
	picture3  = models.FileField('3عکس سر تیتر ' , upload_to = "Article_picture/" , blank = True , null = True )



class Testimonial(models.Model):
    person = models.ForeignKey('Members' , verbose_name="فرد مورد نظر " , on_delete=models.CASCADE )
    rate   = models.IntegerField(verbose_name="امتیاز" , null = True , blank = True ) 
    
    message = RichTextField(verbose_name = "متن پیام" , blank = True , null = True )
    
    
    class Meta : 
        db_table = "Testimonial"
        verbose_name_plural = "رضایت نامه ها"
        
        
        
        
class Blogs(models.Model) : 
    
    STATUS_CHOICES = (
		('d', 'پیش نویس') , 
		('p' , 'منتشر شود ')
	)
    head_picture = models.FileField(verbose_name="عکس مقاله یا نظریات "  , upload_to="Articles_Blogs" , null = True , blank = True )
    title = models.CharField(verbose_name="عنوان مقاله "  , max_length= 200 )
    slug  = models.SlugField(verbose_name="آدرس مقاله "   , max_length= 200 , unique= True ) 
    
    author = models.ForeignKey('Members' , verbose_name="نویسنده" , on_delete=models.CASCADE , null = True , blank = True )
    message =  RichTextField(verbose_name = "متن پیام" , blank = True , null = True )
    time_created = models.DateField(verbose_name="زمان ساخته شدن " , default=timezone.now )
    
    status = models.CharField(verbose_name="وضعیت" , max_length=1 , choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now_add = True   , null = True , blank = True ) 
    tags = models.ManyToManyField('Category_for_Blogs' , null = True , blank = True )
    class Meta : 
        db_table = "Blogs"
        verbose_name_plural = "مقالات و محتوا ساخته شده افراد "
        
        
    def get_absolute_url(self):
    		return reverse("blog:detail_blogs", args= [self.slug , str(self.id) ])
	
 
 
class Category_for_Blogs(models.Model) : 
    name = models.CharField(verbose_name= "نام دسته بندی "  , unique= True , max_length= 200  ) 
    slug = models.SlugField(verbose_name="آدرس دسته بندی ها "  , max_length= 200 , unique= True , null = True , blank = True )
    
    
    def __str__(self) : 
        return self.name 
    
    class Meta : 
        db_table = "Category_for_Blogs"
        
        verbose_name_plural = " دسته بندی های مقالات و محتوا ساخته شده "
    
    
class Work_in_Building(models.Model) : 
    title = models.CharField(verbose_name="نام عنوان " , max_length= 200 )
    description = models.CharField(verbose_name="توضیحات" , max_length= 200 )
    picture = models.FileField(verbose_name="عکس عنوان" , upload_to="Work_in_Building" )
    status = models.BooleanField(default=False , verbose_name="نمایش داده شود ")
    
    
    def __str__(self) : 
        return self.title 
    
    class Meta : 
        db_table = "Work_in_Building"
        verbose_name_plural = "کار های صورت گرفته برای تمایش صفحه اول سایت"