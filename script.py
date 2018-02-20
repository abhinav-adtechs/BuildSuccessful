#!/usr/bin/env python


import os
import subprocess
import sys
import requests
import datetime


############################# I N I T I A L I S A T I O N S #############################

projectPath = "/your/project/path"

targetBuildName = "yourTargetBuildName"
buildModifierOffline = "--offline"

apkOutputPath = "/Your/apk/output/path/myapp.apk"

webHookUrl = "http://hooks.slack.com/services/something-secretkey"

#######################################################################################



def startBuildProcess():

    os.chdir(projectPath)

    '''Use this if you get an error saying permission denied'''
    #test = subprocess.Popen(["chmod","+x","gradlew"], stdout=subprocess.PIPE)

    p = subprocess.Popen(['./gradlew', buildModifierOffline, targetBuildName], stdout=subprocess.PIPE)
    
    while True:
        line = p.stdout.readline()
        if line != b'':
            os.write(1, line)
        else:
            break

    p.kill()

    messageToPost = "Successful build of " + targetBuildName + " at " + datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y") + ". Pushing apk via ADB."
    postToSlack(messageToPost)


def startApkPushProcess():
    p = subprocess.Popen(['adb', 'install', '-r', apkOutputPath], stdout=subprocess.PIPE)
    print "Please note that the default timeout for ADB is 5 minutes. Thanks!"

    while True:
        line = p.stdout.readline()

        if line != b'':
            os.write(1, line)
        else:
            break

    p.kill()
    postToSlack("Apk installed or Device not available!")


def postToSlack(messageToPost):

    payload = {
        "text": messageToPost
    }
    headers = {
        'Content-type': "application/json",
        'Cache-Control': "no-cache",
    }

    response = requests.request("POST", webHookUrl, data=str(payload), headers=headers)

    print response.text + " POSTED ON SLACK"




if __name__ == "__main__":
    startBuildProcess()
    startApkPushProcess()