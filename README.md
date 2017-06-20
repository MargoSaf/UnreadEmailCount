# Description
This program is a web-driven application that accepts gmail credentials and returns unread email count. The back-end is written in python and uses REST API of gmail. The front-end and “bridge” between the front and back-ends is written in java.

Note: For Java-side is used Netbeans IDE

# Prerequisites

To run this program, you'll need:
* Python 3.6.
* Gmail API Overview, Python Quickstart.
* Java Runtime Environment.
* Windows operating system.
*	Access to the internet.

# Running 

Step 1: Server side

*	Run Server.py.
* Configure hostname for http server if need be (default is localhost:8080).

Step 2: Client side

*	Run unread_email_count.jar (unread_email_count\dist).
*	If necessary configure hostname of http server form "Settings" window.
*	Input login and password of existing  gmail account.
*	Click ‘Get Count’ button.

You see your all email count and unread email count. 

Note: If you want to use this program to see your gmail unread email count , you need  change your account settings. Allow less secure apps: ON. (https://myaccount.google.com/lesssecureapps?rfn=27&rfnc=1&eid=-1324603768160278546&et=0&asae=2&pli=1) 
