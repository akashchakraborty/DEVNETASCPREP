#!/usr/bin/env python
"""Working with nested data hands-on exercise / coding challenge."""


import json
import os
from pprint import pprint


# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, "interfaces.json")) as file:

    #TODO: Parse the contents of the JSON file into a variable
    json_text=file.read()

json_data=json.loads(json_text)
print("<==>")
# TODO: Loop through the interfaces in the JSON data and print out each
# interface's name, ip, and netmask.
data=json_data["ietf-interfaces:interfaces"]["interface"]
for i in data:
    print("Interface name: {}\nIPv4 Address: {}\nNetmask: {}".format(i['name'],i['ietf-ip:ipv4']['address'][0]['ip'],i['ietf-ip:ipv4']['address'][0]['netmask']))
    print("")
