from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from wa.models import User, Language, Book, Paragraph, UserHistory
# Create your views here.

def audio(request):
    #languages = Language.objects.all()
	#context = {'all_languages' : all_languages}
    #return render(request, 'wa/audio.html', context)
    #return HttpResponse("You're looking at the results of poll ")
    langs = Language.objects.all()
    context = {'langs': langs}
    return render(request, 'wa/audio.html', context)
