from django.urls import path
from .views import *


urlpatterns = [
    path('', AvitoMain.as_view(), name='main'),
    path('about/', about, name='about'),
    path('addpage/', AddAd.as_view(), name='add_ad'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('ads/<slug:ad_slug>/', ShowAd.as_view(), name='post'),
    path('category/<slug:cat_slug>/', AvitoCategory.as_view(), name='category')
]