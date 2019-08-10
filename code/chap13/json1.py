import json

#json as dict
# data = '''
#     {
#       "name" : "Chuck",
#       "phone" : {
#         "type" : "intl",
#         "number" : "+1 734 303 4456"
#        },
#        "email" : {
#          "hide" : "yes"
#        }
#     }
# '''

#json as list which has dict
data = '''
[
    {
      "name" : "Chuck",
      "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
       },
       "email" : {
         "hide" : "yes"
       }
    }
]
'''

info = json.loads(data)
# print('Name:',info["name"])
# print('Hide:',info["email"]["hide"])

for item in info:
    print('Name:',item["name"])
    print('Hide:',item["email"]["hide"])
