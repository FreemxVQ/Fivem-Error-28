from tkinter import messagebox
from secrets import token_hex
import subprocess , tempfile,os
import os
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import subprocess
from subprocess import call
from tkinter import * 
from tkinter import messagebox
from colorama import Fore, Style
import getpass

import webbrowser
from tkinter.messagebox import showerror
import os
from pathlib import Path
import subprocess
from tkinter import *
from pathlib import Path
from tkinter import Tk, Canvas, END, Text, Button, PhotoImage,messagebox,sys
import subprocess
import requests
import pyperclip
from tkinter import *
import base64
from psutil import NoSuchProcess, AccessDenied, ZombieProcess, process_iter
from threading import Thread
from multiprocessing import cpu_count
from ctypes import windll
from os import _exit as close
import sys

if windll.shell32.IsUserAnAdmin() == False:
        showerror("โปรแกรม", "แจ้งเตือน: กรุณารันแอดมินเพื่อใช้งาน.")
        close(0)
call("netsh advfirewall set allprofiles state on >NUL", shell = True)
call("netsh advfirewall firewall delete rule name=\"LagSwitch\" >NUL", shell = True)

class AntiDebug(Thread):
    def __init__(self):
        self.debigging = True

        Thread.__init__(self)

    def detect_vm(self):
        if (hasattr(sys, 'real_prefix')):
            sys.exit(0)

    def detect_core(self):
        if (cpu_count() == 1):
            sys.exit(0)

    def check_for_process(self):
        for proc in process_iter():
            try:
                for name in ['proxifier', 'graywolf', 'extremedumper', 'zed', 'exeinfope', 'dnspy', 'ilspy', 'titanhide', 'x32dbg', 'codecracker', 'simpleassembly', 'process hacker 2', 'pc-ret', 'http debugger', 'Centos', 'process monitor', 'debug', 'reverse', 'simpleassemblyexplorer', 'de4dotmodded', 'dojandqwklndoqwd-x86', 'sharpod', 'folderchangesview', 'fiddler', 'die', 'pizza', 'crack', 'strongod', 'ida -', 'brute', 'dump', 'StringDecryptor', 'wireshark', 'debugger', 'httpdebugger', 'gdb', 'kdb', 'x64_dbg', 'windbg', 'x64netdumper', 'petools', 'scyllahide', 'megadumper', 'reversal', 'ksdumper v1.1 - by equifox', 'dbgclr', 'HxD', 'monitor', 'peek', 'ollydbg', 'ksdumper', 'http', 'wpe pro', 'dbg', 'httpanalyzer', 'httpdebug', 'PhantOm', 'kgdb', 'james', 'x32_dbg', 'proxy', 'phantom', 'mdbg', 'WPE PRO', 'system explorer', 'de4dot', 'x64dbg', 'protection_id', 'charles', 'systemexplorer', 'pepper', 'hxd', 'procmon64', 'MegaDumper', 'ghidra', 'xd', '0harmony', 'dojandqwklndoqwd', 'hacker', 'process hacker', 'SAE', 'mdb', 'checker', 'harmony', 'Protection_ID', 'x96dbg', 'systemexplorerservice', 'folder', 'mitmproxy', 'dbx', 'sniffer', 'regmon', 'diskmon', 'procmon', 'http', 'traffic', 'packet', 'debuger', 'dbg', 'ida', 'dumper', 'pestudio', 'hacker', "vboxservice.exe","vboxtray.exe","vmtoolsd.exe","vmwaretray.exe","vmwareuser","VGAuthService.exe","vmacthlp.exe","vmsrvc.exe","vmusrvc.exe","prl_cc.exe","prl_tools.exe","xenservice.exe","qemu-ga.exe","joeboxcontrol.exe","joeboxserver.exe","joeboxserver.exe"]:
                    if name.lower() in proc.name().lower():
                        try:
                            proc.kill()
                        except: sys.exit(0)
            except (NoSuchProcess, AccessDenied, ZombieProcess):
                sys.exit(0)

    def check_for_debugger(self):
        if (windll.kernel32.IsDebuggerPresent() != 0 or windll.kernel32.CheckRemoteDebuggerPresent(
                windll.kernel32.GetCurrentProcess(), False) != 0):
            sys.exit()

    def detect_screen_syze(self):
        if (windll.user32.GetSystemMetrics(0) <= 200 or windll.user32.GetSystemMetrics(1) <= 200):
            sys.exit()

    def run(self):
        self.detect_screen_syze()
        self.detect_core()
        self.detect_vm()

        while self.debigging:
            self.check_for_process()
            self.check_for_debugger()

