'''
#!/usr/bin/env python
# -*- coding: utf8 -*-
from fpdf import FPDF
import os
from wa.models import Language,Book, Paragraph
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
from django.core.files import File

fontLanguageMap = {'Assamese':'lohit_bn','Bengali':'MuktiNarrow','Bodo':'gargi','Dogri':'gargi','Gujarati':'lohit_gu','Hindi':'gargi',
'Kannada':'Kedage-b','Konkani':'gargi','Maithili':'gargi','Malayalam':'','Manipuri':'',
'Marathi':'gargi','Nepali':'gargi','Oriya':'','Punjabi':'','Sanskrit':'gargi',
'Santali':'gargi','Sindhi':'gargi','Tamil':'TSCu_SaiIndira','Telugu':'','English':'Sawasdee'}

def concat(book_id):
	para_no = Paragraph.objects.filter(book=Book.objects.get(pk=book_id))
	infiles_list = []
	all_files_list = []
	offset=1;
	for i in para_no:
		file_name = str(book_id) + "/chunks/" + str(i.id) + "/DigiFiles/1.txt"
		if i.isChapter == 1:
			infiles_list = []
		infiles_list.append(file_name)
		if(offset<=len(para_no)-1):
			if (para_no[offset].isChapter==1):
				all_files_list.append(infiles_list)
		offset=offset+1

	#print("all_files_list")
	#print(all_files_list)
	return all_files_list

	
def pdfGen(Input,fontName,Output):
    pdf = FPDF()
    pdf.add_page()
    ttfName=fontName+'.ttf'
    pdf.add_font(fontName, '', ttfName, uni=True) 
    pdf.set_font(fontName, '', 14)
    linestring = open(Input, 'r').read()
    pdf.write(8,linestring)
    pdf.ln(20)
    pdf.output(Output, 'F')

	
def digiConcatenation(book_id):
	all_files_list=concat(book_id)
	count=1;
	Lang=Book.objects.get(pk = book_id).lang.langName
	#Lang=Language.objects.get(id=(Book.objects.get(pk = book_id)).lang).langName
	for i in all_files_list:
		for j in i:
			a = default_storage.open(j)
			path_to_save='/tmp/digiFiles/'
			local_fs = FileSystemStorage(location=path_to_save)
			local_fs.save(a.name,a)
	
		# all chapters: For each chapter one final1, final2.txt ..and corresponding pdf.
	for i in all_files_list:  
		path_final='/tmp/digiFiles/'+str(book_id)+'/'+str(count)+'.txt'
		with open(path_final, 'w') as fout:		
			# each chapter ka chunk
			for j in i:	  
				temp='/tmp/digiFiles/'+j
				ins = open( temp, "r" )
				for line in ins:
					fout.write(line)
				fout.write('\n\n')
		path_pdf='/tmp/digiFiles/'+str(book_id)+'/'+str(count)+'.pdf'		
		pdfGen(path_final,fontLanguageMap[Lang],path_pdf)	
		f = open(path_pdf, 'rb')
		myfile = File(f)
		new_name =str(book_id) + "/DigiChapters/Chapter"+str(count)+".pdf"
		default_storage.save(new_name,myfile)
		os.remove(path_final)
		os.remove(path_pdf)
		#local_fs.delete(path_final)
		count=count+1
		#fout.write('\f')	
	#path='/tmp/digiFiles/'
	#os.remove(path)
	
	for i in all_files_list:		
		for j in i:
			temp='/tmp/digiFiles/'
			os.remove(temp)
'''	
			
			
			
	

