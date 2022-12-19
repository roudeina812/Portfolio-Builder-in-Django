from django.db import models


# Create your models here.


class Person(models.Model):
    Login = models.CharField(max_length=20, unique= True)
    Password = models.CharField(max_length=20 , unique= True)
    Role = models.CharField(max_length=5)


class InfoPers(models.Model):
    Nom = models.CharField(max_length=20)
    Prenom = models.CharField(max_length=20)
    birthDate = models.DateField(default="2022-12-11")
    email = models.EmailField(max_length=254, null=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    gender = models.CharField(max_length=10, choices=(('F', 'Female'), ('M', 'Male')), default='F')
    State = models.CharField(max_length=30)
    DescPro = models.TextField()
    Philo_Statement = models.TextField()
    Bio = models.TextField()
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)


class Experience(models.Model):
    name = models.CharField(max_length=50)
    Exp = models.CharField(max_length=200)
    Type = models.CharField(max_length=10, choices=(('P', 'Professionel'), ('A', 'Associatif'),('R', 'Recompense')), default='F')
    Date_Debut = models.DateField()
    Date_Fini = models.DateField()
    Description = models.TextField()
    id_Person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)


class Justification(models.Model):
    name = models.CharField(max_length=50)
    id_Just = models.BigAutoField(primary_key=True)
    Fichier = models.FileField(max_length=None)
    id_Experience = models.ForeignKey(Experience, on_delete=models.CASCADE, null=True)
