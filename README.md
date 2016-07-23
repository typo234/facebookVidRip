# facebookVidRip
Script to rip facebook video, still requires manual identification of video string.

Original code/idea from http://stackoverflow.com/questions/18552813/convert-unicode-of-form-uxxxxxx-to-string-or-text

TODO:
  - stop just accepting raw input, ensure a correct url is being entered
  - automate identification of url from source
  - clean up, beautify, etc

In order to use: view-source of video page you wish to download, find the string that begins with https and includes the video url's unique ID, copy entire string up to next 'https' and enter into script.  Script will spit out the url of the raw video.
