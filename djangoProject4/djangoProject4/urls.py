from django.contrib import admin
from django.urls import path
from myapp import views as user_views  # Переименуем второй импорт, чтобы избежать конфликта
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.catalog, name='catalog'),
    path('register/', user_views.register, name='register'),
    path('login/', user_views.user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('school/', user_views.school, name='school'),
    path('discount/', user_views.discount, name='discount'),
    path('read/', user_views.read, name='read'),
    path('book/<int:book_id>/', user_views.book_detail, name='book_detail'),
    path('cart/', user_views.cart_view, name='cart'),
    path('cart/add/<int:product_id>/', user_views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:book_id>/', user_views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', user_views.checkout_view, name='checkout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
