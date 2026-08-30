from django.db import models
from PIL import Image
from django.utils.text import slugify
import os

# Create your models here.
# class PortfolioItem(models.Model):
#     ECOSYSTEM_CHOICES = [
#         ('photography', 'Photography'),
#         ('films', 'Films'),
#         ('design', 'Design & Animation'),
#         ('dj-events', 'DJ Events'),
#     ]
    
#     title = models.CharField(max_length=255)
#     slug = models.SlugField(unique=True, help_text="Used for unique project subpages")
#     ecosystem = models.CharField(max_length=30, choices=ECOSYSTEM_CHOICES)
#     category = models.CharField(max_length=100, help_text="e.g., Weddings, Fashion, Corporate Videos, Club Events")
#     image = models.ImageField(upload_to='portfolio/')
#     video_url = models.URLField(blank=True, null=True, help_text="YouTube/Vimeo embed URL (Leave blank for photography)")
#     is_wide_span = models.BooleanField(default=False, help_text="Spans across 2 columns for asymmetric visual rhythm")
#     created_at = models.DateTimeField(auto_now_add=True)

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         if self.image:
#             img_path = self.image.path
#             img = Image.open(img_path)
            
#             # Auto-optimization sequence using Pillow
#             if img.mode in ("RGBA", "P"):
#                 img = img.convert("RGB")
            
#             # Scale down massive raw camera files to web-production specs max width 1920px
#             max_dimension = 1920
#             if img.width > max_dimension or img.height > max_dimension:
#                 img.thumbnail((max_dimension, max_dimension), Image.Resampling.LANCZOS)
                
#             img.save(img_path, "JPEG", quality=82, optimize=True)

#     def __str__(self):
#         return f"[{self.get_ecosystem_display()}] {self.title}"

class PortfolioItem(models.Model):
    ECOSYSTEM_CHOICES = [
        ('photography', 'Photography'),
        ('films', 'Films'),
        ('design', 'Design & Animation'),
        ('dj-events', 'DJ Events'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, max_length=280, help_text="Auto-generated if left blank.")
    ecosystem = models.CharField(max_length=30, choices=ECOSYSTEM_CHOICES)
    
    # Subcategory allows specific tags for Photography (e.g., Birthday, Gunyo Choli, Pasni, Weddings, Food)
    # For Films / Design / DJ Events, this can be left blank or set to high-level tags.
    subcategory = models.CharField(
        max_length=100, 
        blank=True, 
        help_text="Tag e.g.: Weddings, Birthdays, Gunyo Choli, First Rice, Landscapes, Food"
    )
    
    image = models.ImageField(upload_to='portfolio/')
    video_url = models.URLField(blank=True, null=True, help_text="YouTube/Vimeo embed link for Films or Event highlights.")
    is_wide_span = models.BooleanField(default=False, help_text="Spans across 2 columns in the portfolio grid.")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        # Guarantee unique slug generation
        if not self.slug:
            base_slug = slugify(self.title) or "portfolio-item"
            slug = base_slug
            counter = 1
            while PortfolioItem.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        super().save(*args, **kwargs)

        # Image Optimization Sequence
        if self.image:
            img_path = self.image.path
            try:
                img = Image.open(img_path)
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                
                max_dimension = 1920
                if img.width > max_dimension or img.height > max_dimension:
                    img.thumbnail((max_dimension, max_dimension), Image.Resampling.LANCZOS)
                
                img.save(img_path, "JPEG", quality=82, optimize=True)
            except Exception:
                pass

    def __str__(self):
        sub_info = f" ({self.subcategory})" if self.subcategory else ""
        return f"[{self.get_ecosystem_display()}] {self.title}{sub_info}"
        
        
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