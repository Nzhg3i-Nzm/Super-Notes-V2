let numNotes = 0
const noteNames = []
let noteNamesCount = 0

function footer(){
	var f = document.createElement("footer");
	document.body.appendChild(f);
	var p = document.createElement("p");
	var txt = document.createTextNode("Annotated with Super Notes, 2023");
	p.appendChild(txt);
	f.appendChild(p);
}

function Highlight(d){
	var element = document.getElementById(d);
	element.style.backgroundColor="lime";
}

function doSearch(){
	var term = document.getElementById('search').value;
	var filename = term.concat("", ".html");
	openNote(filename);
}

function openNote(fileName){
	var head = document.createElement("div");
	document.body.appendChild(head);
	let headName = fileName.concat("", "_head");
	head.setAttribute("id", headName);
	head.setAttribute("class", "holderHead");
	head.setAttribute("width", "1200px");
	head.setAttribute("height", "100px");
	addInfoToHead(fileName, headName);
	var holder = document.createElement("div");
	holder.setAttribute("id", fileName);
	holder.setAttribute("class", "iframeHolder");
	holder.setAttribute("style", "background-color: black;");
	holder.setAttribute("width", "1200px");
	holder.setAttribute("height", "600px");
	document.getElementById(headName).appendChild(holder);
	var frame = document.createElement("iframe");
	let frameName = fileName.concat("", "_frame");
	frame.setAttribute("id", frameName);
	frame.setAttribute("src", fileName);
	frame.setAttribute("class", "frame");
	frame.setAttribute("width", "1200px");
	frame.setAttribute("height", "600px");
	document.getElementById(fileName).appendChild(frame);
	numNotes = numNotes+1;
	noteNames[noteNamesCount] = fileName;
	noteNamesCount = noteNamesCount+1;
	updateSize()
}

function closeNote(fileName){
	head = fileName.concat("", "_head");
	//removing head also removes rest of note
	document.getElementById(head).remove()
	numNotes = numNotes - 1
	noteNamesCount = noteNamesCount - 1
	for (let i=0; i < noteNames.length; i++) {
		if (noteNames[i] == fileName) {
			noteNames.splice(i, 1);
		}
	}
	updateSize();
}

function updateSize(){
	var sizeW = (1200 / numNotes)+"px";
	var s = (1200 / numNotes);
	if (s < 301) {
		sizeW = 400+"px";
	}
	for (let i=0; i < noteNames.length; i++) {
		var baseName = noteNames[i];
		head = baseName.concat("", "_head");
		holder = noteNames[i];
		frame = baseName.concat("", "_frame");
		//begin head
		document.getElementById(head).setAttribute("width", sizeW);
		//begin holder
		document.getElementById(holder).setAttribute("width", sizeW);
		//begin frame
		document.getElementById(frame).setAttribute("width", sizeW);
	}
}

function addInfoToHead(fileName, headName) {
	const div = document.createElement("div");
	document.getElementById(headName).append(div);
	div.setAttribute("id", fileName+"_info");
	const name = document.createElement("p");
	const textNode = document.createTextNode("note - "+fileName);
	name.setAttribute("class", "info");
	name.append(textNode);
	document.getElementById(fileName+"_info").append(name);
	const x = document.createElement("img");
	document.getElementById(fileName+"_info").append(x);
	x.setAttribute("src", "images/x.png");
	x.setAttribute("class", "x");
	x.setAttribute("id", fileName+"_x");
	let action = "closeNote(\'"+fileName+"\')";
	x.setAttribute("onClick", action);
}

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
		box.setAttribute("onClick", "openNote('"+files[i]+"')");
		box.textContent = files[i];
		document.getElementById("dropdown").appendChild(box);
		i++;
	}
}