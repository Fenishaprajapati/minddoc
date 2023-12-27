from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name="home"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('record/<int:pk>', views.customer_record, name="record"),
    path('delete_record/<int:pk>', views.delete_record, name="delete_record"),
    path('add_record/', views.add_record, name="add_record"),
    path('update_record/<int:pk>', views.update_record, name="update_record"),
    path('mental_state/', views.mental_state, name="mental_state"),
    path('anxiety_issues/', views.anxiety_issues, name="anxiety_issues"),
    path('depression_issues/', views.depression_issues, name="depression_issues"),
    path('common_diseases/', views.common_diseases, name="common_diseases"),
    path('phobias/', views.phobias, name="phobias"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)