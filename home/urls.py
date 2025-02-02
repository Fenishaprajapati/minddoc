from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('<int:year>/<str:month>', views.events, name="events"),
    path('events/', views.events, name="events"),
    path('events_list/', views.events_list, name="events_list"),
    path('add_venue/', views.add_venue, name="add_venue"),
    path('list_venue/', views.list_venue, name="list_venue"),
    path('show_venue/<venue_id>', views.show_venue, name="show_venue"),
    path('search_venues/', views.search_venues, name="search_venues"),
    path('venue_text/', views.venue_text, name="venue_text"),
    path('add_event/', views.add_event, name="add_event"),
    path('update_event/<event_id>', views.update_event, name="update_event"),
    path('update_venue/<venue_id>', views.update_venue, name="update_venue"),
    path('delete_event/<event_id>', views.delete_event, name="delete_event"),
    path('my_events', views.my_events, name="my_events"),
    path('venue_events/<venue_id>', views.venue_events, name="venue_events"),
    path('show_event/<event_id>', views.show_event, name="show_event"),
    path('update_gbc/<gbc_id>', views.update_gbc, name="update_gbc"),

    
    # path('delete_record/<int:pk>', views.delete_record, name="delete_record"),
    # path('add_record/', views.add_record, name="add_record"),
    # path('update_record/<int:pk>', views.update_record, name="update_record"),
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
    path('subjects/', views.subjects, name="subjects"),                         #subjects
    path('anthrophobia/', views.anthrophobia, name="anthrophobia"),
    path('zoophobia/', views.zoophobia, name="zoophobia"),
    path('coulrophobia/', views.coulrophobia, name="coulrophobia"),
    path('genophobia/', views.genophobia, name="genophobia"),
    path('cacophobia/', views.cacophobia, name="cacophobia"),
    path('automatonophobia/', views.automatonophobia, name="automatonophobia"),
    path('ombrophobia/', views.ombrophobia, name="ombrophobia"),
    path('kosmikophobia/', views.kosmikophobia, name="kosmikophobia"),
    path('archnophobia/', views.archnophobia, name="archnophobia"),
    path('ophidiophobia/', views.ophidiophobia, name="ophidiophobia"),
    path('entomophobia/', views.entomophobia, name="entomophobia"),
    path('hylophobia/', views.hylophobia, name="hylophobia"),
    path('objects/', views.objects, name="objects"),                            #objects
    path('noscomephobia/', views.noscomephobia, name="noscomephobia"),                            
    path('hemophobia/', views.hemophobia, name="hemophobia"),                            
    path('photophobia/', views.photophobia, name="photophobia"),                            
    path('trypophobia/', views.trypophobia, name="trypophobia"),                            
    path('aichmophobia/', views.aichmophobia, name="aichmophobia"),                            
    path('nomophobia/', views.nomophobia, name="nomophobia"),                            
    path('pyrophobia/', views.pyrophobia, name="pyrophobia"),                            
    path('acidophobia/', views.acidophobia, name="acidophobia"),                            
    path('kinemortophobia/', views.kinemortophobia, name="kinemortophobia"),                            
    path('pediophobia/', views.pediophobia, name="pediophobia"),                            
    path('eisoptrophobia/', views.eisoptrophobia, name="eisoptrophobia"),                            
    path('chronomentophobia/', views.chronomentophobia, name="chronomentophobia"),                            
    path('situations/', views.situations, name="situations"),                   #situations
    path('acrophobia/', views.acrophobia, name="acrophobia"),                   
    path('claustrophobia/', views.claustrophobia, name="claustrophobia"),                   
    path('aquaphobia/', views.aquaphobia, name="aquaphobia"),                   
    path('glossophobia/', views.glossophobia, name="glossophobia"),                   
    path('monophobia/', views.monophobia, name="monophobia"),                   
    path('nyctophobia/', views.nyctophobia, name="nyctophobia"),                   
    path('astraphobia/', views.astraphobia, name="astraphobia"),                   
    path('agoraphobia/', views.agoraphobia, name="agoraphobia"),                   
    path('taphophobia/', views.taphophobia, name="taphophobia"),                   
    path('rhabdophobia/', views.rhabdophobia, name="rhabdophobia"),                   
    path('fomo/', views.fomo, name="fomo"),        
                               
    path('experts/', views.experts, name="experts"),

    path('experts_premium/', views.experts_premium, name="experts_premium"),
    path('experts_premium2/', views.experts_premium2, name="experts_premium2"),

    path("manage_appointments/", views.manage_appointments, name="manage_appointments"),
    path("manage_appointments2/", views.manage_appointments2, name="manage_appointments2"),

    path('premium/', views.premium, name="premium"),
    path('goal_based_care/', views.goal_based_care, name="goal_based_care"),
    path('goal_based_care_premium/', views.goal_based_care_premium, name="goal_based_care_premium"),
    path('goal_based_care_premium_level2/', views.goal_based_care_premium_level2, name="goal_based_care_premium_level2"),
    path('goal_based_care_premium_level3/', views.goal_based_care_premium_level3, name="goal_based_care_premium_level3"),
    path('report/', views.report, name="report"),
    
    path('quiz/', views.quiz, name="quiz"),
    path('results/', views.quiz_results, name='quiz_results'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)