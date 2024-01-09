from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('record/<int:pk>', views.customer_record, name="record"),
    path('delete_record/<int:pk>', views.delete_record, name="delete_record"),
    path('add_record/', views.add_record, name="add_record"),
    path('update_record/<int:pk>', views.update_record, name="update_record"),
    path('mental_state/', views.mental_state, name="mental_state"),
    path('generalized_anxiety_disorder/', views.generalized_anxiety_disorder, name="generalized_anxiety_disorder"),
    path('social_anxiety_disorder/', views.social_anxiety_disorder, name="social_anxiety_disorder"),
    path('separation_anxiety_disorder/', views.separation_anxiety_disorder, name="separation_anxiety_disorder"),
    path('psychotic_depression/', views.psychotic_depression, name="psychotic_depression"),
    path('major_depressive_depression/', views.major_depressive_depression, name="major_depressive_depression"),
    path('situational_depression/', views.situational_depression, name="situational_depression"),
    path('post_traumatic_stress_disorder/', views.post_traumatic_stress_disorder, name="post_traumatic_stress_disorder"),
    path('obsessive_compulsive_disorder/', views.obsessive_compulsive_disorder, name="obsessive_compulsive_disorder"),
    path('dissociative_identity_disorder/', views.dissociative_identity_disorder, name="dissociative_identity_disorder"),
    path('phobias/', views.phobias, name="phobias"),
    path('subjects/', views.subjects, name="subjects"),
    path('objects/', views.objects, name="objects"),
    path('situations/', views.situations, name="situations"),
    path('experts/', views.experts, name="experts"),
    path('premium/', views.premium, name="premium"),
    path('goal_based_care/', views.goal_based_care, name="goal_based_care"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)