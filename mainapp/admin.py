from django.contrib import admin
from .models import (
    HomeBanner, WhyChooseUsItem, BannerBg, WhyChooseUsFeature, MiddleSectionImage, Service,
    ClientReview, Footer, FooterCategory, FooterContact, AboutBanner, AboutSection,
    ServiceBanner, ServiceSection, ServiceBannerImage, Banner, SecondBannerSlide, FirstBannerSlide,
    ProjectBanner, ProjectSection, ThirdBannerSlide, ContactBanner, ContactSection, Enquiry,
    Package, PackageDetail, FAQ, EnquiryTitle
)

# ---------------- Home & Section Models ----------------
@admin.register(HomeBanner)
class HomeBannerAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(WhyChooseUsItem)
class WhyChooseUsItemAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(BannerBg)
class BannerBgAdmin(admin.ModelAdmin):
    list_display = ('background_image',)

@admin.register(WhyChooseUsFeature)
class WhyChooseUsFeatureAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(MiddleSectionImage)
class MiddleSectionImageAdmin(admin.ModelAdmin):
    list_display = ('alt_text',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(ClientReview)
class ClientReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating')

@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(FooterCategory)
class FooterCategoryAdmin(admin.ModelAdmin):
    list_display = ('footer', 'name', 'url')

@admin.register(FooterContact)
class FooterContactAdmin(admin.ModelAdmin):
    list_display = ('footer', 'phone', 'email', 'website')

@admin.register(AboutBanner)
class AboutBannerAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)

# ---------------- Service Models ----------------
class ServiceBannerImageInline(admin.TabularInline):
    model = ServiceBannerImage
    extra = 1

@admin.register(ServiceBanner)
class ServiceBannerAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [ServiceBannerImageInline]

@admin.register(ServiceSection)
class ServiceSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)

# ---------------- Project Models ----------------
@admin.register(ProjectBanner)
class ProjectBannerAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(ProjectSection)
class ProjectSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(ThirdBannerSlide)
class ThirdBannerSlideAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")

@admin.register(SecondBannerSlide)
class SecondBannerSlideAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")

@admin.register(FirstBannerSlide)
class FirstBannerSlideAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("id", "first_banner_heading", "second_banner_heading", "created_at")
    search_fields = ("first_banner_heading", "second_banner_heading")

# ---------------- Contact Models ----------------
@admin.register(ContactBanner)
class ContactBannerAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(ContactSection)
class ContactSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "service", "created_at")
    search_fields = ("name", "email", "phone", "service")
    list_filter = ("service", "created_at")

# ---------------- FAQ ----------------
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'order')
    list_editable = ('order',)

@admin.register(EnquiryTitle)
class EnquiryTitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'title1', 'title2')

# ---------------- Package Models ----------------
class PackageDetailInline(admin.TabularInline):
    model = PackageDetail
    extra = 1
    fields = ('category', 'description')  # include icon

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_sqft')
    list_filter = ('name',)
    search_fields = ('name',)
    inlines = [PackageDetailInline]

from django.utils.html import format_html

@admin.register(PackageDetail)
class PackageDetailAdmin(admin.ModelAdmin):
    list_display = ('package', 'category', 'description')
    list_filter = ('package', 'category')
    search_fields = ('package__name', 'category', 'description')

    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<img src="{}" style="height:50px;"/>', obj.icon.url)
        return "-"
    icon_preview.short_description = 'Icon'

