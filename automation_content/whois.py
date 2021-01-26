from jnpr.junos import Device
import sys
dev=Device(host=sys.argv[1], user="root", password="Embe1mpls")
dev.open()
#message=dev.facts["hostname"]+ " is an " + dev.facts['model'] + " running " + dev.facts["version"]
print (dev.facts["hostname"]+ " is an " + dev.facts['model'] + " running " + dev.facts["version"])
dev.close()
#from slacker import Slacker
#slack = Slacker('xoxp-89396208643-89446660672-98529286339-0e5407813326b0e6c079b06d9f87a6f8')
#slack.chat.post_message('#general', message, username='j-bot')

