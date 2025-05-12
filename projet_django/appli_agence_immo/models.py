from django.db import models

# Create your models here.


class Acheteurs(models.Model):
    nom=models.CharField(max_length=30,unique=True)
    id_acheteur=models.IntegerField(primary_key=True,unique=True)
    superficie=models.DecimalField(max_digits=6, decimal_places=2)
    nbr_chambre=models.IntegerField()
    garage=models.BooleanField()
    ville=models.CharField(max_length=30)

    class MetaAcheteurs:
        constraints = [
            models.UniqueConstraint(fields=['nom', 'id_acheteur'], name='ma_cle_unique')
        ]


class Bien_Immobiliers(models.Model):
    id_bien=models.IntegerField(primary_key=True)
    ville=models.CharField(max_length=30)
    surface=models.DecimalField(max_digits=6, decimal_places=2)
    nb_chambres=models.IntegerField()
    garage=models.BooleanField()
    etat=models.CharField(max_length=10)
    estimation=models.IntegerField(default=0)

class Vendeurs(models.Model):
    id_vendeur=models.IntegerField(primary_key=True)
    nom=models.CharField(max_length=30)


class Agent_immo(models.Model):
    id_agent=models.IntegerField(primary_key=True)
    id_bien=models.IntegerField()

class Achat(models.Model):
    id_bien=models.ForeignKey(Bien_Immobiliers,on_delete=models.CASCADE,primary_key=True)
    id_vendeur=models.ForeignKey(Vendeurs,on_delete=models.CASCADE)
    id_acheteur=models.ForeignKey(Acheteurs,on_delete=models.CASCADE)
    id_agent=models.ForeignKey(Agent_immo,on_delete=models.CASCADE)
    bien_achete=models.BooleanField()
    bien_visite=models.BooleanField()

class Rendez_Vous(models.Model):
    id_bien=models.ForeignKey(Bien_Immobiliers,on_delete=models.CASCADE)
    id_vendeur=models.ForeignKey(Vendeurs,on_delete=models.CASCADE)
    id_acheteur=models.ForeignKey(Acheteurs,on_delete=models.CASCADE)
    id_agent=models.ForeignKey(Agent_immo,on_delete=models.CASCADE)
    date=models.DateField()