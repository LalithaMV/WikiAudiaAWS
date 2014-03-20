from wa.models import Language,Book, Paragraph, UserHistory, Document, CustomUser
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
