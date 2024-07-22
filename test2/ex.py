

import os
import re

str1 = os.system("ifconfig")

'''f = open("ifconfig.txt","w")

f.write(str(str1))

f.close()

pattern = "*inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"

x = re.search(pattern,str(str1))

print(x)'''
print(str1)
