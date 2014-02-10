from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from wa.models import User, Language, Book, Paragraph, UserHistory, Document
from wa.forms import DocumentForm
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from forms import CustomUserCreationForm
from django.shortcuts import render
from fpdf import FPDF

from wa.tasks import soundProcessingWithAuphonicTask
from django.core.urlresolvers import reverse
# Create your views here.

def error_processor(request):
	if 'error' in request.session:
		return {'msg': request.session['error']}
	else:
		return {}
	
def front(request):
	c=RequestContext(request,{'foo':'bar',},[error_processor])
	if 'error' in request.session:
		del request.session['error']
	return render_to_response('wa/session/front.html',c)
	
def logout(request):
	auth.logout(request)
	#return render_to_response('WikiApp/session/front.html')	
	return HttpResponseRedirect('/wa')
	
def auth_view(request):
	username= request.POST.get('username','')
	password= request.POST.get('password','')
	user= auth.authenticate(username=username, password=password)
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/wa/home')
	else:
		request.session['error'] = "Username and Password do not match.Try Again!"
		return HttpResponseRedirect('/wa')
#Have not done auth.logout(request)	
def home(request):
	return render_to_response('wa/session/home.html', {'full_name':request.user.first_name,'languages_known':request.user.languages_known,'points':request.user.points })
	#return render_to_response('WikiApp/session/home.html', {'full_name':request.user.userprofile.Languages})

def register_user(request):
	if request.method == 'POST':
		form=CustomUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/wa/register_success')
	else:
		form= CustomUserCreationForm()
	return render(request,  'wa/session/register.html', {
		'form': form,
	})
def register_success(request):
	return render_to_response('wa/session/register_success.html')
	
def digitize(request):
	return render_to_response('wa/AudioDigi/Digitize.html')
def audio(request):
    #languages = Language.objects.all()
	#context = {'all_languages' : all_languages}
    #return render(request, 'wa/audio.html', context)
    #return HttpResponse("You're looking at the results of poll ")
    langs = Language.objects.all()
    context = {'langs': langs}
    return render(request, 'wa/audio.html', context)

def audioUpload(request):
    # Handle file upload
    '''
    Add additional inputs to post to figure out the book and 
    the paragraph number so that the upload takes place in that folder
    Current working : Saves the file with a fixed name and the file sent for API processing is fixed as well. 
    Both of these should be made dynamic 
    '''
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.docfile.save('Ashu.wav',request.FILES['docfile'])
            #soundProcessWithAuphonic('documents/Ashu.wav')
            soundProcessingWithAuphonicTask.delay('../documents/ashu.mp3')
            return HttpResponseRedirect(reverse('wa.views.audio'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'wa/audioUpload.html',
        {'documents': documents, 'form': form},
       
        context_instance=RequestContext(request)
    )

def uploadDigi(request):
	if request.POST.has_key('unicode_data'):
		file = open("DigiFiles/KannadaInput.txt", "w")
		file.write((request.POST['unicode_data']).encode('utf8'))
		file.close()
		#concatenateDigi(request)
		pdfGen(request)
		x = request.POST['unicode_data']
		return HttpResponse(x)
	
def ajax(request):
	if request.POST.has_key('client_response'):
		x = request.POST['client_response']                 
		#y = socket.gethostbyname(x)                          
		response_dict = {}                                         
		#response_dict.update({'server_response': y })                                                                  
		return HttpResponse('Success')
	else:
		return render_to_response('WikiApp/AudioDigi/trial.html', context_instance=RequestContext(request))		
		
def concatenateDigi(request):
	filenames = ['DigiFiles/one.txt','DigiFiles/two.txt']
	with open('DigiFiles/final.txt', 'w') as fout:
		for line in fileinput.input(filenames):
			fout.write(line)
def pdfGen(request):
	pdf = FPDF()
	pdf.add_page()
	#pdf.add_font('gargi', '', 'gargi.ttf', uni=True) 
	#pdf.set_font('gargi', '', 14)
	#pdf.write(8, u'Hindi: एक अमरीकि')
	pdf.add_font('Kedage-b', '', 'Kedage-b.ttf', uni=True) 
	pdf.set_font('Kedage-b', '', 14)
	#pdf.add_font('TSCu_SaiIndira', '', 'TSCu_SaiIndira.ttf', uni=True) 
	#pdf.set_font('TSCu_SaiIndira', '', 14)
	linestring = open('DigiFiles/KannadaInput.txt', 'r').read()
	pdf.write(8,linestring)
	pdf.ln(20)
	pdf.output("DigiFiles/KannadaOutput.pdf", 'F')
			
			

	
