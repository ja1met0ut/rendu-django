from django.db import models

class Serie(models.Model):

    titre = models.CharField(max_length=100)

    realisateur = models.CharField(max_length=100)

    date_parution = models.DateField(blank=True, null=True)

    duree = models.IntegerField(blank=False)

    resume = models.TextField(null = True, blank = True)

    def __str__(self):
        chaine = f"{self.titre} réalisé par {self.realisateur} sortie le {self.date_parution}"
        return chaine

    def dico(self):
        return {"titre" : self.titre, "realisateur" : self.realisateur, "date_parution" : self.date_parution, "duree" : self.duree, "resume" : self.resume }
# Create your models here.
