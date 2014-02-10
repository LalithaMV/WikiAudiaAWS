from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import json
from django.core import serializers
from django.conf import settings
import os
from PIL import Image
from wa.models import User, Language, Book, Paragraph, UserHistory
# Create your views here.

def audioSelection(request):
    #languages = Language.objects.all()
	#context = {'all_languages' : all_languages}
    #return render(request, 'wa/audio.html', context)
    #return HttpResponse("You're looking at the results of poll ")
    langs = Language.objects.all()
    #context = {'langs': langs}
    context = RequestContext(request, {'langs': langs, } )
    return render(request, 'wa/audio.html', context)

def getImage(request, book_id):
	response = HttpResponse(mimetype = "image/jpg");
	path = os.path.dirname(settings.BASE_DIR) + "/" + "wastore/" + book_id + "/" + "frontcover.jpg"
	print(path);
	if(os.path.exists(path)):
		image = Image.open(path)
	else:
		image = Image.open(os.path.dirname(settings.BASE_DIR) + "/" + "wastore/" + "default/" + "frontcover.jpg")
	image.save(response, 'png');
	return response; 

def audioUpload(request, book_id):
	#print("book_id")
	#print(book_id)
	return HttpResponse("You're looking at poll %s" %  book_id)
	#Make a function call for choosing a para for the user.
	#render ash's view

def langBooks(request):
	#print(os.path.dirname(settings.BASE_DIR))
	#outside = os.path.dirname(settings.BASE_DIR)
	#if(os.path.exists())
	language = request.GET['language']
	#print(language);
	language = Language.objects.get(langName = language)
	#print(language)
	languageBooks = language.book_set.all()
	ret = serializers.serialize("json", languageBooks)
	#resp = HttpResponse(content_type = "application/json");
	#json.dump(languageBooks, resp)
	return HttpResponse(ret)


