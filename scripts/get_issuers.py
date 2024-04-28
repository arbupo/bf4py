import re
import json
from datetime import date

from bf4py import BF4Py

mic = 'XFRA'
bf4py = BF4Py(default_mic=mic) 
search_dict = bf4py.bonds.search_parameter_template()
search_dict['currencies'].append('USD')
result = bf4py.bonds.search(params=search_dict)

issuers = []
for bond_object in result:
    bond_title = bond_object['name']['originalValue']
    issuer = re.match(r'^.*?(?=\d)', bond_title).group(0)
    if issuer not in issuers and issuer != "":
        issuers.append(issuer)

issuers_list = [{'issuer': issuer} for issuer in issuers]

with open('issuers.json', 'w') as file:
    file.write(json.dumps(issuers_list, indent=4))
