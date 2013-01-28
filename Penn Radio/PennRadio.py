#Tagging on these suck. If anyone is reading this, let me know and 
#I'll send you a collection of properly organized and consistently 
#tagged MP3s. Or you can take an hour and do it yourself in EasyTag
#like I did, but the first option is easier.

import xml.etree.ElementTree as ET
import urllib
import time

tree = ET.parse("Penn_Radio_archive_files.xml")
root = tree.getroot()
files = root.findall('file')
base_path = "http://ia600209.us.archive.org/13/items/Penn_Radio_archive/"

for child in root.findall('file'):
    filename = child.attrib['name']
    url = base_path + filename

    print "Downloading %s..." % filename
    urllib.urlretrieve (url, filename)

    time.sleep(10)