from wa.models import Book,Paragraph
import logging
def audioConcatenation(book_id):
	version_no = Paragraph.objects.filter(book=Book.objects.get(pk=book_id))
	chapter_no=1
	infiles_list = []
	all_files_list = []
	for i in version_no:
		version_val =  i.validAudioVersionNumber + 1
		if i.isChapter == 1:
			#save the done concatenated file by taking the no and reset the cumulation file
			all_files_list.append(infiles_list)
			infiles_list = []
		else:
			#add the audio file to the cumulation file 
			file_name = str(book_id) + "/chunks/" + str(i.id) + "/AudioFiles/"+str(version_val)+".wav"
			infiles_list.append(file_name)
	
	all_files_list.append(infiles_list)
	logger = logging.getLogger('wa')
	logger.info(all_files_list)
		#str(book_id) + "/chunks/" + str(para_id) + "/AudioFiles/1.wav"

def getNo():
	i=0
	while True:
		yield i
		i=i+1