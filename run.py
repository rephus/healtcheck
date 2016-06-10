#!/usr/bin/python
import requests
import time
import sys
import ConfigParser

# Global variables
todayDate=time.strftime("%Y/%m/%d")
todayHour=time.strftime("%H:%M:%S")

# Check status
def check (service, url,content):

  start = time.time()
  print "Checking "+service
  valid = contains(url,content)
  print "* Request took {} seconds ".format(int(time.time() - start))
  if not valid:
      error = "'"+url+"' doesn't contain '"+content+"'"
      print "* Service "+service+" check FAILED at "+todayDate+" "+todayHour +": " +error
      subject="Service "+service+" DOWN"
      message="Service "+service+" failed at "+todayDate+" "+todayHour +":\n\n"+error
      sys.exit(1)
  else:
      print "* OK"

def contains (url, content):
  for r in range(retry) :
    try:
        text =  requests.get(url, timeout = timeout).text
        exist = text.find(content) != -1
        if not exist:
          if debug: print """* URL '{}':
          ** expected '{}'
          ** got '{}'""".format(url,content,text.encode('utf8'))
        return exist
    except Exception as error:
        print "* ({}) Error in '{}': {}".format(r,url,error)
  return False

# Main
print "Running checkHealth script at "+todayDate+" "+todayHour+"\n"

# Load config
config = ConfigParser.ConfigParser()
config.read("config.cfg")
timeout = int (config.get('config', 'timeout') )
debug = config.get('config', 'debug') == 'true'
retry = int (config.get('config', 'retry'))

servers = config.items("servers")

for server in servers:
  service = server[0]
  values = server[1].split(",")
  endpoint = values[0]
  content = values[1]
  check(service,endpoint,content)

print "\nCheckHealth script ended without errors \n"

sys.exit(0)
