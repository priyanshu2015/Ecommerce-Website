
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index,name="home"),
    path("about/", views.about,name="AboutUs"),
    path("contact/", views.contact,name="ContactUs"),
    path("tracker/", views.tracker,name="TrackingStatus"),
    path("search/", views.search,name="Search"),
    path("products/<int:myid>", views.productView,name="ProductView"), # data provided by html when this href is called
    path("checkout/", views.checkout,name="Checkout"),

    # Payment With Razorpay
    path("payment/", views.app_create,name="payment"),
    path("payment/charge/", views.app_charge,name="charge"),

    # Authentication APIs
    path('handleLogout/', views.handleLogout, name='handleLogout'),
    path('myprofile/', views.myprofile,  name="myprofile"),
    path('handleLoginEmail/', views.handleLoginEmail, name='handleLoginEmail'),
    path('changeEmail/', views.changeEmail, name='changeEmail'),


]