$("document").ready(init);

function init()
{
	//alert("coming")
	detailDigi = $("a#digiMore");
	//detailDigi.click( {category: "digi"}, getMore);
	detailDigi.bind('click', {category: "di"}, getMore);

	detailRec = $("a#recMore");
	detailRec.bind('click', {category: "re"}, getMore);

	detailUpload = $("a#uploadMore");
	detailUpload.bind('click', {category: "up"}, getMore);

	digiClick = 1;
	recClick = 1;
	uplClick = 1;

}

function getMore(event)
{
	type = event.data.category;
	//alert(event.data.category);
	//alert("comingt to getMore");
	//if(type == "di"):
	//identify if content has to be added or removed;
	remove = true;
	if(type == "di")
	{
		if(digiClick == 1)
		{
			remove = false;
			digiClick = 0;
		}
		else
		{
			digiClick = 1;
		}
	}
	if(type == "re")
	{
		if(recClick == 1)
		{
			remove = false;
			recClick = 0;
		}
		else
		{
			recClick = 1;
		}
	}
	if(type == "up")
	{
		if(uplClick == 1)
		{
			remove = false;
			uplClick = 0;
		}
		else
		{
			uplClick = 1;
		}
	}
	if(remove == false)
	{
		//alert("coming to add");
		// add the details
		// ajax call to get all langwise
		$.get('/wa/userDetailsLangwise/', {category: event.data.category}, addDetailsToView , "json");
		//res = [{"count": 1, "language": u"English"}, {"count": 4, "language": u"Telugu"}];
		/*
		res = [{"count": "1", "language": "English"}, {"count": "4", "language": "Telugu"}];
		addDetailsToView(res)
		*/
		//$.ajax({url: "/wa/userDetailsLangwise/", data: {category: event.data.category}, })
	}
	else if(remove == true)
	{
		// remove the details
		// TOADD
		// alert("coming to remove");
		if(type == "di")
		{
			//remove children of digiMoreContainer
			spanDiv = $("span#digiMoreContainer");
		}
		else if(type == "re")
		{
			// remove children of recMoreContainer
			spanDiv = $("span#recMoreContainer");
		}
		else if(type == "up")
		{
			// remove children of uploadMoreContainer
			spanDiv = $("span#uploadMoreContainer");
		}
		spanDiv.empty();
	}
}

function addDetailsToView(data)
{
	dataGlobal = data;
	//alert("coming");
	//alert(data[0].language);
	//alert(type);
	if(type == "di")
	{
		spanDiv = $("span#digiMoreContainer");
	}
	else if(type == "re")
	{
		spanDiv = $("span#recMoreContainer");
	}
	else if(type == "up")
	{
		spanDiv = $("span#uploadMoreContainer");
	}
	$.each(data, addDivs);

}

function addDivs(index)
{ 
	tempDiv = document.createElement('div');
	if(type == "re" || type == "di")
	{ 
		tempDiv.innerHTML = "" + dataGlobal[index].count  + "  texts of " + dataGlobal[index].language + "" ;
	}
	else if(type = "up")
	{
		tempDiv.innerHTML = "" + dataGlobal[index].count  + " books of " + dataGlobal[index].language + "" ;
	}
	//alert(spanDiv);
	// TOADD
	spanDiv.append(tempDiv);
}