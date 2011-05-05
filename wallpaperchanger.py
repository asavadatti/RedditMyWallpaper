def changeWallpaper(path):
  try:
    print 'Trying Gnome'
    import commands
    command = "gconftool-2 --set /desktop/gnome/background/picture_filename --type string '%s'" % path
    status, output = commands.getstatusoutput(command)
  except ImportError:
    try:
      print 'Trying Windows'
      import ctypes
      SPI_SETDESKWALLPAPER = 20
      ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, path , 0)
    except ImportError:
      try:
        print 'Trying Mac OS X'
        import subprocess
        SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""
        subprocess.Popen(SCRIPT%filename, shell=True)
      except ImportError:
        print 'fail!'
