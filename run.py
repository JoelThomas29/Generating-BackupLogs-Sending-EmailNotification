""" Executes the application """

from get_config import SSH
from store_result import extract_result
from email_notification import email

# Part 1 - get_config
SSH()

# Part 2 - store_result
extract_result()

# Part 3 - email_notification
email()
	


