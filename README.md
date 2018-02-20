# BuildSuccessful

It is a python script which automates the process of `gradle assemble` and `apk push via adb` along with `slack notification`


`Please note that this app has still not been released in the public domain, so you may not be able to use this at the moment`



### Setting up the project

1. First install `python 2.7` and clone this project.
Then make these initialisations:

```projectPath = "/your/project/path"
targetBuildName = "yourTargetBuildName"
buildModifierOffline = "--offline" 
apkOutputPath = "/Your/apk/output/path/myapp.apk"
webHookUrl = "http://hooks.slack.com/services/something-secretkey"
```


2. Then go to the url (provided in the group). 
In the features section, select incoming webhooks :

[![N|Solid](https://github.com/abhinav-adtechs/BuildSuccessful/blob/master/screenshots/features.png)](Image1)



3. Next, add a new webhook:


[![N|Solid](https://github.com/abhinav-adtechs/BuildSuccessful/blob/master/screenshots/add-webhooks.png)](Image2)

4. Finally copy the webHook url and paste it in initialisations:

```
webHookUrl = "http://hooks.slack.com/services/something-secretkey"
```
DONE! From next time just run the following code

```
python script.py
```

### Todos

 - Put app for production with custom url modification.
 - Add slackbot conversational allowance for getting gradle build percentage. 


### Development

Want to contribute? Great!

License
----

MIT