def mess():
  os.system("cls & title Windows & mode 15,1")
  messagebox.showinfo("โปรแกรม", "ยินดีต้อนรับสู่โปรแกรมแก้เข้าเกมไม่ได้นะครับ \n \n เพราะมึงรันของเยอะไปไหนเน็ตพวกมึงเลยเป็นแบบนึ้ 5555 \n\nแต่กูไม่ดักนะห้ามเกะโปรแกรม อิอิ  เช็คได้ค้าบ ")
  main()
def main():
    os.system("cls & title Windows & mode 55,21") # ความกว้่างของ Ui ของต่อย
    print(Fore.LIGHTBLUE_EX, '''
       ███████╗██╗██╗   ██╗███████╗███╗   ███╗
       ██╔════╝██║██║   ██║██╔════╝████╗ ████║
       █████╗  ██║██║   ██║█████╗  ██╔████╔██║
       ██╔══╝  ██║╚██╗ ██╔╝██╔══╝  ██║╚██╔╝██║
       ██║     ██║ ╚████╔╝ ███████╗██║ ╚═╝ ██║
       ╚═╝     ╚═╝  ╚═══╝  ╚══════╝╚═╝     ╚═╝
     ''')                                                                                                                                                   
    print(Fore.LIGHTCYAN_EX, '''
      ╔══════════════════════════════════════╗   
      ║                                      ║
      ║       [1] : Restart  internet        ║
      ║                                      ║
      ║       [2] : Follow me                ║
      ║                                      ║
      ║       [3] : EXIT                     ║
      ║                                      ║
      ╚══════════════════════════════════════╝  
      ''')
    print(Fore.LIGHTRED_EX,'')
    Nomsod = input("RUN : ")

    if Nomsod == "1":
        os.system("cls & title Enter 1 & mode 55,21")
        os.system('cls')
        file_location = os.path.join(tempfile.gettempdir(), f"virus{token_hex(16)}.bat")
        open(file_location, 'wb').write(bytes('''
        echo 
        netsh winsock 
        cls
        netsh int ipv4 reset
        cls
        netsh int ipv6 reset
        cls
        netsh int tcp reset
        cls
        ipconfig /flushdns
        cls
        ipconfig /renew
        cls
        ipconfig /release
        cls
        ipconfig /flushdns
        cls
        ipconfig /release
        cls
        ping localhost -n 1 >nul
        cls
        ipconfig /renew
        cls
        netsh int ip reset
        cls
        netsh winsock reset
        cls
        ''', 'utf-8'))
        subprocess.run(['attrib', '+h', file_location])
        subprocess.run([file_location])
        os.remove(file_location) 
        messagebox.showinfo("โปรแกรม", "เริ่มใช้งานแล้วนะ\n")
        main()

    if Nomsod == "2": 
        os.system('cls')
        os.system("cls & title Menu 2 & mode 55,21")
        print(Fore.LIGHTBLUE_EX, '''
    ███████╗ ██████╗ ██╗     ██╗     ██╗    ██╗
    ██╔════╝██╔═══██╗██║     ██║     ██║    ██║
    █████╗  ██║   ██║██║     ██║     ██║ █╗ ██║
    ██╔══╝  ██║   ██║██║     ██║     ██║███╗██║
    ██║     ╚██████╔╝███████╗███████╗╚███╔███╔╝
    ╚═╝      ╚═════╝ ╚══════╝╚══════╝ ╚══╝╚══╝ 
        ''')                                                                                                                                                   
        print(Fore.LIGHTCYAN_EX, '''
        ╔══════════════════════════════════════╗   
        ║                                      ║
        ║       [1] : Discord                  ║
        ║                                      ║
        ║       [2] : Facebook                 ║
        ║                                      ║
        ║       [3] : youtube                  ║
        ║                                      ║
        ╚══════════════════════════════════════╝  
        ''')
        print(Fore.LIGHTRED_EX,'')
        Menu = input("RUN : ")

        if Menu == "1":  
            webbrowser.open("https://discord.gg/9hbTfaFRpY", new=1) 
            main()
        if Menu == "2":  
            webbrowser.open("https://www.facebook.com/search/top?q=%E0%B9%84%E0%B8%A1%E0%B9%88%E0%B8%9A%E0%B8%AD%E0%B8%81", new=1) 
            main()
        if Menu == "3":  
            webbrowser.open("https://www.youtube.com/channel/UCVKtx45LlkOYYQeVGagI0ZQ", new=1) 
            main()
        else:
            messagebox.showerror("กรอกผิด", "กรุณาเขียนให้ถูกนะครับ/คะ")
            main()
    if Nomsod == "3":  
        quit()
    else:
        messagebox.showerror("กรอกผิด", "กรุณาเขียนให้ถูกนะครับ/คะ")
        main()

mess()

