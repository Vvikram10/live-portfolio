from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    category = models.CharField(max_length=50)
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class Certificate(models.Model):
    CATEGORY_CHOICES = [
        ('PROGRAMMING', 'Programming'),
        ('WEB_DEV', 'Web Development'),
        ('DATA_SCIENCE', 'Data Science'),
        ('CLOUD', 'Cloud Computing'),
        ('OTHER', 'Other'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='certificates/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    issuer = models.CharField(max_length=100)
    issuer_logo = models.URLField()
    credential_url = models.URLField()
    date = models.DateField()
    duration = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title