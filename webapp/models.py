from django.db import models


# Create your models here.
<<<<<<< HEAD
<<<<<<< HEAD
class Gebruiker(models.Model):
    #userid = models.Autofield(primary_key=True)
    voornaam = models.charField(max_length=50)
    naam =  models.charField(max_length=50)
    email = models.charField(max_length=50)
    straatnaam = models.charField(max_length=50)
    huisnr = models.IntegerField()
    postcode = models.IntegerField()
    busnr = models.charField(max_length=10)
    telefoonnr = models.IntegerField()
    password= models.charField(max_length=30) #ToDo: add hashes + saltes (import)
    toegangslevel = models.ForeignKey(Toegangslevel, on_delete=models.CASCADE)

    def __str__(self):              # __unicode__ on Python
        return self.name
        #authentication https://docs.djangoproject.com/en/1.9/topics/auth/customizing/



class TblUserLog(models.Model)
    created = models.DateTimeField(auto_now_add=True)
    gebruiker = models.ForeignKey(Gebruiker, on_delete=models.CASCADE)
    tbllog = models.ForeignKey(TblLog, on_delete= models.CASCADE)


class TblLog(models.Model)
    logText = models.charField(255)
    tblUserLogs = models.ManytoManyField(Gebruiker, through="TblUserLogs")

 class Toegangslevel
    toegangslevelnaam = models.charField(255)
=======
class Panden(models.Model):
=======
class Pand(models.Model):
>>>>>>> origin/master
	#id autocreated by django
	straatnaam = models.CharField(max_length=128)
	huisnr = models.SmallIntegerField
	postcodeID = models.ForeignKey(Steden)
	pandtype = models.ForeignKey(Pandtype)
	handelstatus = models.ForeignKey(Handelstatus)
	voortgang = models.ForeignKey(Voortgang)

	def __str__(self):
        return self.id


class Tag(models.Model):
    #id autocreated by django
    tagnaam = models.CharField(max_length=128)
    Pand = models.ManyToManyField(Panden)

	def __str__(self):
        return self.id


class Stad(models.Model):
	postcode = models.SmallIntegerField
	stadsnaam = models.CharField(max_length=128)

	def __str__(self):
        return self.id

class Foto(models.Model):
	url = models.CharField(max_length=256)
	pand = models.ManyToManyField(Panden)

	def __str__(self):
        return self.id


class PandType(model.Model):
	pandtype = models.CharField(max_length=128) #kantoor,huis, appartement, ...

	def __str__(self):
        return self.id


class Handelstatus(models.Model)
	status = models.CharField(max_length=128) #verkoop, verhuur, verpachten, ...

	def __str__(self):
        return self.id


class Voortgang(models.Model)
	status = models.Charfiels(max_length=128) #online, optie, bij notaris, ...

<<<<<<< HEAD
>>>>>>> origin/master
=======
	def __str__(self):
        return self.id


>>>>>>> origin/master
