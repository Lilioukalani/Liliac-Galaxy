# import speical libaries already built in python
import random, urllib2
# list of options to select from
the_url = 'https://raw.githubusercontent.com/Lilioukalani/Liliac-Galaxy/master/activities.txt'
list_raw_text= urllib2.urlopen(the_url).read()

#print "DEBUG: " + str(list_raw_text.split())


possible_activities= list_raw_text.split()
the_activity =random.choice (possible_activities)

print "Possible activities are: " + str(possible_activities)
print "What we are going to do: " + the_activity
