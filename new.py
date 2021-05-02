from subprocess import Popen

a = open("Log")

if 'Dark-Killer.zip' in a.read():
  Popen(("unzip","Dark-Killer.zip"),stderr=None,stdout=None)
  print('\n [ Successfully extracted ]')
  Popen(("rm","Run.py"),stderr=None,stdout=None)
  Popen(("rm","Dark-Killer.zip"),stderr=None,stdout=None)
  Popen(("rm","Log"),stderr=None,stdout=None)
  Popen(("rm","new.py"),stderr=None,stdout=None)
  