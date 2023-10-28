#WELCOME TO SUPER NOTES
#
#config/mod files use .snc ending (super notes config), to avoid
#being confused with other files
name=input("What do you want to title your notes?\n")
name=name+".txt"
file=open(name, "x")
file.close()
stop=False
load=""

print("Welcome to Super Notes!")
print("You can take notes here, and there are some special functions that")
print("will boost your speed and automate some functions.")
print("When you are done, the notes will be exported to a text file located")
print("in the \"outputs\" folder.")
print("\n\nControls:")
print("\nBox: boxes in a section of notes, type box again to end. Sentences may not exceed 90 characters")
load=input("\nWould you like to load notes from an existing file?")
load=load.lower()
if load[0]=="y":
    lfile=open(input("type the file name (including .txt)\n"), "r")
    wfile=open(name, "a")
    for line in lfile:
        line=line.strip()
        wfile.write(line+"\n")
        print(line)
    lfile.close()
    wfile.close()

config=input("Would you like to load a configuration?\nWARNING: Config files can perform unintended actions on your device, which may have serious consequences. Please\nonly use config files that you trust.\n")
config=config.lower()
using_mod=False
if config[0]=="y":
    global filename
    filename=input("type the config/mod file name\n")
    using_mod=True
    cfile=open(filename, "r")
    global modtag
    for line in cfile:
        line=line.strip()
        if "###title###" in line:
            line=line.replace("###title###", "")
            modtag="{ "
            modtag=modtag+line
            modtag=modtag+" }"
            title="Using "
            title=title+line
            title=title+" mod"
            print(title)
        elif ("###message###" in line) and (line[13] != "<"):
            line=line.replace("###message###", "")
            print(modtag, line)
        elif ("###message###" in line) and (line[13] == "<"):
            pass
        elif ("###code###" in line) and (line[11] != "<"):
            line=line.replace("###code###", "")
            print(modtag)
        elif ("###code###" in line) and (line[11] == "<"):
            pass
        else:
            print("Mod is not formatted correctly, now using default settings.")
            print("Check modrules.txt to see how to create a mod")

def check_mod(funct_name):
    cfile=open(filename, "r")
    loc="<"
    loc=loc+funct_name
    loc=loc+">"
    for line in cfile:
        line=line.strip()
        if loc in line:
            line=line.strip()
            if "###message###" in line:
                line=line.replace("###message###", "")
                mes=line.replace(loc, "")
                print(modtag, mes)
            elif "###code###" in line:
                line=line.replace("###code###", "")
                line=line.replace(loc, "")
                print(modtag, "is running code")
                eval(line)
    cfile.close()

def createHTML():
    hq_file_name=name.replace("txt", "html")
    file=open(hq_file_name, "x")
    file.close()
    hq_file=open(hq_file_name, "a")
    lq_file=open(name, "r")
    hq_file.write("<head>")
    hq_file.write("<title>"+hq_file_name.replace(".html", "")+"</title>")
    hq_file.write("<script src=\"files/webpage_functions.js\"></script>")
    hq_file.write("<link rel=\"stylesheet\" href=\"files/webpage_style.css\">")
    hq_file.write("</head>")
    hq_file.write("<body style=\"background-color:tan;\">")
    hq_file.write("<center><h1 class=\"title\">"+hq_file_name.replace(".html", "")+"</h1></center>")
    hq_file.write("<div class=\"body\">")
    eq_count=0
    p_id=0
    div_id=0
    for line in lq_file:
        line=line.strip()
        if (line[len(line)-1:]=="=") and eq_count==0:
            hq_file.write("<div id=\"div_"+str(div_id)+"\" class=\"roundBox\" width=100px; height=10px;\">")
            hq_file.write("<br/>")
            div_id+=1
            eq_count+=1
            line=""
        if line[len(line)-1:]=="+":
            line=line[:len(line)-1]
        if (line[len(line)-1:]=="=") and eq_count==1:
            line=""
            eq_count+=1
        hq_file.write("<div id=\"p_"+str(p_id)+"\" onClick=\"Highlight(d=\'p_"+str(p_id)+"\')\">")
        hq_file.write("<span>"+line+"</span>")
        hq_file.write("</div>")
        p_id+=1
        if eq_count==2:
            hq_file.write("<br/>")
            hq_file.write("</div>")
            eq_count=0
    hq_file.write("</div>")
    hq_file.write("<p>Hint: Click on a line to highlight it.</p>")
    hq_file.write("<script>footer()</script>")
    hq_file.write("</body>")

def main():
    global stop, quality
    if using_mod==True:
        check_mod("main")
    box=False
    while stop==False:
        words=input()
        in_file=open(name, "a")
        if words=="stop":
            in_file.write("\n\nAnnotated with Super Notes, 2023")
            high_quality=input("Would you like to create an additional higher quality document to make it easier to view your notes later?\n")
            if high_quality[0].lower()=="y":
                createHTML()
            stop=True
        elif words=="box" or words=="Box":
            if box==False:
                print("=========================enabled")
                in_file.write("==================================================\n")
                box=True
                if using_mod==True:
                    check_mod("boxstart")
            elif box==True:
                print("=========================disabled")
                in_file.write("==================================================\n")
                box=False
                if using_mod==True:
                    check_mod("boxend")
        else:
            if box==False:
                words=words+"\n"
                in_file.write(words)
            elif box==True:
                i=len(words)
                breakstring=""
                break_exists=False
                if i>45:
                    breakstring=words[45:]
                    break_exists=True
                    ii=len(breakstring)
                    while ii<49:
                        breakstring=breakstring+" "
                        ii+=1
                    breakstring+="+"
                    breakstring+="\n"
                words=words[:45]
                i=len(words)
                while i<49:
                    words=words+" "
                    i+=1
                words=words+"+"
                words=words+"\n"
                in_file.write(words)
                if break_exists==True:
                    in_file.write(breakstring)
        in_file.close()

main()
if using_mod==True:
    check_mod("end")
