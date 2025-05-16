from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    about_description = models.TextField()
    profile_image = models.ImageField(upload_to='profile/')
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('SOFTWARE ', 'Software '),
        ('TOOLS ', ' Tool'),
        ('MAINTENANCE', 'Maintenance')
    ]

    name = models.CharField(max_length=100)
    percentage = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    icon = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.role} at {self.company}"

class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    date_obtained = models.DateField()
    certificate_image = models.ImageField(upload_to='certifications/')
    credential_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('LINKEDIN', 'LinkedIn'),
        ('GITHUB', 'GitHub'),
        ('TWITTER', 'Twitter'),
        ('INSTAGRAM', 'Instagram'),
        ('FACEBOOK', 'Facebook')
    ]

    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.platform

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"