from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base.html')

def login_user(request):
    return render(request, 'registration/Login.html')

def createaccount(request):
    return render(request, 'registration/createAccount.html')

def documentation(request):
    return render(request, 'documentation.html')

def forgotpassword(request):
    return render(request, 'registration/forgotPassword.html')

def fashion(request):
    return render(request, 'fashion/fashion.html')

def fashionmen(request):
    return render(request, 'fashion/fashionMen.html')

def fashionmenauth(request):
    return render(request, 'fashion/fashionMenAuth.html')
    
def fashionwomen(request):
    return render(request, 'fashion/fashionWomen.html')

def gadgets(request):
    return render(request, 'gadget/gadgetHomepage.html')

def laptop(request):
    return render(request, 'gadget/gadgetLaptops.html')

def phone(request):
    return render(request, 'gadget/gadgetPhones.html')

def tv(request):
    return render(request, 'gadget/gadgettv.html')

def hair(request):
    return render(request, 'hair/hairHomePage.html')

def bonestraight(request):
    return render(request, 'hair/boneStraight.html')

def accessories(request):
    return render(request, 'hair/hairAccessories.html')

def accessoriesauth(request):
    return render(request, 'hair/hairAccessoriesAuth.html')

def humanhair(request):
    return render(request, 'hair/humanHair.html')

def humanhairauth(request):
    return render(request, 'hair/humanhairAuth.html')

def comparegadget(request):
    return render(request, 'compare/compareGadget.html')
