import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">
    +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text) # find() the tag 'name' from the tree. .text get the data
print('Attr:', tree.find('email').get('hide')) # get() require the attribute 'hide'
