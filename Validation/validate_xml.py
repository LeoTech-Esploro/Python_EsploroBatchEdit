import xmlschema
schema = xmlschema.XMLSchema("C:\\Users\\sean1\\Desktop\\Sean Costello\\School\\University of La Verne\\Senior Year\\Spring Semester\\CMPS 471- Internship\\Wilson Library\\Project4\\Validation\\rest_user.xsd")
schema.validate("C:\\Users\\sean1\\Desktop\\Sean Costello\\School\\University of La Verne\\Senior Year\\Spring Semester\\CMPS 471- Internship\\Wilson Library\\Project4\\XML_Output.xml")
print("Validation successful")
