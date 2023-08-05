
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import  static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include("base.urls.user_urls")),
    path('api/company/', include("base.urls.company_urls")),
    path('api/admin/', include("base.urls.admin_urls")),
    path('api/tailor/', include("base.urls.tailor_urls")),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

