# Description
This program is a web-driven application that accepts gmail credentials and returns unread email count. The back-end is written in python and uses REST API of gmail. The front-end and “bridge” between the front and back-ends is written in java.
<br />Note: For Java-side is used Netbeans IDE
# Prerequisites
To run this program, you'll need:
<ul>
<li>	Python 3.6.</li>
<li>	Gmail API Overview, Python Quickstart.</li>
<li>	Java Runtime Environment.</li>
<li>	Windows operating system.</li>
<li>	Access to the internet.</li>
</ul>
# Running 
<br />Step 1: Server side
<ul>
<li>		Run URL_Connection.py.</li>
<li>		Configure hostname for http server if need be (default is localhost:8080).</li> 
</ul>
<br />Step 2: Client side
<ul>
<li>		Run unread_email_count.jar (unread_email_count\dist). </li>
<li>		If necessary configure hostname of http server form "Settings" window.</li>
<li>		Input login and password of existing  gmail account. </li>
<li>		Click ‘Get Count’ button. </li>
</ul>
<br />You see your all email count and unread email count. 
<br />Note: If you want to use this program to see your gmail unread email count , you need  change your account settings. Allow less secure apps: ON. (https://myaccount.google.com/lesssecureapps?rfn=27&rfnc=1&eid=-1324603768160278546&et=0&asae=2&pli=1) 
