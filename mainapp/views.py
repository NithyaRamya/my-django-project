from django.shortcuts import render

# Create your views here.
from .models import HomeBanner
from .models import WhyChooseUsItem
from .models import BannerBg
from .models import WhyChooseUsFeature,MiddleSectionImage,Service
from .models import ClientReview, Footer
from decimal import Decimal
from .models import AboutBanner
from .models import AboutSection
from .models import ServiceBanner,ServiceSection
from .models import ProjectBanner,ProjectSection,Banner,SecondBannerSlide,FirstBannerSlide,ThirdBannerSlide
from .models import ContactBanner,ContactSection,FAQ,EnquiryTitle, Package
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    banner = HomeBanner.objects.first()
    why_choose_items = WhyChooseUsItem.objects.all()  
    banner_bg = BannerBg.objects.first() 
    features = WhyChooseUsFeature.objects.all()
    middle_image = MiddleSectionImage.objects.first()  # Get the first uploaded image
    services = Service.objects.all()[:6] 
    reviews = ClientReview.objects.all()
    for r in reviews:
        rating = float(r.rating or 0)
        r.full_stars = int(rating)                       # full stars count
        r.half_star = (rating - r.full_stars) >= 0.5     # True if half star
        r.empty_stars = 5 - r.full_stars - (1 if r.half_star else 0)

    footer = Footer.objects.first()
    context = {
        'banner': banner,
        'banner_bg': banner_bg,
        'why_choose_items': why_choose_items,
        'features': features,
        'middle_image': middle_image,
        'services': services,
        'reviews': reviews,
        "footer": footer,
       
         # for looping stars in template
        
    }
    return render(request, 'home.html', context)

def aboutus(request):
    aboutbanner = AboutBanner.objects.first()
    about_section = AboutSection.objects.first()
    banner = HomeBanner.objects.first()
    footer = Footer.objects.first()
    
    context={
        'banner': banner,
        'aboutbanner': aboutbanner,
        'about_section': about_section,
        'footer': footer,
        
        
    }
    return render(request, 'aboutus.html', context)

def services(request):
    servicebanner = ServiceBanner.objects.prefetch_related("images").first()
    banner = HomeBanner.objects.first()
    footer = Footer.objects.first()
    services = Service.objects.all()[:6] 
    services_section=ServiceSection.objects.all()
    banners = Banner.objects.all().order_by('-created_at')
    first_banner_slides = FirstBannerSlide.objects.filter(is_active=True).order_by("order")    
    second_banner_slides = SecondBannerSlide.objects.filter(is_active=True).order_by("order")
    third_banner_slides = ThirdBannerSlide.objects.filter(is_active=True).order_by("order")
    context={
        'banner': banner,
        'servicebanner': servicebanner,
        'footer': footer,
        'services': services,
        'services_section':services_section,  
        'banners': banners ,
        "first_banner_slides": first_banner_slides,
        "second_banner_slides": second_banner_slides,
        "third_banner_slides": third_banner_slides,
        
        
        
    }
    return render(request, 'services.html', context)

def projects(request):
    banner = HomeBanner.objects.first()
    footer = Footer.objects.first()
    projectbanner = ProjectBanner.objects.first()
    projects_section=ProjectSection.objects.all()
    context={
        'banner': banner,
        'projectbanner': projectbanner,
        'footer': footer,
        'projects_section':projects_section
            
    }
    return render(request, 'projects.html', context)

def contactus(request):
    contactbanner = ContactBanner.objects.first()
    contact_section = ContactSection.objects.first()
    banner = HomeBanner.objects.first()
    footer = Footer.objects.first()
    packages = Package.objects.prefetch_related("details").all()
    
    context={
        'banner': banner,
        'contactbanner': contactbanner,
        'contact_section': contact_section,
        'footer': footer,
        "packages": packages,
        
    }
    return render(request, 'contactus.html', context)



from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Enquiry

from django.shortcuts import render, redirect


from .models import Enquiry

def enquiry_view(request):
    enquirytitle = EnquiryTitle.objects.first()  # for template display

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        details = request.POST.get('details')

        try:
            # Save to DB
            Enquiry.objects.create(
                name=name,
                email=email,
                phone=phone,
                service=service,
                details=details
            )

            # Send email (for testing use console backend)
            subject = f'New Enquiry from {name}'
            message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nService: {service}\nDetails: {details}"
            recipient_list = ['your_email@gmail.com']
            send_mail(subject, message, email, recipient_list, fail_silently=False)

            messages.success(request, "Your enquiry has been sent successfully!")
        except Exception as e:
            messages.error(request, f"Error: {e}")

        return redirect('enquiry')

    context = {'enquirytitle': enquirytitle}
    return render(request, 'enquiry.html', context)


def faq_view(request):
    faqs = FAQ.objects.all()
    faq_title = FAQ.objects.first()  # single object for page title and heading
    banner = HomeBanner.objects.first()
    footer = Footer.objects.first()
    
    context = {
        'faqs': faqs,
        'faq_title': faq_title,
        'banner': banner,
        'footer': footer,
    }
    return render(request, 'faq.html', context)


