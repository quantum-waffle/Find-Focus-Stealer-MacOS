#!/usr/bin/python  
# see https://apple.stackexchange.com/questions/123730/is-there-a-way-to-detect-what-program-is-stealing-focus-on-my-mac                                                                                               
# pip3 install pyobjc
# Python 3.11.0
try:
    from AppKit import NSWorkspace
except ImportError:
    print("Can't import AppKit -- maybe you're running python from brew?")
    print("Try running with Apple's /usr/bin/python instead.")
    exit(1)

from datetime import datetime
from time import sleep

last_active_name = None
while True:
    active_app = NSWorkspace.sharedWorkspace().activeApplication()
    if active_app['NSApplicationName'] != last_active_name:
        last_active_name = active_app['NSApplicationName']
        print('%s: %s [%s]' % (
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            active_app['NSApplicationName'],
            active_app['NSApplicationPath']
        ))
    sleep(1)