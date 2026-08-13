from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name="index"),
    path("about/",about,name="about"),
    path("services/",services,name="services"),
    path('services/photography/', photography_packages, name='photography_packages'),
    path('services/videography/', videography_packages, name='videography_packages'),
    path('services/editing-retouching/', editing_packages, name='editing_packages'),
    path('services/graphic-design/', design_packages, name='design_packages'),
    path('services/animation/', animation_packages, name='animation_packages'),
    path('services/social-media/', social_content_packages, name='social_content_packages'),
    path('services/dj-entertainment/', dj_packages, name='dj_packages'),
    path('services/custom-quote/', custom_quote, name='custom_quote'),
    path("portfolio/",portfolio,name="portfolio"),
    path("photography/",photography,name="photography"),
    path("contact/",contact,name="contact"),
    path('blog/',blog_list, name='blog_list'),
]