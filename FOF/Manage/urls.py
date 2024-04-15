from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # INDEX 
    path('', views.index, name="index"),

    # LOGIN SIGNUP 
    path('logins', views.logins, name='logins'),
    path('Logout_page', views.Logout_page, name='Logout_page'),
    path('signup', views.signup, name='signup'),
    path('userin4', views.userin4, name='userin4'),

    # MANAGE 
    path('manage', views.manage, name='manage'), 
    path('create', views.m_form, name="create"),
    path('create/land', views.land_form, name="land"),
    path('create/plant', views.plant_form, name="plant"),
    path('api/get-season-info/<int:season_id>/', views.get_season_info, name='get_season_info'),
    path('api/get-land-by-season/<int:season_id>/', views.get_land_by_season, name='get-land-by-season'),
    path('api/get-land-info/<int:land_id>/', views.get_land_info, name='get-land-info'),
    path('api/get-plant-by-land/<int:land_id>/', views.get_plant_by_land, name='get-plant-by-land'),
    
    # RESOURCE


    # MARKET 
    path('maker', views.maker, name="maker"),
    path('maker_sell/', views.maker_sell, name="maker_sell"),

    # CONTACT 
    path('contact', views.contact, name="contact"),
   
]

# Tạo một danh sách mới chỉ chứa urlpatterns cho đường dẫn 'search'
search_urlpatterns = [
    path('search', views.search, name='search'),
]

# Kết hợp static settings chỉ cho search_urlpatterns
search_urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=search_urlpatterns

