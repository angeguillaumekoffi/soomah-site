from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Informations(models.Model):
    titre = models.CharField("Titre", max_length=256, blank=True, null=True)
    descri = RichTextField("Description", blank=True, null=True)
    url = models.CharField("url", max_length=25, blank=True, null=True)
    class Meta:
        db_table= "Informations"
        managed = True
        verbose_name = "Information"
        verbose_name_plural = "Informations"
    def __str__(self):
        return "{}".format(self.titre)
        
class Contacts(models.Model):
    nom = models.CharField("Nom", max_length=30, blank=True, null=True)
    email = models.CharField("Email", max_length=256, blank=True, null=True)
    objet = models.CharField("Objet", max_length=256, blank=True, null=True)
    message = RichTextField("Message", blank=True, null=True)
    class Meta:
        db_table= "Contacts"
        managed = True
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
    def __str__(self):
        return "{}".format(self.email)