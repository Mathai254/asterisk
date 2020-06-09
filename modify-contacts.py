import xml.etree.ElementTree as ET
tree = ET.parse('/path_to_file/file_name.xml') # Path to downloaded file from 3CX
root = tree.getroot()


for DirectoryEntry in root.findall('DirectoryEntry'):
	fname = DirectoryEntry.find('FirstName').text
	lname = DirectoryEntry.find('LastName').text
	#print(fname, lname)
	Name = ET.Element("Name")
	Name.text = str(lname) +" "+str(fname)
	#print(Name.text)
	DirectoryEntry.append(Name)

	DirectoryEntry.remove(DirectoryEntry.find('FirstName'))
	DirectoryEntry.remove(DirectoryEntry.find('LastName'))

tree.write('modified.xml') # Name of the modified xml contact list
