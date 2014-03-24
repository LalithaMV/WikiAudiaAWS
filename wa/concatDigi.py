from wa.models import Language,Book, Paragraph

def concat(book_id):
	print("in concat")
	para_no = Paragraph.objects.filter(book=Book.objects.get(pk=book_id))
	infiles_list = []
	all_files_list = []
	for i in para_no:
		if i.isChapter == 1:
			#save the done concatenated file by taking the no and reset the cumulation file
			all_files_list.append(infiles_list)
			print("infiles_list")
			print(infiles_list)
			infiles_list = []
		else:
			#add the audio file to the cumulation file 
			file_name = str(book_id) + "/chunks/" + str(i.id) + "/DigiFiles/1.txt"
			infiles_list.append(file_name)

	all_files_list.append(infiles_list)
	
	print("all_files_list")
	print(all_files_list)
'''
Interface: 
once the percentageDigiComplete = number of chunks, call this function to form a pdf of the book 
I/P : bookID
first get the para_Ids
Then create path by appending required things
Then get these files from mongo to local system (tmp/book_id/digi/)
Now concatenate them (Give a new line after each file)
then call pdfGen
Now save this to gridfs
Then delete all the files in tmp/book_id/digi/
'''
def digiConcatenation(book_id):
	print("in concat Digi")
	concat(book_id)

