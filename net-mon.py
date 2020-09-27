import smtplib
import sys
import subprocess
import os
from decouple import config

# IP address to detect
IP_DEVICE = '255.255.255.255'

proc = subprocess.Popen(["ping", '-t', IP_DEVICE], stdout=subprocess.PIPE)

while True:
    line = proc.stdout.readline()
    if not line:
        break
    else:
        None

    try:
        connected_ip = line.decode('utf-8').split()[2].replace(':', '')
        if connected_ip == IP_DEVICE:
            print('Device connected!')

            # Creates SMTP session
            smtp_session = smtplib.SMTP('smtp.gmail.com', 587)
            # Start TLS for security
            smtp_session.starttls()
            # Authentication
            smtp_session.login("youremail@email.cpom", "yourpassword")
            # Message to be sent
            message = "Device connected to the network " + IP_DEVICE
            to = "noreply@noreply.com"
            fr = "noreply@noreply.com"
            # Sending mail
            smtp_session.sendmail(to, fr, message)
            # Terminating the session
            smtp_session.quit()
            break
        else:
            print('Pinging device...')
    except:
        pass
