from subprocess import Popen


with open("Log","w") as var:
  
  Popen(("ls"),stderr=var,stdout=var)


Popen(("python","new.py"),stderr=None,stdout=None)
