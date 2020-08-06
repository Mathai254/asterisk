import xml.etree.ElementTree as ET
tree = ET.parse('/home/samuel/Desktop/KO/modified.xml') # Path to downloaded file from 3CX
root = tree.getroot()


for Contact in root.findall('Contact'):
	DirectoryEntry = ET.Element("DirectoryEntry")
	Name = ET.Element("Name")
	Telephone = ET.Element("Telephone")
	name = Contact.find('Name').text
	tel = Contact.find('Telephone').text
	Name.text = str(name)
	Telephone.text = str(tel)

	DirectoryEntry.append(Name)
	DirectoryEntry.append(Telephone)
	root.append(DirectoryEntry)
	root.remove(Contact)


root.tag = 'AsteriskIPPhoneDirectory'

tree.write('mod.xml')
