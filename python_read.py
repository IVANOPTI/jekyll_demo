text_file=open("access.log","r")
entire_file=text_file.readlines()
text_file.close

print "<!DOCTYPE html>"
print "<html>"
print "<title>Python Test</title>"
print "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\"/>"
print "<head>"
print "<style></style>"
print "</head>"
print "<body>"
print "<table>"
print "<tr><td>IP</td><td>Date</td><td>Action</td></tr>"

loged=set()
for line in reversed(entire_file):
    try:
	arr=linarr = line.split(' ')
	date = arr[3]
	matchIP = arr[0]
	matchDate = date[1:]
	matchAct = arr[6]
	if( matchIP,matchDate,matchAct)not in loged:
	     print "<tr><td>", matchIP, "</td><td>", matchDate, "<td></td>", matchAct, "</td></tr>" 
	else:
	    continue  
    except IndexError,e:
	error=e

print "</table>"
print "</body>"
print "</html>"
