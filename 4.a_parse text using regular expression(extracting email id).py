#extracting email id using findall 
import re
doc = "For more details please mail us at: xyz@abc.com,pqr@mno.com"
addresses = re.findall(r'[\w\.-]+@[\w\.-]+', doc)
for address in addresses:
    print(address)
