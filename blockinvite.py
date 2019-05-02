# -*- coding: utf-8 -*-
#SELFBOT AUTOBLOCK SPAM By @teambotprotect
#THAKS FOR ALL TEAM BOTS
from TBP.linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,timeit,atexit
from time import strftime
#==================================================================================================================#
dz = LINE("")
dz.log("Auth Token : " + str(dz.authToken))
dzMID = dz.profile.mid
botStart = time.time()
oepoll = OEPoll(dz)
Dhenza = [dzMID,"ub1c5a71f27b863896e9d44bea857d35b"]
#==================================================================================================================#
def restartBot():
    print ("[ Info ] Bot Restart")
    python = sys.executable
    os.execl(python, python, *sys.argv)
def logError(text):
    me.log("[ Error ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@dhenza15 "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mid")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    dz.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
#==================================================================================================================#
def dhenzaBots(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            sendMention(op.param1, " @! Makasih sudah invite",[op.param1])
            sendMention(op.param1, " @! Maaf weh Auto block on pc ae",[op.param1])
            dz.blockContact(op.param1)
        if op.type == 6:
            contact = dz.getContact(op.param1)
            print ("[ 6 ] {} has been blocked".format(contact.displayName) + " Mid: " + contact.mid )
        if op.type == 13:
            if dzMID in op.param3:
               group = dz.getGroup(op.param1)
               inviter= dz.getContact(op.param2)
               print ("[ 13 ] " + inviter.displayName + " invite you" + str(group.name))
               if str(group.name).lower() in ["tes","spam","js","cupu","desah","asu"]:
                  dz.rejectGroupInvitation(op.param1)
               elif len(group.members) < 5:
                  dz.rejectGroupInvitation(op.param1)
        if op.type == 21 or op.type == 22 or op.type ==24:
            print ("[ NOTIFY LEAVE ROOM ]")
            dz.leaveRoom(op.param1)
        if (op.type == 25 or op.type == 26) and op.message.contentType == 0:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != me.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if 'ORGCONTP' in msg.contentMetadata.keys()!= None and msg.contentMetadata['ORGCONTP'] == "CALL":
                if msg.contentMetadata['GC_EVT_TYPE'] == "I":
                    dz.sendMessage(sender, "DON'T INVITE ME GROUP CALL")
                    dz.blockContact(sender)
            if sender in Dhenza:
                if text.lower() in ['speed','sp']:
                    dz.sendReplyMessage(msg.id, to,"About"+str(timeit.timeit('"-".join(str(n) for n in range(100))',number=1000)) + "secs")
                elif text.lower() == 'help':
                	  dz.sendReplyMessage(msg.id, to, "🔖Menu Selfbot \n🕷•Me \n🕷•Sp \n🕷•Runtime \n🕷•Restart")
                elif text.lower() == 'runtime':
                       dz.sendReplyMessage(msg.id, to, "System run {}".format(str(format_timespan(time.time() - botStart))))
                elif text.lower() in ['me']:
                	   dz.sendContact(to,sender);dz.sendMessageMusic(to, title=dz.getContact(sender).displayName, subText=str(dz.getContact(sender).statusMessage), url='line.me/ti/p/~teambotprotect', iconurl="http://dl.profile.line-cdn.net/{}".format(dz.getContact(sender).pictureStatus), contentMetadata={})
                elif text.lower() == 'restart':
                       dz.sendReplyMessage(msg.id, to, "Please wait for Restart...")
                       restartBot()
    except Exception as error:
        logError(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                dhenzaBot(op)
                oepoll.setRevision(op.revision)
    except:
        pass
        
        
