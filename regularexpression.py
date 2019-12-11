import re

pattern = r'\w+@\w+\.\w+'

sequence ='ranjanlamsal19@gmail.com abc@gmail.com ran@gmail.com'


if re.match(pattern, email):
    print('Email is valid.')
else:                         
    print('invalid email.')
    
# print(re.match(pattern, sequence))
#match le space samma matra match garxa bt re.findall le chai sabai possible display garxa
# print(re.findall(pattern, sequence))