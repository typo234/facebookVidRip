#facebook vid rip
#thanks to http://stackoverflow.com/questions/18552813/convert-unicode-of-form-uxxxxxx-to-string-or-text

import re
import urllib

print "You will need to view-source on the page of the video you want on facebook."
print "Once you view-source, you are looking for something like 'https\u00253A\u00255C' ...etc until the next https entry"
enterMessage = "Please enter url of video: \n"
s = raw_input(enterMessage)
print " "
print "Click below url for video\n"
print re.sub(r'\\(.)', r'\1', urllib.unquote_plus(s.decode('unicode_escape')))