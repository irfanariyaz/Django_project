#write urlpatterns to map url requests to view functions 



from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    # path('home/', views.index, name='home'),
 
    path('sign_up/', views.sign_up, name='sign_up'),
    path('create_classifield/',views.create_classifield,name='create_classifield'),
    path('search/',views.search,name='search'),
    #path('category/',views.category,name='category'),
    #create a category url with a name of category as string and a view function as category
    path('category/<str:subcategory>/',views.category,name='category'),
    path('category/<str:subcategory>/<str:location>/',views.category_location,name='category_location'),
    path('show/<int:id>/',views.show,name='show'),
    path('my-classifields/',views.my_classifieds,name='my_classifields'),
    path('my-classifields/update/<int:pk>/',views.ClassifieldUpdateView.as_view(),name = 'update-classified')
    ]
