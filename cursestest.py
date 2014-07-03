#!/usr/bin/env python

from os import system
import curses
import subprocess

def get_param(prompt_string):
    screen.clear()
    screen.border(0)
    screen.addstr(2, 2, prompt_string)
    screen.refresh()
    input = screen.getstr(10, 10, 60)
    return input

def execute_cmd(cmd_string):
    system("clear")
    a = system(cmd_string)
    print ""
    if a == 0:
        print "Command executed correctly"
    else:
        print "Command terminated with error"
    raw_input("Press enter")
    print ""

def cli(string):
    cmd = subprocess.Popen(string.split(),
			   stdout=subprocess.PIPE,
			   stderr=subprocess.PIPE,
			  )
    output, error = cmd.communicate()
    print error
    return output
x = 0

try:
    import requests
except:
    cli("pip install requests")
    import requests


while x != ord('8'):
    screen = curses.initscr()

    screen.clear()
    screen.border(0)
    screen.addstr(2, 2, "Please enter a number...")
    screen.addstr(4, 4, "1 - Add a user")
    screen.addstr(5, 4, "2 - Restart Apache")
    screen.addstr(6, 4, "3 - Show disk space")
    screen.addstr(7, 4, "4 - Add new vhost")
    screen.addstr(8, 4, "5 - Show active vhosts/domains")
    screen.addstr(9, 4, "6 - run apache buddy")
    screen.addstr(10, 4, "7 - Run Mysqltuner")
    screen.addstr(11, 4, "8 - Exit")
    screen.refresh()

    x = screen.getch()

    if x == ord('1'):
        username = get_param("Enter the username")
        homedir = get_param("Enter the home directory, eg /home/nate")
        groups = get_param("Enter comma-separated groups, eg adm,dialout,cdrom")
        shell = get_param("Enter the shell, eg /bin/bash:")
        curses.endwin()
        execute_cmd("useradd -d " + homedir + " -g 1000 -G " + groups + " -m -s " + shell + " " + username)
    if x == ord('2'):
        curses.endwin()
        execute_cmd("service httpd restart")
    if x == ord('3'):
        curses.endwin()
        execute_cmd("df -h")
    if x == ord('4'):
            curses.endwin()
            domain = get_param("Enter the domain name you want to add")
            r=requests.get("http://justcurl.com/", headers={"host":domain})

            c = r.content
            #p=c.find("]",c.find("/etc/apache2/sites-enabled/"))-1
            #c = c[:p] + ".conf" + c[p:]
            #p=c.find("]",c.find("/etc/apache2/sites-available/",p))-1
            #c = c[:p] + ".conf" + c[p:]
            #p=c.find("&",c.find("/etc/apache2/sites-available/",p))-1
            #c = c[:p] + ".conf" + c[p:]
            #p=c.find("/",c.find("/etc/apache2/sites-available/",p))-1
            #c = c[:p] + ".conf" + c[p:]

            outfile=open("somescript.sh", "w")

            outfile.write(c)
            outfile.close()
            #cmd = subprocess.Popen("sh ./somescript.sh".split(),
            #                       stdout=subprocess.PIPE,
            #                       stderr=subprocess.PIPE,
            #                      )
            #output, error = cmd.communicate()
            #print output
            #print error
            o = cli("sh ./somescript.sh")
            print o

    if x == ord('5'):
        curses.endwin()
        execute_cmd("httpd -S 2>/dev/null |grep 80")
    if x == ord('6'):




	curses.endwin()
        a = cli("curl -s http://cloudfiles.fanatassist.com/apachebuddy.pl")
        outfile=open("apachebuddy.pl", "w")
        outfile.write(a)
        outfile.close()

        print cli("perl ./apachebuddy.pl")

       # print cli("perl <( curl -s http://cloudfiles.fanatassist.com/apachebuddy.pl )")
       # a = sh.curl("-s", "http://cloudfiles.fanatassist.com/apachebuddy.pl")
       # b = sh.perl(a)i

    if x == ord('7'):
        curses.endwin()
        cli("wget https://raw.githubusercontent.com/major/MySQLTuner-perl/master/mysqltuner.pl -O /tmp/mysqltuner.pl")
        print cli("perl /tmp/mysqltuner.pl")





curses.endwin()
