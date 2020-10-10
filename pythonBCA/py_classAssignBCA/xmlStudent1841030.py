import xml.etree.ElementTree as ET
myTree = ET.parse('data.xml')

#Checking the Root Tag
myroot = myTree.getroot()
print(myroot.tag)

for x in myroot.findall('Student'):
    id = x.find('id').text #convert data to text
    name = x.find('name').text
    course = x.find('program').text
    grade  = x.find('grade').text
    
    print('\n')
    print('ID       : {}\n'.format(id))
    print('NAME     : {}\n'.format(name))
    print('COURSE   : {}\n'.format(course))
    print('GRADE    : {}\n'.format(grade))

idget     = input('ID :')
nameget   = input('Name :')
courseget = input('Course :')
gradeget  = input('Grade  :')

child=ET.Element("Student") #added tags tudent
myroot.append(child)

#Data get saved here
id = ET.SubElement(child,'id')
id.text = idget
nm = ET.SubElement(child, "name")
nm.text = nameget
program = ET.SubElement(child, "program")
program.text = courseget
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
