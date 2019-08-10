import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''
#users is the list of user
stuff = ET.fromstring(input)
lst = stuff.findall('users/user') # take the tag 'user' list under the 'users'
print('User count:', len(lst)) # length of list lst

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))
