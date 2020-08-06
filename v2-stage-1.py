import xml.etree.ElementTree as ET
tree = ET.parse('/home/samuel/Desktop/KO/kocontacts.xml') # Path to downloaded file from 3CX
root = tree.getroot()


for Contact in root.findall('Contact'):
	fname = Contact.find('FirstName').text
	lname = Contact.find('LastName').text
	pnumber = Contact.find('Phone')
	phoneno = pnumber.find('phonenumber').text
	#print(phoneno)
	Name = ET.Element("Name")
	Name.text = str(lname) +" "+str(fname)
	#print(Name.text)
	Contact.append(Name)
	Telephone = ET.Element("Telephone")
	Telephone.text = str(phoneno)
	Contact.append(Telephone)

	Contact.remove(Contact.find('FirstName'))
	Contact.remove(Contact.find('LastName'))
	Contact.remove(Contact.find('Phone'))

tree.write('modified.xml') # Name of the modified xml contact list
