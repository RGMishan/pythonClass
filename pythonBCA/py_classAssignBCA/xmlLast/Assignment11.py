import xml.etree.ElementTree as ET

tree = ET.parse('detail.xml')
root = tree.getroot()

for x in root.findall('Student'):
    i =x.find('name').text
    e = x.find('program').text
    print(i, e)

for grade in root.iter('grade'):
    new_desc = str(grade.text)+'+'
    grade.text = str(new_desc)
    grade.set('updated', 'yes')

tree.write('new.xml')
