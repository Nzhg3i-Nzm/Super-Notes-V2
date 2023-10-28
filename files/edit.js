function dropdown(){
	document.getElementById("dropdown").classList.toggle("show");
	document.getElementById("dropButton").classList.add("dropButton2");
	document.getElementById("dropButton").classList.remove("dropButton");
}

async function makeDropdown(){
	const response = await fetch("../notes.txt");
	var files = await response.text();
	files = JSON.parse(files);
	var i = 0;
	while (i<files.length){
		var box = document.createElement("div");
		box.setAttribute("onClick", "loadNote('"+files[i]+"')");
		box.textContent = files[i];
		document.getElementById("dropdown").appendChild(box);
		i++;
	}
}

var lines = 0;
var line_order = [];
var nameOfFile = "";
var isNoteOpen = false;

async function loadNote(filename){
	if (isNoteOpen == false){
		filename = filename.slice(0, filename.length-4);
		filename = filename+"txt";
		nameOfFile = filename;
		const response = await fetch("../"+filename);
		var content = await response.text();
		console.log(content);
		var textbox = document.createElement("div");
		textbox.setAttribute("id", "textHolder");
		textbox.setAttribute("class", "textHolder");
		document.getElementById("main").appendChild(textbox);
		content = content.split("\r\n");
		for (string in content){
			lines+=1;
			line_order.push(lines);
			var box = document.createElement("div");
			box.setAttribute("id", "content_"+lines);
			box.setAttribute("class", "textEditor");
			box.setAttribute("contentEditable", true);
			box.setAttribute("onKeyDown", "addNewLine('content_"+lines+"', "+lines+", event)");
			box.textContent = content[string];
			document.getElementById("textHolder").appendChild(box);
		}
		isNoteOpen = true;
	}
	else{
		alert("Please refresh the page to open another note.");
	}
}

function saveNewContent(length){
	newContent = ""
	i=0
	while (i<line_order.length){
		newContent += (document.getElementById("content_"+line_order[i]).textContent) + "\n";
		i++;
	}
	return newContent;
}

function sendNewContent(filename, content){
	fetch("../edit", {
		method: "POST",
		body: content,
		headers: {
			"File": filename
	}
	})
}

async function makeNewFile(filename){
	const response = await fetch("../notes.txt");
	var files = await response.text();
	files = JSON.parse(files);
	if (files.includes(filename+".html")){
		alert("Unable to create note. A note with that name already exists.");
	}
	else{
		filename += ".txt";
		fetch("../newFile", {
			method: "POST",
			body: "",
			headers: {
				"File": filename
		}
		})
	}
}

function addNewLine(textboxId, index, event){
	if (event.key.toString() == 'Enter') {
		event.preventDefault();
		lines++;
		line_order.splice(line_order[index-1], 0, lines);
		var box = document.createElement("div");
		box.setAttribute("id", "content_"+lines);
		box.setAttribute("class", "textEditor");
		box.setAttribute("contentEditable", true);
		box.setAttribute("onKeyDown", "addNewLine(\"content_"+lines+"\", "+lines+", event)");
		box.textContent = "";
		document.getElementById(textboxId).after(box);
	}
}