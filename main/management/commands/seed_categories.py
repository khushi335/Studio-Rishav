from django.core.management.base import BaseCommand
from django.utils.text import slugify
from main.models import PhotographyCategory

class Command(BaseCommand):
    help = "Seeds initial 24 photography categories"

    def handle(self, *args, **kwargs):
        categories_list = [
            "Food Photography", "Portraits Photography", "Landscape Photography",
            "Weddings Photography", "Events Photography", "Commercial Photography",
            "Automotive Photography", "Lifestyle Photography", "Actor/Actress Photography",
            "Product Photography", "Anniversary Photography", "Baby Shower Photography",
            "First rice-eating ceremony Photography", "Gunyu Cholo Photography",
            "Birthday Photography", "Club Party Photography", "Gender Reveal Photography",
            "Bridal Makeup Photography", "Graduations Photography", "Upanayana Photography",
            "Film & Posters Photography", "Halloween Photography", "Modeling Photography",
            "New Year, Sydney 2026"
        ]

        for idx, title in enumerate(categories_list, start=1):
            PhotographyCategory.objects.get_or_create(
                title=title,
                defaults={'slug': slugify(title), 'order': idx}
            )

        self.stdout.write(self.style.SUCCESS("All 24 photography categories created successfully!"))