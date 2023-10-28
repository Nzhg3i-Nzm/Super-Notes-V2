import http.server as HttpServer
import socketserver
import os

def updateNoteList():
    notes=os.listdir()
    bannedPaths=['edit.html', 'files', 'images', 'notes.txt', 'server.py', 'super_notes_viewer.html', 'userhome.html']
    i=0
    while i<len(bannedPaths):
        notes.remove(bannedPaths[i])
        i+=1
    i=0
    while i<len(notes):
        if str(notes[i])[len(notes[i])-3:]=="txt":
                notes.remove(notes[i])
        i+=1
    notes=str(notes)
    #change from ' to " because javascript JSON parser requires double quote
    notes=notes.replace("\'", "\"")
    file=open("notes.txt", "w+")
    file.write(notes)
    file.close()

updateNoteList()

def convertToHTML(name):
    hq_file_name=name.replace("txt", "html")
    try:
        file=open(hq_file_name, "x")
        file.close()
    except:
        file=open(hq_file_name, "r")
        file.close()
    #erase file
    hq_file=open(hq_file_name, "w")
    hq_file.write("")
    #put new content into file
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


#main server code
class MyHttpRequestHandler(HttpServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            updateNoteList()
            self.path = 'userhome.html'
        return HttpServer.SimpleHTTPRequestHandler.do_GET(self)
    def do_POST(self):
        if self.path == '/edit':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            filename = self.headers['File']
            openFile = open(filename, "w")
            content = str(post_data)[2:]
            content = content[:len(content)-1]
            content = content.split("\\n")
            i=0
            openFile.write("")
            openFile = open(filename, "a")
            while i<len(content):
                openFile.write(content[i]+"\n")
                i+=1
            openFile.close()
            self.send_response(200)
            self.wfile.write(bytes("Accepted", "utf-8"))
            convertToHTML(filename)
        if self.path == '/newFile':
            filename = self.headers['File']
            newFile = open(filename, "x")
            newFile.close()
            filename = filename.replace("txt", "html")
            newFile = open(filename, "x")
            newFile.close()
            updateNoteList()

handler_object = MyHttpRequestHandler

PORT = 8001
my_server = socketserver.TCPServer(("", PORT), handler_object)

print("Visit http://localhost:"+str(PORT))

my_server.serve_forever()
