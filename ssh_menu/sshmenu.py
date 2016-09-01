#!/usr/bin/python
#coding=utf8
"""
# Author: Bill
# Created Time : 2016-08-31 18:20:06

# File Name: w.py
# Description:

"""
from snack import *
import time, sys, os
import ConfigParser
import sys, getopt

version = '$Id: sshmenu.py 1.0.1 $'

def menuhostlist(screen, defaultitem = 0):
    global _hostlistcfgfile
    lbcw = []
    listitem = []

    Config = ConfigParser.ConfigParser()
    cfgfile = Config.read(_hostlistcfgfile)
    if cfgfile == []:
        screen.finish()
        print "hostlist.cfg not found!"
        sys.exit(1)
    configsections = sorted(Config.sections())

    for item in configsections:
        if Config.has_option(item, 'description'):
            vmdescription  = Config.get(item, 'description')
            listitem.append(item.ljust(20) + " " + vmdescription)
        else:
            listitem.append(item.ljust(20))

    lbcw = ListboxChoiceWindow(screen, 'Hostlist',
                    'Choose Target for SSH-Connection:',
                    listitem, default = defaultitem)

    # We start the ssh-session only when None or OK is returned.
    # a simple 'return' on the list give None and is ok in this situation
    if lbcw[0] in (None, 'ok'):
        sshhost = Config.get(configsections[lbcw[1]], 'hostname')
        sshuser = Config.get(configsections[lbcw[1]], 'username')
        sshport = Config.get(configsections[lbcw[1]], 'hostport')
        screen.suspend()
        oscmd = "ssh -p %s %s@%s" %(sshport,sshuser, sshhost)
        os.system(oscmd)
        screen.resume()
        menuhostlist(screen, lbcw[1])

def listhost():
    global _hostlistcfgfile
    listitem = []
    Config = ConfigParser.ConfigParser()
    cfgfile = Config.read(_hostlistcfgfile)
    if cfgfile == []:
        screen.finish()
        print "hostlist.cfg not found!"
        sys.exit(1)
    configsections = sorted(Config.sections())

    for item in configsections:
        print "[%s]"%item
        sshhost = Config.get(item, 'hostname')
        sshuser = Config.get(item, 'username')
        print "%s@%s"%(sshuser,sshhost)


_hostlistcfgfile = '%s/hostlist.cfg'%os.path.split(os.path.realpath(__file__))[0]

if len(sys.argv) == 2:
    opts, args = getopt.getopt(sys.argv[1:], "h")
    for op, value in opts:
        if op == "-h":
            listhost()
else:
    screen = SnackScreen()
    menuhostlist(screen)
    screen.finish()
