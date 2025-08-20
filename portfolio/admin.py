from django.contrib import admin
from django.utils.html import format_html
from .models import (
    NavbarLink, Hero, About, SocialLink,
    Project, SkillCategory, Skill,
    ContactInfo, Message, FooterLink
)
from .forms import (
    ProjectForm, SkillCategoryForm, SkillForm,
    NavbarLinkForm, SocialLinkForm
)

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    form = SkillForm

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    form = SkillCategoryForm
    list_display = ("name", "display_icon", "skill_count")
    search_fields = ("name",)
    inlines = [SkillInline]

    def display_icon(self, obj):
        if obj.icon:
            return format_html('<img src="{}" width="30" height="30" />', obj.icon.url)
        return "-"
    display_icon.short_description = "Icon"

    def skill_count(self, obj):
        return obj.skills.count()
    skill_count.short_description = "Number of Skills"

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    form = SkillForm
    list_display = ("name", "category")
    list_filter = ("category",)
    search_fields = ("name",)
    autocomplete_fields = ["category"]

@admin.register(NavbarLink)
class NavbarLinkAdmin(admin.ModelAdmin):
    form = NavbarLinkForm
    list_display = ("name", "url", "display_icon")
    search_fields = ("name", "url")
    
    def display_icon(self, obj):
        if obj.icon:
            return format_html('<img src="{}" width="30" height="30" />', obj.icon.url)
        return "-"
    display_icon.short_description = "Icon"

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ("name", "subtitle", "display_image")
    search_fields = ("name", "subtitle", "description")
    fieldsets = (
        ("Basic Info", {
            "fields": ("name", "subtitle", "description")
        }),
        ("Image", {
            "fields": ("image",)
        }),
        ("Links", {
            "fields": ("hire_me_link", "contact_me_link")
        })
    )

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "-"
    display_image.short_description = "Hero Image"

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title", "display_image", "content_preview")
    search_fields = ("title", "content")
    
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "-"
    display_image.short_description = "Image"

    def content_preview(self, obj):
        return obj.content[:100] + "..." if obj.content else ""
    content_preview.short_description = "Content Preview"

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    form = SocialLinkForm
    list_display = ("platform", "url", "display_icon")
    search_fields = ("platform", "url")
    
    def display_icon(self, obj):
        if obj.icon:
            return format_html('<img src="{}" width="30" height="30" />', obj.icon.url)
        return "-"
    display_icon.short_description = "Icon"

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    list_display = ("title", "display_image", "skills_preview", "has_links")
    search_fields = ("title", "description", "skills1", "skills2", "skills3", "skills4")
    list_filter = ("skills1", "skills2", "skills3", "skills4")
    fieldsets = (
        ("Basic Info", {
            "fields": ("title", "description", "image")
        }),
        ("Skills", {
            "fields": ("skills1", "skills2", "skills3", "skills4"),
            "classes": ("collapse",)
        }),
        ("Links", {
            "fields": ("code_link", "demo_link")
        })
    )

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "-"
    display_image.short_description = "Image"

    def skills_preview(self, obj):
        skills = []
        for field in ['skills1', 'skills2', 'skills3', 'skills4']:
            if getattr(obj, field):
                skills.extend(getattr(obj, field).split(',')[:2])
        return ", ".join(skills[:3]) + ("..." if len(skills) > 3 else "")
    skills_preview.short_description = "Skills"

    def has_links(self, obj):
        return bool(obj.code_link or obj.demo_link)
    has_links.boolean = True
    has_links.short_description = "Has Links"

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ("email", "phone", "location")
    search_fields = ("email", "phone", "location")

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message_preview", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "email", "message")
    readonly_fields = ("created_at",)
    
    def message_preview(self, obj):
        return obj.message[:100] + "..." if obj.message and len(obj.message) > 100 else obj.message
    message_preview.short_description = "Message"

@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ("name", "url")
    search_fields = ("name", "url")