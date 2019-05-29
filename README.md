# This program is expected to run in a Linux environment, which is able to reach a virtual router/switch configured in GNS3 or running as   a VM in any virtualization platform.

# Run the following in the OS terminal before running the application
sudo apt-get update && sudo apt-get install libssl-dev

sudo pip3 install netmiko

# Start by run.py which would orchestrate the entire application.
  1. Retrieve configurations from the connected router
  2. Creates log files from above results
  3. Connects to your email and sends a message to the address provided
Please Note: It would usually take about 10-15 seconds to run the program
             and create the expected results. 

# Please make sure you have set the right configurations in your personal email to receive the notifications sent by the script.
  For example: gmail categorizes such attempts to login as less secured and 
  as a work around it asks the user to set the required permissions in gmail
  settings. 

