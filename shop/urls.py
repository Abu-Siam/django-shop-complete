from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from shop import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm
urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    # path('', views.home),
    path('product-detail/<int:pk>', views.ProductDetail.as_view(), name='product-detail'),
    # path('product-detail/', views.product_detail, name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('mobile/', views.mobile, name='mobile'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name='login'),
    # path('login/', views.login, name='login'),

    # path('registration/', views.customerregistration, name='customerregistration'),
    path('registration/', views.SignUpView.as_view(), name='customerregistration'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)