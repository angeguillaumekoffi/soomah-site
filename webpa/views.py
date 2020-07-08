from django.core.mail import send_mail, BadHeaderError
from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect
from Infos.models import Informations
from . import forms


class HomePage(generic.TemplateView):
    template_name = "home.html"
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        infos = Informations.objects.all()[:3]

        kwargs["infos"] = infos
        messages.info(request, "Bienvenue dans la communauté. Un monde nouveau s'ouvre à vous dès aujourd'hui.")
        return super().get(request, *args, **kwargs)


class AboutPage(generic.TemplateView):
    template_name = "about.html"
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        infos = Informations.objects.get(titre="QUI SOMMES-NOUS ?")

        kwargs["infos"] = infos
        return super().get(request, *args, **kwargs)

class ConditionPage(generic.TemplateView):
    template_name = "conditions.html"
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        infos = Informations.objects.get(titre="CONDITIONS D’UTILISATION")

        kwargs["infos"] = infos
        return super().get(request, *args, **kwargs)

class CommentDemarrer(generic.TemplateView):
    template_name = "howto.html"
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        infos = Informations.objects.get(titre="COMMENT BIEN DEMARRER ?")

        kwargs["infos"] = infos
        return super().get(request, *args, **kwargs)
        
class Faq(generic.TemplateView):
    template_name = "faq.html"
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        infos = Informations.objects.get(titre="FAQ")

        kwargs["infos"] = infos
        return super().get(request, *args, **kwargs)
        
class Contact(generic.TemplateView):
    template_name = "contact.html"
    http_method_names = ["get", "post"]

    def get(self, request, *args, **kwargs):
        if "contact_form" not in kwargs:
            kwargs["contact_form"] = forms.ContactForm(request.POST)
        return super().get(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        contact_form = forms.ContactForm(request.POST)
        if not (contact_form.is_valid()):
            messages.warning(
                request,
                "Echec de validadation ! Revoyez les details s'il vous plait.",
            )
            return super().get(request, contact_form=contact_form)
        # Both forms are fine. Time to save!
        mail = contact_form.save(commit=False)
        
        try:
            objet = form.cleaned_data['objet']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(objet, message, 'contact@soomah.org', ['angekoffiguillaume@gmail.com',])
        except BadHeaderError:
            #messages.warning(request, "Erreur d'entête !")
            #return redirect("contact")
            pass
        except:
            #messages.warning(request, "Echec d'envoi du mail !")
            #return redirect("contact")
            pass

        messages.success(request, "Merci de nous avoir contacté ! Vous recevrez par couriel une reponse de l'équipe ...")
        return redirect("contact")
        
        
