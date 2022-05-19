from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class SerieForm(ModelForm):
    class Meta:
        model = models.Serie
        fields = ('titre', 'realisateur', 'date_parution', 'duree', 'resume')
        labels = {
            'titre' : _('Titre'),
            'realisateur' : _('Realisateur'),
            'date_parution' : _('Date de parution'),
            'duree' : _('Duree'),
            'resume' : _('Resume'),
        }
        localized_fields = ('date_parution',)