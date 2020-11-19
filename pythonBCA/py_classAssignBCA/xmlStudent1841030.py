import xml.etree.ElementTree as ET
myTree = ET.parse('data.xml')

#Checking the Root Tag
myroot = myTree.getroot()
print(myroot.tag)

for x in myroot.findall('Doctor'):
    id = x.find('id').text #convert data to text
    name = x.find('name').text
    spec = x.find('spec').text
    login  = x.find('login').text
    password  = x.find('password').text
    
    print('\n')
    print('ID       : {}\n'.format(id))
    print('NAME     : {}\n'.format(name))
    print('SPECIALIZATION   : {}\n'.format(spec))
    print('LOGIN    : {}\n'.format(login))
    print('PASSWORD    : {}\n'.format(password))

idget     = input('ID :')
nameget   = input('Name :')
specget = input('Specialization :')
loginget  = input('Login  :')
passwordget  = input('Password  :')

child=ET.Element("Doctor") #added tags tudent
myroot.append(child)

#Data get saved here
id = ET.SubElement(child,'id')
id.text = idget
nm = ET.SubElement(child, "name")
nm.text = nameget
program = ET.SubElement(child, "program")
program.text = specget
grade=ET.SubElement(child, "grade")
grade.text= gradeget

#Insert into our data file
myTree.write('data.xml')

idEmp     = input('ID :')
nameEmp   = input('FullName :')
salaryEmp = input('Salary :')
designationEmp  = input('YearofExperience  :')

child=ET.Element("Employee")
myroot.append(child)

id = ET.SubElement(child,'ID')
id.text = idEmp
nm = ET.SubElement(child, "FullName")
nm.text = nameEmp
program = ET.SubElement(child, "Salary")
program.text = salaryEmp
grade=ET.SubElement(child, "YearofExperience")
grade.text = designationEmp

myTree.write('data.xml')


# for grade in myroot.iter('id'):  
#     print("\nThe ID present are:\n")  
#     print(grade.text)
