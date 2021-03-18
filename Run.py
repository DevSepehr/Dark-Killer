import sys
from subprocess import Popen
try:
  Popen(("unzip","Dark-Killer.zip"),stderr=None,stdout=None)
  Popen(("rm","Dark-Killer.zip"),stderr=None,stdout=None)
except:
  os.system("clear")
  print("\n [!] You have already done so now type the following command : \n >> python Dark-Killer.py")
  sys.exit()
