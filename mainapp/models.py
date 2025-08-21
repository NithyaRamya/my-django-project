# app/models.py
from django.db import models
from django import forms

class HomeBanner(models.Model):
    title = models.CharField(max_length=200)
    house_image = models.ImageField(upload_to='house_images/')
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    description1 = models.TextField(max_length=100,blank=True, null=True)
    description2 = models.TextField(max_length=100,blank=True, null=True)
    description3 = models.TextField(max_length=500,blank=True, null=True)
    background_image = models.ImageField(upload_to='banner_images/')
    house_image = models.ImageField(upload_to='house_images/')
    description4 = models.TextField(max_length=500,blank=True, null=True)

    def __str__(self):
        return self.title

class WhyChooseUsItem(models.Model):
    title = models.CharField(max_length=100)    
    icon = models.ImageField(upload_to='why_choose_us/')
    
    class Meta:
        verbose_name = "Why Choose Us Item"
        verbose_name_plural = "Why Choose Us Items"

    def __str__(self):
        return self.title
    
class BannerBg(models.Model):
    background_image = models.ImageField(upload_to='banner_bg/', blank=True, null=True)

    def __str__(self):
        if self.background_image:
            return str(self.background_image.name)
        return "No background image"

class WhyChooseUsFeature(models.Model):
    icon = models.ImageField(upload_to='why_choose_us/icons/')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class MiddleSectionImage(models.Model):
    image = models.ImageField(upload_to='why_choose_us/middle/')
    alt_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.alt_text if self.alt_text else "Middle Section Image"

# models.py
class Service(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services/')
    
    def __str__(self):
        return self.title

class ClientReview(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='client_reviews/')
    review_text = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)  # e.g., 4.5
    background_image = models.ImageField(upload_to='review/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Footer(models.Model):
    logo = models.ImageField(upload_to="footer/")
    title = models.CharField(max_length=100)
    description = models.TextField()

    # Social Media Links
    instagram_image = models.ImageField(upload_to='instagram_images/', blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    youtube_image = models.ImageField(upload_to='youtube_images/', blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)

    facebook_image = models.ImageField(upload_to='facebook_images/', blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class FooterCategory(models.Model):
    footer = models.ForeignKey(Footer, on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)

def __str__(self):
        return f"{self.name} ({self.footer.title})"
    
class FooterContact(models.Model):
    footer = models.ForeignKey(Footer, on_delete=models.CASCADE, related_name="contacts")
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Contact for {self.footer.title}"
    
    
class AboutBanner(models.Model) :
   title = models.CharField(max_length=200, default="About Us")
   about_image = models.ImageField(upload_to='about_images/')
   
   def __str__(self):
        return self.title
    
class AboutSection(models.Model):
    title = models.CharField(max_length=100, default="About Us")
    highlight = models.CharField(max_length=100, default="Nagercoil Builders")
    description = models.TextField()
    image1 = models.ImageField(upload_to="about/")
    image2 = models.ImageField(upload_to="about/")
    image3 = models.ImageField(upload_to="about/")

    def __str__(self):
        return self.title
    
class ServiceBanner(models.Model):
    title = models.CharField(max_length=200,blank=True, null=True)
    title1 = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
     return self.title or "Untitled Service Banner"


class ServiceBannerImage(models.Model):
    banner = models.ForeignKey(ServiceBanner, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="service_images/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    servicesection_image = models.ImageField(upload_to='services/', blank=True, null=True)

    def __str__(self):
        banner_title = self.banner.title if self.banner else "No Banner"
        return f"{banner_title} - {self.description or 'Image'}"

    
class ServiceSection(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    
class ProjectBanner(models.Model) :
   title = models.CharField(max_length=200)
   project_image = models.ImageField(upload_to='project_images/')
   
   def __str__(self):
        return self.title
    
class ProjectSection(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/')
    
    
    def __str__(self):
        return self.title


class Banner(models.Model):
    # First Banner (Carousel + heading + description above images)
    first_banner_heading = models.CharField(max_length=255, blank=True, null=True)
    first_banner_description = models.TextField(blank=True, null=True)

    # Second Banner (Carousel + text + optional image side by side)
    second_banner_heading = models.CharField(max_length=255, blank=True, null=True)
    second_banner_description = models.TextField(blank=True, null=True)
    second_banner_image = models.ImageField(upload_to="banners/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"

    def __str__(self):
        return f"Banner #{self.id} - {self.first_banner_heading or 'No Heading'}"


class SecondBannerSlide(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="second_banner/")
    order = models.PositiveIntegerField(default=0, help_text="Order of display in the carousel")
    is_active = models.BooleanField(default=True)
    second_image = models.ImageField(upload_to="second_banner/", blank=True, null=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title

class FirstBannerSlide(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="first_banner/")
    order = models.PositiveIntegerField(default=0, help_text="Order of display in the carousel")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
    
class ThirdBannerSlide(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="third_banner/")
    order = models.PositiveIntegerField(default=0, help_text="Order of display in the carousel")
    is_active = models.BooleanField(default=True)
    second_image = models.ImageField(upload_to="third_banner/", blank=True, null=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
    
    
class ContactBanner(models.Model) :
   title = models.CharField(max_length=200)
   contact_image = models.ImageField(upload_to='contact_images/')
   
   def __str__(self):
        return self.title
    
class ContactSection(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    highlight = models.CharField(max_length=100, blank=True, null=True)  # <--- check this
    def __str__(self):
        return self.title


class Package(models.Model):
    PACKAGE_CHOICES = [
        ("basic", "Basic"),
        ("standard", "Standard"),
        ("premium", "Premium"),
    ]
    name = models.CharField(max_length=50, choices=PACKAGE_CHOICES, unique=True)
    price_per_sqft = models.PositiveIntegerField()

    def __str__(self):
        return self.get_name_display()


class PackageDetail(models.Model):
    CATEGORY_CHOICES = [
        ("construction", "Constructions"),
        ("electrical", "Electrical Work"),
        ("plumbing", "Plumbing & Painting"),
        ("extra", "Extra Work"),
    ]
    package = models.ForeignKey("Package", related_name="details", on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.package.name} - {self.get_category_display()}"
    



class Enquiry(models.Model):
    
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=100)
    details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
   
    

    def __str__(self):
        return f"{self.name} - {self.service}"
    
class EnquiryTitle(models.Model):
        title = models.CharField(max_length=200,blank=True, null=True,default="Enquiry")
        title1= models.CharField(max_length=200,blank=True, null=True,)
        enquiry_image = models.ImageField(upload_to='enquiry_images/',blank=True, null=True)
        description = models.TextField(max_length=200,blank=True, null=True)
        title2= models.CharField(max_length=200,blank=True, null=True,)
        def __str__(self):
         return self.title
    
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    description = models.TextField(max_length=200,blank=True, null=True)
    title = models.CharField(max_length=200,blank=True, null=True,default="FAQ")
    title1 = models.CharField(max_length=200,blank=True, null=True)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=1)  # to control display order

    class Meta:
        ordering = ['order']  # order FAQs by this field

    def __str__(self):
        return self.question

