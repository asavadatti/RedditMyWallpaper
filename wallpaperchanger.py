import subprocess,sys,os
import platform

def changeWallpaper(path):
  osName = platform.system()
  
  if(osName == "Darwin"):
    # Trying Apple Mac OSX
    print (" Trying Mac OSX")
    Script = """/usr/bin/osascript<<END
    tell application "Finder"
    set desktop picture to POSIX file "%s"
    end tell
    END"""
 
    # run the apple script inserting the filename
    subprocess.Popen(Script%path,shell=True)

#  if(osName == "Linux"):
#    # Trying Linux

#    print 'Trying Gnome'
#    import commands
#    command = "gconftool-2 --set /desktop/gnome/background/picture_filename --type string '%s'" % path
#    status, output = commands.getstatusoutput(command)


