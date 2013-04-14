# -*- coding: utf-8 -*-
# Making our Eurovision mood report into a web server
import urllib
from datetime import datetime
import os
import Tkinter
import tkFileDialog

class MoodTracker:
    def __init__(self, master, logfilename):
        self.logfilename = logfilename
        self.title = Tkinter.Label(text="Eurovision mood tracker")
        self.title.pack()
        # the button frame
        fr = Tkinter.Frame(master)
        fr.pack(side='top', expand=1, fill='x')
        back = Tkinter.Button(fr, text="Check mood", command=lambda : self.nextframe(-1))
        back.grid(row=0, column=0, sticky="w", padx=4, pady=4)
        
    def _logresult(self, result):
        now = datetime.now()
        now_as_string = str(now)
        with open('moodtracker.log','a') as fo:
            fo.write(now_as_string + " " + result + "\n")
            
    def show_and_log_mood(self):
        url = 'http://admin.webworks.se/pythoncourse/eurovision'
        try:
            connection = urllib.urlopen(url)
            result = connection.read()
        except IOError:
            result =  url + "fetch did not work"
        _logresult(result)
        return "Mood is: " + result
 
if __name__ == "__main__":
    root = Tkinter.Tk()
    root.geometry("800x600+300+300")

    dirname = tkFileDialog.answerdirectory(parent=root,initialdir=".",title='Please select a directory for the log file')

    logfilename = os.path.join(dirname, 'moodtracker.log')
    
    app = MoodTracker(root, logfilename)
    root.mainloop()





     







