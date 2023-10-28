var notes;

async function makeNotes(){
	//create the note divs
	const response = await fetch("../notes.txt");
	notes = await response.text();
	notes = JSON.parse(notes);
	var i = 0;
	while (i<notes.length){
		var noteHolder = document.createElement("div");
		noteHolder.setAttribute("id", notes[i]);
		noteHolder.setAttribute("class", "noteHolder");
		noteHolder.setAttribute("onClick", "location.href=\'"+notes[i]+"\'");
		document.getElementById("main").appendChild(noteHolder);
		i++
	}
	i=0
	while (i<notes.length) {
		var nameSpot = document.createElement("div");
		nameSpot.setAttribute("class", "nameSpot");
		nameSpot.setAttribute("id", notes[i]+"_name");
		document.getElementById(notes[i]).appendChild(nameSpot);
		i++
	}
	i=0
	while (i<notes.length){
		var noteName = document.createElement("span");
		noteName.textContent=notes[i];
		document.getElementById(notes[i]+"_name").appendChild(noteName);
		i++
	}
}