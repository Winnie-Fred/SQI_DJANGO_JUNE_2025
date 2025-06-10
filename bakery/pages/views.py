from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "pages/home.html")


def about(request):
    return render(request, "pages/about.html")

def menu(request):
    pastries = {
        "Meatpie": {
            "price": 1200,
            "description": "A flaky, golden-brown pastry filled with seasoned minced meat, potatoes, and vegetables.",
            "image_path": "meatpie.jpg"
        },
        "Doughnut": {
            "price": 800,
            "description": "A soft, deep-fried ring-shaped treat coated with sugar and perfect for a sweet snack.",
            "image_path": "doughnut.jpg"
        },
        "Chicken Pie": {
            "price": 1300,
            "description": "A savory pastry packed with tender chicken chunks, creamy sauce, and mixed vegetables.",
            "image_path": "chicken-pie.jpg"
        },
        "Sausage Roll": {
            "price": 1000,
            "description": "A puff pastry rolled around juicy sausage meat, baked until crisp and golden.",
            "image_path": "sausage-roll.jpg"
        },
        "Fish Roll": {
            "price": 1100,
            "description": "A soft roll stuffed with spicy, flavorful fish filling, great for a light meal or snack.",
            "image_path": "fish-roll.jpg"
        }
    }

    return render(request, "pages/menu.html", {"pastries": pastries})


def contact(request):
    return render(request, "pages/contact.html")
