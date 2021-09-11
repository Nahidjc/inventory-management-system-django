
from django.contrib import admin
from django.urls import path, include
from inventory import views
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('loginApp.urls')),
    path('inventory/', include('inventory.urls')),
    path('transactions/', include('transaction.urls')),
    path('', views.home, name='home'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
