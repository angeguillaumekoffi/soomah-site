from django.urls import path
from . import views

app_name = "profiles"
urlpatterns = [
    path("me/", views.ShowProfile.as_view(), name="show_self"),
    path("me/modifier/", views.EditProfile.as_view(), name="edit_self"),
    path("me/aider", views.VueAider.as_view(), name="aider"),
    path("me/liste/envoi/", views.VueListeEnvoi.as_view(), name="ListeEnvoi"),
    path("me/liste/envoi/confirmation/<slug:Id>/", views.VueConfirmerEnvoi.as_view(), name="ConfirmeEnvoi"),
    path("me/liste/envoyes/", views.VueHistoriqueEnvoi.as_view(), name="HEnvoye"),
    path("me/liste/reception/", views.VueListeReception.as_view(), name="ListeReception"),
    path("me/liste/reception/confirmation/<slug:Id>/", views.VueListeReception.as_view(), name="ConfirmeReception"),
    path("me/liste/montantrecu/", views.VueHistoriqueRecu.as_view(), name="MRecu"),
    path("me/inscription/informations/", views.VueInfosPerso.as_view(), name="infosPerso"),
    path("myaccount/suscribe/", views.VuePaypal.as_view(), name="paypal"),
    path('myaccount/suscribe/config/', views.stripe_config),  # new
    path('myaccount/suscribe/create-checkout-session/', views.create_checkout_session), # new
    path("me/success/<slug:session_id>/", views.SuccessView.as_view()), # new
    path("me/cancelled/", views.CancelledView.as_view()), # new
    path("<slug:slug>/", views.ShowProfile.as_view(), name="show"),
]
