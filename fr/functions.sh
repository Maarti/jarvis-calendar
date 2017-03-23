#!/bin/bash
# Here you can define translations to be used in the plugin functions file
# the below code is an sample to be reused:
# 1) uncomment to function below
# 2) replace XXX by your plugin name (short)
# 3) remove and add your own translations
# 4) you can the arguments $2, $3 passed to this function
# 5) in your plugin functions.sh file, use it like this:
#      say "$(pv_myplugin_lang the_answer_is "oui")"
#      => Jarvis: La réponse est oui

jv_calendar_createEvent()
{
	python -u python/createEvent.py
}

jv_calendar_lookForEvent()
{
	python -u python/lookForEvent.py 
	while read line
	do
		say "$line"
	done < python/evenement.txt
}
jv_calendar_nextEvent()
{
	python -u python/nextEvent.py
	while read line
	do
		say "$line"
	done < python/evenement.txt
}

jv_calendar_todayEvent()
{
	python -u python/todayEvent.py
	while read line
	do
		say "$line"
	done < python/evenement.txt
}
jv_calendar_tomorrowEvent()
{
	python -u python/tomorrowEvent.py
	while read line
	do
		say "$line"
	done < python/evenement.txt
}
