from django.db import models
from separatedvaluesfield.models import SeparatedValuesField
# Create your models here.
# Have used camel case for all var names
class User(models.Model):
    #userId = models.PositiveIntegerField(default = 0) # do not use userID 0 while assigning 
    username = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    phoneNo = models.PositiveIntegerField(default = 0)
    languages = SeparatedValuesField(max_length = 254, token = ',')# models.CharField() 
    loginTimes = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

class Language(models.Model):
    #langId = models.IntegerField()
    langName = models.CharField(max_length = 30)
    def __unicode__(self):
        return self.langName

class Book(models.Model):
    #bookId = models.PositiveIntegerField(default = 0) #do not use bookId 0 while assigning 
    lang = models.ForeignKey(Language)
    author = models.CharField(max_length=200)
    bookName = models.CharField(max_length=200)
    #imageOfBook = models.CharField(max_length=254)
    percentageCompleteAudio = models.FloatField(default = 0)
    percentageCompleteDigi = models.FloatField(default = 0)
    percentageAudioInvalid = models.FloatField(default = 0)
    dBookDownloads = models.PositiveIntegerField(default = 0)
    aBookDownloads = models.PositiveIntegerField(default = 0)
    def __unicode__(self):
        return self.author + ',' + self.bookName + ',' + self.lang.langName

class Paragraph(models.Model):
    book = models.ForeignKey(Book)
    #paraId = models.PositiveIntegerField(default = 0)
    audioAssignedTo = models.ForeignKey(User, related_name = 'audioAssignedTo')
    audioReadBy = models.ForeignKey(User, related_name = 'audioReadBy')
    isRecording = models.BooleanField(default = False)
    digiAssignedTo = models.ForeignKey(User, related_name = 'digiAssignedTo')
    digiBy = models.ForeignKey(User, related_name = 'digiBy')
    isDigitizing = models.BooleanField(default = False)
    isChapter = models.BooleanField(default = False)
    validAudioVersionNumber = models.PositiveIntegerField()
    upVotes = models.PositiveIntegerField(default = 0)
    downVotes = models.PositiveIntegerField(default = 0)
    status = models.CharField(max_length = 2, choices = (('re', 'Recording'),('va', 'Validating'),('do', 'Done')))

class UserHistory(models.Model):
    user = models.ForeignKey(User)
    loginTime = models.DateTimeField(auto_now_add = True)
    logoutTime = models.DateTimeField()
    action = models.CharField(max_length = 2, choices = (('re','Recorded'),('di', 'Digitized'),('va', 'validateAudio'),('vd', 'validateDigi'),('up', 'uploadBook')))   
    paragraph = models.ForeignKey(Paragraph)
    vote = models.CharField(max_length = 2, choices = (('up', 'UpVote'), ('do', 'DownVote')), default = None)
    audioVersion = models.PositiveIntegerField(default = 0)
#autoincr??

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
