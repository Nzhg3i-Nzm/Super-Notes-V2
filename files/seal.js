function makeSeal(){
	var div = document.createElement("div");
	div.setAttribute("id", "sealdiv");
	div.setAttribute("class", "sealdiv");
	document.body.appendChild(div);
	var sealimg = document.createElement("img");
	sealimg.setAttribute("src", "../images/seal.png");
	sealimg.setAttribute("class", "sealimg");
	sealimg.setAttribute("onClick", "searchNotes()")
	document.getElementById("sealdiv").appendChild(sealimg)
}

var input;

async function searchNotes(){
	input = prompt("What can I help you find?\n-Seal");
	located = [];
	for (i in notes){
		var response = await fetch("../"+notes[i]);
		response = await response.text();
		if (response.includes(input) == true){
			located.push(notes[i]);
		}
	}
	if (located.length != 0){
		assembled_string = "Found what you were looking for in: \n";
		for (j in located){
			assembled_string += located[j]+"\n";
		}
		assembled_string += "-Seal";
		alert(assembled_string);
	}
	else{
		alert("Sorry! I didn't find it anywhere.\n-Seal");
	}
}