from django.shortcuts import render, get_object_or_404

# Create your views here.
def HomePageView(request):
    return render(request, 'home.html')

def ContactPageView(request):
<<<<<<< HEAD
<<<<<<< HEAD
    return render(request, 'pages/contact.html')

def CatogoriesPageView(request):
    return render(request,'pages/categories.html')    
=======
=======
>>>>>>> upstream/main
    return render(request, 'pages/contact.html') 


def CartPageView(request):
<<<<<<< HEAD
    return render(request, 'pages/cart.html')      
>>>>>>> upstream/main
=======
    return render(request, 'pages/cart.html')      
>>>>>>> upstream/main
