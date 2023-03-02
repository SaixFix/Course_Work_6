from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# TODO здесь необходимо подклюючит нужные нам urls к проекту

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),
    path("token/", TokenObtainPairView.as_view()),  # jwt
    path("token/refresh/", TokenRefreshView.as_view()),  # jwt
    path("auth/", include('djoser.urls')),  # djoser
    path("auth/", include('djoser.urls.jwt')),  # djoser авторю по токенам jwt
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
