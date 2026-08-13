from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages
from .models import PortfolioItem, PhotographyCategory
from .forms import ContactForm
from django.conf import settings
from decouple import config

# Create your views here.
def index(request):
    return render(request,"main/index.html")

def about(request):
    return render(request,"main/about.html")
    
def services(request):
    return render(request,"main/services.html")
    
def photography(request):
    # Prefetch related images to optimize database queries
    categories = PhotographyCategory.objects.prefetch_related('images').all()
    
    return render(request, 'main/photography.html', {
        'categories': categories
    })
    
def photography_packages(request):
    packages = [
        {
            "id": "portrait-session",
            "name": "Portrait Photoshoot",
            "tagline": "Simple portrait session for individuals, models, and personal branding.",
            "price": "$650",
            "badge": "Popular",
            "features": [
                "2-hour photoshoot session",
                "Up to 2 outfit changes",
                "15 fully retouched photos",
                "Private online download gallery",
            ]
        },
        {
            "id": "editorial-fashion",
            "name": "Fashion & Editorial",
            "tagline": "Professional shoot for clothing brands, magazines, and fashion lookbooks.",
            "price": "$1,200",
            "badge": "Best Value",
            "features": [
                "Half-day shoot (up to 4 hours)",
                "Full outfit and studio setup guidance",
                "35 edited high-resolution photos",
                "Full rights to use photos for printing & ads",
            ]
        },
        {
            "id": "commercial-campaign",
            "name": "Brand Photography",
            "tagline": "Custom photo shoot for company websites, products, and advertising.",
            "price": "$2,200",
            "badge": None,
            "features": [
                "Full-day photoshoot (up to 8 hours)",
                "Multiple models and product setups",
                "All high-resolution files included",
                "Fast 5-day delivery turnaround",
            ]
        }
    ]
    return render(request, 'main/photography_packages.html', {'packages': packages})


def videography_packages(request):
    packages = [
        {
            "id": "brand-film",
            "name": "Brand Video",
            "tagline": "Short promotional video to show off your business or products.",
            "price": "$1,800",
            "badge": "Popular",
            "features": [
                "Full day 4K video shooting",
                "Planning and video script help",
                "Clear audio recording setup",
                "1 main video + 1 short video for social media",
                "Full rights for online and TV ads",
            ]
        },
        {
            "id": "cinema-wedding",
            "name": "Wedding Video",
            "tagline": "Complete wedding day video coverage to capture special moments.",
            "price": "$2,600",
            "badge": "Best Value",
            "features": [
                "Up to 10 hours of video shooting",
                "2 camera operators",
                "Drone video footage (where allowed)",
                "4-6 minute highlight video + full ceremony video",
                "Private 4K online download link",
            ]
        },
        {
            "id": "event-live",
            "name": "Event Video",
            "tagline": "Live recording for stage shows, parties, and corporate events.",
            "price": "$1,450",
            "badge": None,
            "features": [
                "Up to 6 hours event shooting",
                "Direct sound system audio connection",
                "Music highlight clip",
                "48-hour quick video clip for social media",
                "Full event recording file",
            ]
        }
    ]
    return render(request, 'main/videography_packages.html', {'packages': packages})


def editing_packages(request):
    packages = [
        {
            "id": "beauty-retouch",
            "name": "Photo Retouching",
            "tagline": "Fixing skin, colors, and background details in your photos.",
            "price": "$450",
            "badge": "Popular",
            "features": [
                "Blemish removal and smooth skin retouching",
                "Color and lighting adjustments",
                "Background cleaning and object removal",
                "Includes 10 high-quality photos",
            ]
        },
        {
            "id": "cinema-editing",
            "name": "Video Editing",
            "tagline": "Trimming, organizing, and assembling raw video clips into a full video.",
            "price": "$950",
            "badge": "Best Value",
            "features": [
                "Video clip trimming and story setup",
                "Color tuning for a clean look",
                "Background music and voice balance",
                "Adding title text and logos",
                "Exported in high-quality 4K",
            ]
        },
        {
            "id": "full-post-suite",
            "name": "Full Campaign Editing",
            "tagline": "Complete editing service for both photos and videos together.",
            "price": "$1,600",
            "badge": None,
            "features": [
                "Editing for up to 25 photos",
                "1 main video edit + 2 short social media edits",
                "Matching color styles across photos and videos",
                "Fast 5-day delivery time",
            ]
        }
    ]
    return render(request, 'main/editing_packages.html', {'packages': packages})
    
