$("document").ready(init);

function init()
{
	/*langSel = $("select#language");
	langSel.change(langChanged);*/
}

function langChanged(event)
{
	//event.preventDefault();
	if(langSel.val() != "default")
		$.get('/wa/audio/langBooks/', {language : langSel.val()}, addBooksToPage);
}
function addBooks()
{
	console.log("Add books : ");
}
function addBooksToPage(data,lang)
{
	//alert(this.oldvalue);
	console.log("Add books to page:"+data);
	dispDiv = document.getElementById(lang);
	var allLinks = $('a[id^="waLink_"]')
	//alert("length" + allLinks.length);
	//for (var aLink in allLinks)
	for(j=0;j<allLinks.length;j++)
	{
		aLink = allLinks[j]
		console.log($(aLink).parent('div#dispBooks').length);
		//alert(aLink.id);
		if(($(aLink).parent('div#dispBooks').length) != 0)
			dispDiv.removeChild(aLink);
	} 
	var json = JSON.parse(data);
	//alert(json[0].fields.lang);
	//alert(dispDiv);
	for(i =0, len = json.length; i < len; ++i)
	{
		//alert(json[i].pk);
		book = json[i];
		/*link = document.createElement('a')
		//alert(book.pk);
		link.id = "book" + book.pk;
		link.name = "book" + book.pk;
		link.innerHTML = "" + book.fields.bookName;*/
		//alert("{% url 'audioUpload' book.pk %}");
		//alert(book.fields.lang);
		fig = document.createElement('figure');
		fig.id = "fig_" + book.pk ;
		link = document.createElement('a');
		link.id = "waLink_" + book.pk;
		link.name = "waLink_" + book.pk;
		link.href = "/wa/audio/" + book.pk + "/";
		image = document.createElement('img');
		image.id = "figimg_" + book.pk;
		//image.src = "/wa/audio/getimage/" + book.pk + "/";
		image.src = "http://54.213.4.161/scripts/getImage.php?filename="+book.pk+"/bookThumbnail.png";
		image.height = 200;
		image.width = 150;
		image.style.border = "1px solid black";
		fig.appendChild(image);
		figcap = document.createElement('figcaption');
		figcap.id = "figcap_" + book.pk;
		figcap.innerHTML = book.fields.bookName;
		fig.appendChild(figcap);
		link.appendChild(fig);
        dispDiv.appendChild(link);
	}
	this.oldvalue = this.value;
}
