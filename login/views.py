from django.shortcuts import render,redirect
from .models import Classifields,Category,Subcategory
from django.contrib.auth import authenticate,login,logout
from .forms import RegisterForm, ClassifieldForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView,UpdateView,ListView
from django.urls import reverse_lazy
# Create your views here .

def index(request):
       categories = Category.objects.all()
       classifields = Classifields.objects.all()
       context = {
            'classifields': classifields, 
            'categories': categories, 
             
            }
       return render(request, 'login/posts.html',context)
    
 #Create view for login page with context
@login_required(login_url='/login')
def create_classifield(request):
    if request.method == 'POST':
        form = ClassifieldForm(request.POST,request.FILES)
        if form.is_valid():
            post= form.save(commit=False)
            post.seller = request.user

            post.save()
            return redirect('/')
    else:
            form = ClassifieldForm()

    context = {          
          'form': form,
   }
    return render(request, 'login/create_classifield.html',context)



def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user =form.save()
            login(request,user)
            return redirect('/')
    else:
         form = RegisterForm()
    return render(request, 'registration/sign_up.html', {'form': form})

# create a view for search bar in the navbar
def search(request):
    if request.method == 'POST':
       
        search_query = request.POST['search_query']
        classifields = Classifields.objects.filter(title__contains=search_query)
        
        context = {
            'classifields': classifields,
            'search_query': search_query
        }
        return render(request, 'login/index.html',context)
    else:
        return render(request, 'login/search.html', {})

# create a view to select the classifieds that has title with 'accomodation needed'

def category(request,subcategory):
    print('subcategory',subcategory)

    categories = Category.objects.all()
    classifields = Classifields.objects.filter(subcategory__name=subcategory)
    context = {
             'classifields': classifields,
             'categories': categories,
     }
    return render(request, 'login/category.html',context)


#create a view to show the details of the classifieds
def show(request,id):
    categories = Category.objects.all()
    classifield = Classifields.objects.get(id=id)
  

    context = {
        'classifield': classifield,
        'categories': categories,
        'user': request.user,
    }
    return render(request, 'login/show.html',context)


# view to filter classified using location
def category_location(request,subcategory,location):
  
    categories = Category.objects.all() 
    classifields = Classifields.objects.filter(location__name= location)
    
    context = {
        'classifields': classifields,
        'categories': categories,
    }
    return render(request, 'login/category.html',context)

#create a view to display the classifieds that are posted by the seller
@login_required(login_url='/login')
def my_classifieds(request):
    categories = Category.objects.all()
    classifields = Classifields.objects.filter(seller=request.user)
    context = {
        'classifields': classifields,
        'categories': categories,
    }
    return render(request, 'login/category.html',context)
 
 #create a view to update the classifieds using generic updateView

class ClassifieldUpdateView(UpdateView):
     model = Classifields
     fields = "__all__"
     #exclude = ['seller']
     template_name_suffix = '_update_form'
     success_url = reverse_lazy('my_classifields')
     fields_excluding = ['seller']
          
#how do you write an elevator pitch for full stack web development?


     