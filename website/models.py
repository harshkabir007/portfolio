from django.db import models


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("AI", "AI & Machine Learning"),
        ("CV", "Computer Vision"),
        ("WEB", "Web Development"),
        ("EMB", "Embedded Systems"),
        ("ROB", "Robotics"),
        ("TOOLS", "Tools"),
    ]

    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)

    short_description = models.TextField()
    description = models.TextField()

    image = models.ImageField(upload_to="projects")

    github = models.URLField(blank=True)
    demo = models.URLField(blank=True)

    technologies = models.CharField(
        max_length=300,
        help_text="Comma separated"
    )

    featured = models.BooleanField(default=False)

    order = models.PositiveIntegerField(default=0)

    created = models.DateField(auto_now_add=True)

    def tech_list(self):
        return [t.strip() for t in self.technologies.split(",")]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Achievement(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    year = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.company


class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    image = models.ImageField(upload_to="certificates")

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="gallery")

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name