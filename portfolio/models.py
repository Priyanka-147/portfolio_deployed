from django.db import models

# ---------- Navbar ----------
class NavbarLink(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    icon = models.ImageField(upload_to='navbar/', blank=True, null=True)

    def __str__(self):
        return self.name


# ---------- Hero Section ----------
class Hero(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='hero/', blank=True, null=True)
    hire_me_link = models.CharField(max_length=200, blank=True, null=True)
    contact_me_link = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


# ---------- About Section ----------
class About(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class SocialLink(models.Model):
    platform = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    icon = models.ImageField(upload_to='social/', blank=True, null=True)

    def __str__(self):
        return self.platform


# ---------- Project Section ----------
class Project(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, help_text="Project title")
    description = models.TextField(blank=True, null=True, help_text="Detailed project description")
    image = models.ImageField(
        upload_to='projects/', 
        blank=True, 
        null=True,
        help_text="Project screenshot or thumbnail"
    )
    
    # Skills fields
    skills1 = models.CharField(
        max_length=200, 
        blank=True, 
        null=True,
        verbose_name="Frontend Skills",
        help_text="Frontend skills (comma-separated, e.g., HTML, CSS, React)"
    )
    skills2 = models.CharField(
        max_length=200, 
        blank=True, 
        null=True,
        verbose_name="Backend Skills",
        help_text="Backend skills (comma-separated, e.g., Python, Django, Node.js)"
    ) 
    skills3 = models.CharField(
        max_length=200, 
        blank=True, 
        null=True,
        verbose_name="Database Skills",
        help_text="Database and infrastructure skills (comma-separated, e.g., PostgreSQL, MongoDB)"
    ) 
    skills4 = models.CharField(
        max_length=200, 
        blank=True, 
        null=True,
        verbose_name="Other Skills",
        help_text="Other relevant skills (comma-separated)"
    ) 
    
    # Project Links
    code_link = models.URLField(
        max_length=200, 
        blank=True, 
        null=True,
        verbose_name="Code Repository",
        help_text="Link to GitHub/GitLab repository"
    )
    demo_link = models.URLField(
        max_length=200, 
        blank=True, 
        null=True,
        verbose_name="Live Demo",
        help_text="Link to live project demo"
    )

    def __str__(self):
        return self.title


# ---------- Skills Section ----------
class SkillCategory(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    icon = models.ImageField(upload_to='skills/', blank=True, null=True)
    
    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name="skills")
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.category.name})"


# ---------- Contact Section ----------
class ContactInfo(models.Model):
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.email


class Message(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"


# ---------- Footer ----------
class FooterLink(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
    url = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name