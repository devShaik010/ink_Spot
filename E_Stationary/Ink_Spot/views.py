from django.shortcuts import render , HttpResponse ,redirect
from django.contrib.auth.models import User 
from django.contrib.auth.hashers import check_password, make_password
# Import packages from Models

from .models.product import Product
from .models.categories import Categories
from .models.book import Book
from .models.b_catogeries import B_categories
from .models.customer import Customer



# Create your views here.
def index(request):
    product = Product.get_all()
    book = Book.get_all()
    user_profile = (request.session.get('name'))
    login_button = None
    if user_profile:
        login_button = None
    else:
        login_button = "LOGIN"  

    s_data = {}
    s_data['user'] = user_profile
    s_data['login']= login_button     
    s_data['product'] = product 
    s_data['book'] = book 

    return render(request, 'index.html' ,s_data)

# For Creating User ( signup )
def sign_up(request):
    if request.method == 'GET':
        return render(request, "signup.html")
    else:
        postData = request.POST
        name = postData.get('name')
        email = postData.get('email')
        phone = postData.get('phone')
        password = postData.get('password')
        rpassword = postData.get('rpassword')

        error_msg = None
        customer = Customer(name = name,email = email, phone = phone,password = password)
 

        if customer.isname():
            error_msg = "User name is Alredy taken"

        elif name == "" or email =="" or phone == "" or password =="":
            error_msg = "Fill The all fields"

        elif customer.isExist():
            error_msg = "Email Is Alredy Exist try to Login"

        elif customer.isnumber():
            error_msg = "Number is Alredy register try to login"    
        
        elif password != rpassword:
            error_msg = "Password does not macth"

        if error_msg:
            return render(request, "signup.html" ,{'error' : error_msg})


        else:     
           User.objects.create_user(username=name,
                                  email=email,
                                  password=password,)
           
           customer.password = make_password(customer.password)
           customer.register()
           
           return redirect('login')

# For Login 
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')

        customer = Customer(email = email , password = password)
        if customer.isExist():
            customer = Customer.get_cutomer_by_email(email)
        else:
            error_msg = "Invalid"
        error_msg = None


        if customer:
            flag = check_password(password , customer.password)
            if flag:
                request.session['customer_id']= customer.id
                request.session['email']= customer.email
                request.session['name']= customer.name
                
                return redirect('home')
            else:
                error_msg = "Email & password is Invalid"
                # print(customer)
                # print(email,password)
                return render(request, 'login.html' , {'error' : error_msg})
       

# for Books
def book(request):
    book = Book.get_all()
    book = None
    bcat = B_categories.all_catogaries()
    categoryID = request.GET.get('categories')
    if categoryID:
        book = Book.get_all_filter(categoryID )
    else:
        book = Book.get_all()

    user_profile = (request.session.get('name'))
    login_button = None
    if user_profile:
        login_button = None
    else:
        login_button = "LOGIN"  


    bdata = {} 
    bdata['book'] = book
    bdata['b_catogereis'] = bcat
    bdata['user'] = user_profile
    bdata['login']= login_button 

    return render(request, 'book.html',bdata)

  # for product _ stationary items

# For Products
def product(request):
    

    if request.method == 'POST':
        pr_id = request.POST.get('product')
        cart = request.session.get('cart')

        if cart:
            quantity = cart.get(pr_id)
            if quantity:
                cart[pr_id] = quantity+1
            else:
                cart[pr_id] = 1
        else:
            cart = {}
            cart[pr_id] = 1

        request.session['cart'] = cart         
        print(request.session['cart'])

    if request.method == "GET":
        cart = request.POST.get('cart')
        if cart:
            request.session.get('cart').clear()

    product = None
    cat = Categories.all_catogaries()
    categoryID = request.GET.get('categories')
    
    if categoryID:
        product = Product.get_all_filter(categoryID) 
    else:
        product = Product.get_all() 

    user_profile = (request.session.get('name'))
    login_button = None
    if user_profile:
        login_button = None
    else:
        login_button = "LOGIN"  
    

    data = {} 
    data['product'] = product
    data['catogereis'] = cat
    data['user'] = user_profile
    data['login']= login_button 
    return render(request, 'product.html',data)

   
     