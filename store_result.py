""" This program takes input from getting_config.py and stores in the current folder as a log file, stamped with the current date.
    It also creates an HTML difference page, displaying config log differences between current and one day old file  """

import difflib
import datetime
import get_config

def extract_result():
	global difference
	
	# Storing the current output
	new_file = 'configlog_' + get_config.ip + '_' + datetime.date.today().isoformat()
	with open(new_file, 'w') as new:
		new.write(get_config.output + '\n')
	
	# Finding deferences between current and one day old config file, in HTML format
	old_file = 'configlog_' + get_config.ip + '_' + (datetime.date.today() - datetime.timedelta(days=1)).isoformat()
	with open(old_file, 'r') as old, open(new_file, 'r') as new:
		difference = difflib.HtmlDiff().make_file(fromlines = old.readlines(), tolines = new.readlines(), fromdesc = 'Yesterday', todesc = 'Today')

