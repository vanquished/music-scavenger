#Music Scavenger
#Written by Joseph Tennant

#uses
import urllib
import sys
#init vars
line = 0
songline = []
song = sys.argv[1]
artist = sys.argv[2]
query = "http://www.ultimate-guitar.com/search.php?title="+song+" "+artist+"&type%5B2%5D=300&page=1&tab_type_group=text&app_name=ugt&order=myweight&rating%5B0%5D=4&rating%5B1%5D=5"
#Begin
print query
open_url = urllib.urlopen(query)
data = open_url.read()
f = open("urlfile", "w+r")
f.seek(0)
f.truncate()
f.write(data)

#not working
for line in f:
    if 'song' in line:
        songline.append(line)
print line
f.close()
print songline
