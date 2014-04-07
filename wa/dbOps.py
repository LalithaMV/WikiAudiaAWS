from wa.models import Language, Book, Paragraph, UserHistory, Document, CustomUser
import logging
from utilities import pointsToAward
from django.db.models import F

def uploadDigiDb(para_id, user_id):
	'''
	a digitized document is uploaded
	first update the percentatge complete
	then add a row to the table specifying who read it
	then change the status of this chunk -- not for Digi
	'''
	log = logging.getLogger("wa")
	log.info("Coming into uploadDigiDb")

	para = Paragraph.objects.get(pk = para_id)

	book = para.book
	book.percentageCompleteDigi = book.percentageCompleteDigi + 1
	book.save()
	#book.status = 'va'

	para.digiBy = CustomUser.objects.get(pk = user_id)
	para.save()

	uh = UserHistory(user = CustomUser.objects.get(pk = user_id), action = 'di', paragraph = para)
	uh.save()

	user = CustomUser.objects.get(pk = user_id)
	user.points = user.points + pointsToAward("di")
	user.save()

def uploadAudioDb(para_id, user_id):
	log = logging.getLogger("wa")
	log.info("Coming into uploadAudioDb")
	log.info(user_id)
	
	para = Paragraph.objects.get(pk = para_id)

	book = para.book
	book.percentageCompleteAudio = book.percentageCompleteAudio + 1
	book.save()

	#para = Paragraph.objects.get(pk = para_id)
	para.validAudioVersionNumber = 1
	para.status = 'va'
	para.audioReadBy = CustomUser.objects.get(pk = user_id)
	para.save()
	
	uh = UserHistory(user = CustomUser.objects.get(pk = user_id), action = 're', paragraph = para, audioVersion = para.validAudioVersionNumber)
	uh.save()

	user = CustomUser.objects.get(pk = user_id)
	user.points = user.points + pointsToAward("re")
	user.save()

def validatedAudioDb(para_id, user_id, typeOfVote):
	#increment the count for para
	#put in user history
	para = Paragraph.objects.get(pk=para_id)
	if(typeOfVote == "upVote"):
		para.upVotes = F('upVotes') + 1
		uh = UserHistory(user = CustomUser.objects.get(pk = user_id), action = 'va', paragraph = para, vote = 'up')
	elif(typeOfVote == "downVote"):
		para.downVotes = F('downVotes') + 1
		uh = UserHistory(user = CustomUser.objects.get(pk = user_id), action = 'va', paragraph = para, vote = 'do')
	para.save()
	uh.save()
	
	#increment points
	user = CustomUser.objects.get(pk = user_id)
	user.points = user.points + pointsToAward("va")
	user.save()
