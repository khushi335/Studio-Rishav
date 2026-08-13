from django.db import models
from PIL import Image
import os

# Create your models here.
class PortfolioItem(models.Model):
    ECOSYSTEM_CHOICES = [
        ('photography', 'Photography'),
        ('films', 'Films'),
        ('design', 'Design & Animation'),
        ('dj-events', 'DJ Events'),
    ]
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, help_text="Used for unique project subpages")
    ecosystem = models.CharField(max_length=30, choices=ECOSYSTEM_CHOICES)
    category = models.CharField(max_length=100, help_text="e.g., Weddings, Fashion, Corporate Videos, Club Events")
    image = models.ImageField(upload_to='portfolio/')
    video_url = models.URLField(blank=True, null=True, help_text="YouTube/Vimeo embed URL (Leave blank for photography)")
    is_wide_span = models.BooleanField(default=False, help_text="Spans across 2 columns for asymmetric visual rhythm")
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img_path = self.image.path
            img = Image.open(img_path)
            
            # Auto-optimization sequence using Pillow
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            
            # Scale down massive raw camera files to web-production specs max width 1920px
            max_dimension = 1920
            if img.width > max_dimension or img.height > max_dimension:
                img.thumbnail((max_dimension, max_dimension), Image.Resampling.LANCZOS)
                
            img.save(img_path, "JPEG", quality=82, optimize=True)

    def __str__(self):
        return f"[{self.get_ecosystem_display()}] {self.title}"
        
        
class PhotographyCategory(models.Model):
    title = models.CharField(max_length=100) # e.g., "Automotive Photography"
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

class PhotographyImage(models.Model):
    category = models.ForeignKey(PhotographyCategory, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photography/')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']