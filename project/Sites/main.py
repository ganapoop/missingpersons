import tweepy
import json
from keys import keys
import unicodedata
import datetime
import sys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
no_frauds = {}

currentTime = str(datetime.datetime.now().date())
#print currentTime

# pull tweets about missing people
twts = api.search(q='#missingperson', count='49')
# twts2 = api.search(q='#missing', count='1000')
# twts3 = api.search(q='#missingpeople', count='1000')

file = open("locations.json", 'w')
file.write("{\n\t\"Points\":\n\t\t[\n")

def write_data_to_file(file, data, first):
	for s in data:
	#print(s)
		if s not in no_frauds:
			no_frauds[s.text] = 1
			unicode_str = s.text
			text = unicodedata.normalize('NFKD', unicode_str).encode('ascii','ignore')
			#print(type(text))
			tweet = text.split()
			#print(tweet)
			# tweet = list(str(s.text))
			# print(tweet)
			#user_place = unicodedata.normalize('NFKD', s.user.location).encode('ascii','ignore')
			#post_place = unicodedata.normalize('NFKD', s.user.location).encode('ascii','ignore')
			if (tweet[0] != 'RT') and (s.place != None or s.user.location != ""):
				loc = s.place.full_name if (s.place != None) else s.user.location
				print(loc)
				if not first:
					file.write(",\n") #because we don't want the first line to have a comma before it
				else:
					first = False
				file.write("\t\t\t{\n")
				file.write("\t\t\t\"Location\":  \"%s\",\n" % (unicodedata.normalize('NFKD', loc).encode('ascii','ignore')))  #(unicodedata.normalize('NFKD', s.place.full_name).encode('ascii','ignore')))
				file.write("\t\t\t\"URL\": \"http://twitter.com/%s/status/%s\"\n" %(s.user.screen_name, s.id))
				file.write("\t\t\t}")

# write data to json file

first = True
write_data_to_file(file, twts, first)
#first = False
#write_data_to_file(file, twts2, first)
#write_data_to_file(file, twts3, first)

file.write("\n\t\t]\n}")


print "-------------------HASHTAG-MAPPING-------------------"
#hashtag = sys.argv[1]


# terminal commands to call Saranya's javascript code
import subprocess

# text_to_run = 'python %s' % (hashtag
# subprocess.call([text_to_run],shell=True)

# # terminal commands to open .png
# text_to_run = 'open *.png'
# subprocess.call([text_to_run],shell=True)
