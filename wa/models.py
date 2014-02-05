from django.db import models
from django.utils import timezone
from separatedvaluesfield.models import SeparatedValuesField
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager
# Create your models here.
# Have used camel case for all var names
class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None,**extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    A fully featured User model with admin-compliant permissions that uses
    a full-length email field as the username.

    Email and password are required. Other fields are optional.
    """
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    
    languages_known=models.CharField(max_length=50)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['languages_known','first_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])
		
'''		
class User(models.Model):
    #userId = models.PositiveIntegerField(default = 0) # do not use userID 0 while assigning 
    username = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    phoneNo = models.PositiveIntegerField(default = 0)
    languages = SeparatedValuesField(max_length = 254, token = ',')# models.CharField() 
    loginTimes = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
'''	

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
    audioAssignedTo = models.ForeignKey(CustomUser, related_name = 'audioAssignedTo')
    audioReadBy = models.ForeignKey(CustomUser, related_name = 'audioReadBy')
    isRecording = models.BooleanField(default = False)
    digiAssignedTo = models.ForeignKey(CustomUser, related_name = 'digiAssignedTo')
    digiBy = models.ForeignKey(CustomUser, related_name = 'digiBy')
    isDigitizing = models.BooleanField(default = False)
    isChapter = models.BooleanField(default = False)
    validAudioVersionNumber = models.PositiveIntegerField()
    upVotes = models.PositiveIntegerField(default = 0)
    downVotes = models.PositiveIntegerField(default = 0)
    status = models.CharField(max_length = 2, choices = (('re', 'Recording'),('va', 'Validating'),('do', 'Done')))

class UserHistory(models.Model):
    user = models.ForeignKey(CustomUser)
    loginTime = models.DateTimeField(auto_now_add = True)
    logoutTime = models.DateTimeField()
    action = models.CharField(max_length = 2, choices = (('re','Recorded'),('di', 'Digitized'),('va', 'validateAudio'),('vd', 'validateDigi'),('up', 'uploadBook')))   
    paragraph = models.ForeignKey(Paragraph)
    vote = models.CharField(max_length = 2, choices = (('up', 'UpVote'), ('do', 'DownVote')), default = None)
    audioVersion = models.PositiveIntegerField(default = 0)
#autoincr??

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
