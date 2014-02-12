from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
import re
def splitBookIntoPages(f_arg):
	print 'splitbook'
	rxcountpages = re.compile(r"$\s*/Type\s*/Page[/\s]", re.MULTILINE|re.DOTALL)
	data = file(f_arg,"rb").read()
	no_pages = len(rxcountpages.findall(data))
	file_for = f_arg+"[%d]"
	for i in range(0,2):
		filen = file_for%i
		with Image(filename=filen) as img:
			img.save(filename=("temp[%d].jpg"%i))
