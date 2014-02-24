'''
	Input the userID and whether the paragraph should 
	be given for recording or digitization 
'''
from wa.models import Paragraph,CustomUser
def getChunkID(userID,bookID,type):
    try:       
        cu = CustomUser.objects.get(pk=userID)
        if type is 0:
        	chunks_assigned_to_user =  Paragraph.objects.filter(bookID=bookID
        		).filter(audioAssignedTo_id=userID
        		).filter(audioReadBy_id__isnull=True)
        	if chunks_assigned_to_user.length is not null:
        		'''
        			If a chunk which is assigned to user is found
        			but is not recorded send the first available row 
        			back to the user
        		'''
        		return chunks_assigned_to_user[0]
        	else:
        		'''
        			Assign a range to the user according to window size
        		'''
        		#assigned_till_chunk_id = 
        		#last_unread_para_id =         		     		
        		window_size = 3
        		assignWindow(window_size,bookID,userID)
        		chunks_assigned_to_user =  Paragraph.objects.filter(bookID=bookID
        		).filter(audioAssignedTo_id=userID
        		).filter(audioReadBy_id__isnull=True)
        		return chunks_assigned_to_user[0]

    except:
        return 0

def assignWindow(window_size,bookID,userID):
	chunkId = startId
	chunk = Paragraph.objects.filter(bookID=bookID
				).filter(audioReadBy_id__isnull=True)	
	i = 0 
	for c in chunk:
		if i<window_size:
			try:
				chunkId = c.id;
				c.audioAssignedTo_id = userID;
				c.save()
				i=i+1
			except:
				break


