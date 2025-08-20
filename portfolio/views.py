from django.shortcuts import render
from django.contrib import messages
from .models import (
    Hero, About, Project, SkillCategory, 
    ContactInfo, SocialLink, NavbarLink, 
    FooterLink, Message
)

# Home page (contains all sections: hero, about, projects, skills, contact)
def portfolio(request):
    if request.method == "POST":
        # Handle contact form submission
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        if all([name, email, message]):
            Message.objects.create(
                name=name,
                email=email,
                message=message
            )
            messages.success(request, "Message sent successfully!")
        else:
            messages.error(request, "Please fill in all fields.")

    # Get all sections data
    hero = Hero.objects.first()
    about = About.objects.first()
    projects = Project.objects.all()
    # Process skills for each project
    for project in projects:
        project.skills_list = []
        for field in ['skills1', 'skills2', 'skills3', 'skills4']:
            if getattr(project, field):
                project.skills_list.extend([skill.strip() for skill in getattr(project, field).split(',')])
    
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    contact = ContactInfo.objects.first()
    social_links = SocialLink.objects.all()
    navbar_links = NavbarLink.objects.all()
    footer_links = FooterLink.objects.all()

    # Prepare context data for template
    context = {
        "hero": hero,
        "about": about,
        "projects": projects,
        "skill_categories": skill_categories,
        "contact": contact,
        "social_links": social_links,
        "navbar_links": navbar_links,
        "footer_links": footer_links,
    }
    
    return render(request, "portfolio/project4.html", context)


# Contact Page
def contact(request):
    contact = ContactInfo.objects.first()
    social_links = SocialLink.objects.all()
    navbar_links = NavbarLink.objects.all()
    footer_links = FooterLink.objects.all()

    return render(request, "portfolio/contact.html", {
        "contact": contact,
        "social_links": social_links,
        "navbar_links": navbar_links,
        "footer_links": footer_links,
    })


# Blog Page (assuming you’ll add Blog model later)
def blogs(request):
    navbar_links = NavbarLink.objects.all()
    footer_links = FooterLink.objects.all()
    return render(request, "portfolio/blog.html", {
        "navbar_links": navbar_links,
        "footer_links": footer_links,
    })

 