def design_packages(request):
    packages = [
        {
            "id": "logo-starter",
            "name": "Logo Starter",
            "tagline": "Simple logo creation for new projects and small businesses.",
            "price": "$500",
            "badge": "Popular",
            "features": [
                "2 custom logo ideas to choose from",
                "Color and font details guide",
                "Full high-resolution PNG & JPG files",
                "Vector source files included (AI, SVG)",
            ]
        },
        {
            "id": "full-branding",
            "name": "Full Brand Setup",
            "tagline": "Complete look for your business including logos, colors, and fonts.",
            "price": "$1,100",
            "badge": "Best Value",
            "features": [
                "3 logo concepts + icon versions",
                "Complete brand style rulebook",
                "Business card & letterhead designs",
                "Social media profile and banner templates",
            ]
        },
        {
            "id": "marketing-kit",
            "name": "Marketing Design",
            "tagline": "Print and digital promotional materials for ongoing ads.",
            "price": "$850",
            "badge": None,
            "features": [
                "Flyer, brochure, or poster layouts",
                "Custom social media post templates",
                "Web banner graphics",
                "Print-ready PDF files with crop marks",
            ]
        }
    ]
    return render(request, 'main/design_packages.html', {'packages': packages})
    
def animation_packages(request):
    packages = [
        {
            "id": "logo-animation",
            "name": "Animated Logo",
            "tagline": "Short moving logo intro and outro for video clips and channels.",
            "price": "$350",
            "badge": "Popular",
            "features": [
                "5 to 10-second custom logo motion",
                "Includes sound effects and audio sync",
                "Transparent background file (Alpha channel)",
                "Full HD & 4K video exports",
            ]
        },
        {
            "id": "social-motion",
            "name": "Social Motion Pack",
            "tagline": "Moving titles, lower thirds, and short ads for social media.",
            "price": "$750",
            "badge": "Best Value",
            "features": [
                "3 short motion graphic clips (up to 15s each)",
                "Animated title cards and lower thirds",
                "Vertical (9:16) and square (1:1) video formats",
                "Easy-to-edit graphic templates included",
            ]
        },
        {
            "id": "explainer-2d",
            "name": "2D Explainer Video",
            "tagline": "Full animated short video to explain product features or services simply.",
            "price": "$1,400",
            "badge": None,
            "features": [
                "Up to 60-second 2D animation",
                "Custom visual storyboard and characters",
                "Professional voiceover integration",
                "Background music and full sound effects",
            ]
        }
    ]
    return render(request, 'main/animation_packages.html', {'packages': packages})
    
def social_content_packages(request):
    packages = [
        {
            "id": "reels-starter",
            "name": "Reels & Shorts Pack",
            "tagline": "Short vertical videos edited for Instagram Reels, Shorts, and TikTok.",
            "price": "$450",
            "badge": "Popular",
            "features": [
                "5 short vertical video clips (15 to 30s)",
                "On-screen text captions and titles",
                "Color grading for bright screen views",
                "Trending audio matching and cutting",
            ]
        },
        {
            "id": "content-batch",
            "name": "Monthly Content Pack",
            "tagline": "A full set of videos and images to cover your social media calendar.",
            "price": "$950",
            "badge": "Best Value",
            "features": [
                "10 short vertical videos (Reels/TikTok)",
                "15 edited high-resolution photo posts",
                "Grid preview layout plan",
                "Formatted cover images and thumbnails",
            ]
        },
        {
            "id": "brand-assets",
            "name": "Social Launch Kit",
            "tagline": "Complete visual refresh for your social profiles and ad campaigns.",
            "price": "$650",
            "badge": None,
            "features": [
                "Profile avatars, header banners, and story highlights",
                "6 custom editable post templates",
                "3 promo video templates for sales and updates",
                "Brand style guide for social media use",
            ]
        }
    ]
    return render(request, 'main/social_content_packages.html', {'packages': packages})
    
def dj_packages(request):
    packages = [
        {
            "id": "private-party",
            "name": "Essential Party Pack",
            "tagline": "Ideal for birthdays, private gatherings, and intimate venue events.",
            "price": "$600",
            "badge": "Popular",
            "features": [
                "Up to 4 hours of live DJ performance",
                "Compact professional PA sound system",
                "Custom playlist curation based on your preferences",
                "2 ambient party lighting units",
            ]
        },
        {
            "id": "gala-wedding",
            "name": "Gala & Wedding Set",
            "tagline": "Complete sound and atmospheric lighting for major celebrations.",
            "price": "$1,200",
            "badge": "Best Value",
            "features": [
                "Up to 6 hours of live mixing & MC announcements",
                "Full high-power audio system with wireless mics",
                "Intelligent mood lighting and room uplighting",
                "Custom entrance and special moment song edits",
            ]
        },
        {
            "id": "club-vip",
            "name": "Club & Corporate VIP",
            "tagline": "High-energy club sets and corporate event sound engineering.",
            "price": "$1,800",
            "badge": None,
            "features": [
                "Full-day performance or multi-set schedule",
                "Concert-grade sound system and subwoofer setup",
                "Moving light heads & stage haze machine",
                "Dedicated sound engineer on site",
            ]
        }
    ]
    return render(request, 'main/dj_packages.html', {'packages': packages})
    
def custom_quote(request):
    packages = [
        {
            "id": "event-bundle",
            "name": "Event Coverage Bundle",
            "tagline": "Combine event video, photography, and live DJ entertainment for one seamless event solution.",
            "price": "$1,800",
            "badge": "Popular",
            "features": [
                "Full event video highlight & photo gallery",
                "Live DJ performance with pro sound & lights",
                "Single project coordinator on site",
                "Discounted multi-service bundle rate",
            ]
        },
        {
            "id": "brand-launch",
            "name": "Brand Launch Package",
            "tagline": "Everything you need to launch a new product or brand online from scratch.",
            "price": "$2,500",
            "badge": "Best Value",
            "features": [
                "Logo design & full brand identity kit",
                "Product photography & promo video editing",
                "Motion graphic intro & social media reels",
                "Commercial usage rights included",
            ]
        },
        {
            "id": "custom-retainer",
            "name": "Monthly Production Retainer",
            "tagline": "Ongoing monthly creative support across design, video, and social media production.",
            "price": "$1,200",
            "badge": None,
            "features": [
                "Dedicated monthly hours across all services",
                "Priority scheduling & fast turnaround",
                "Flexible scope allocation per month",
                "Regular strategy syncs",
            ]
        }
    ]
    return render(request, 'main/custom_quote.html', {'packages': packages})

def portfolio(request):
    # Fetch all uploaded portfolio items ordered by the newest uploads
    items = PortfolioItem.objects.all().order_by('-created_at')
    
    # Context variable 'items' matches the {% if items %} loop in portfolio.html
    return render(request, 'main/portfolio.html', {'items': items})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            admin_emails_raw = config('ADMIN_EMAILS', default=settings.ADMIN_EMAIL_LIST)
            admin_recipients = [email.strip() for email in admin_emails_raw.split(',')]
            
            context = {
                'name': data['name'],
                'phone': data['phone'],
                'email': data['email'],
                'service': data['service'].replace('_', ' ').title(),
                'event_date': data['event_date'] if data['event_date'] else 'Not Specified',
                'budget': data['budget'] if data['budget'] else 'Not Specified',
                'message': data['message'],
            }
            
            # --- Email 1: Alert Notification to Admins ---
            admin_html = render_to_string('emails/admin_notification.html', context)
            admin_text = strip_tags(admin_html)
            admin_msg = EmailMultiAlternatives(
                subject=f"New Creative Production Inquiry: {context['service']} - {data['name']}",
                body=admin_text,
                from_email=f'Studio Rishav <{config("EMAIL_HOST_USER", default="foto.rishav@gmail.com")}>',
                to=admin_recipients
            )
            admin_msg.attach_alternative(admin_html, "text/html")
            admin_msg.send()
            
            # --- Email 2: Confirmation Receipt to Client ---
            client_html = render_to_string('emails/client_confirmation.html', context)
            client_text = strip_tags(client_html)
            client_msg = EmailMultiAlternatives(
                subject="We've Received Your Creative Brief | Studio Rishav",
                body=client_text,
                from_email=f'Studio Rishav <{config("EMAIL_HOST_USER", default="foto.rishav@gmail.com")}>',
                to=[data['email']]
            )
            client_msg.attach_alternative(client_html, "text/html")
            client_msg.send()
            
            messages.success(request, "Your creative brief has been received. We review every vision with absolute intent and will align shortly.")
            return redirect('contact')
    else:
        form = ContactForm()
        
    return render(request, 'main/contact.html', {'form': form})

# def blog_list(request):
#     posts = Post.objects.filter(status='published').order_by('-created_on')
    
#     context = {
#         'posts': posts,
#         'meta_title': "Studio Journal — Cinema & Brand Strategy | Studio Rishav",
#         'meta_desc': "Read insights on premium editorial photography, avant-garde filmmaking, luxury event coverage, and creative visual branding identity systems.",
#     }
#     return render(request, 'blog/blog_list.html', context)

def blog_list(request):
    """
    Renders the static editorial blog journal archive page.
    Includes SEO meta parameters and dynamic canonical host routing.
    """
    # Active category selection from query string (e.g., ?category=photography)
    selected_category = request.GET.get('category', 'all').lower()

    context = {
        'selected_category': selected_category,
        'meta_title': "Studio Journal — Cinema, Photography & Brand Strategy | Studio Rishav",
        'meta_desc': "Read insights on premium editorial photography, avant-garde filmmaking, luxury event coverage, and creative visual branding identity systems.",
    }
    
    return render(request, 'main/blog_list.html', context)