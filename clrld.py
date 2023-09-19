from tkinter import *
import os
import tkinter.filedialog
import tkinter.messagebox


def clear(win):
	win.spctab.sttsobj.clear()
	win.spctab.polobj.clear()
def reload(win):
	win.spctab.sttsobj.reload()
	win.spctab.polobj.reload()
def save():
	ruleflname=tkinter.filedialog.asksaveasfilename(filetypes=[("Firewall Rules",".rules")],defaultextension=".rules")
	if(ruleflname!=""):	
		os.popen('iptables-save > '+ruleflname,"r")
		tkinter.messagebox.showinfo("Saved","Firewall Rules have been saved as: "+ruleflname)
def restore():
	ruleflname=tkinter.filedialog.askopenfilename(filetypes=[("Firewall Rules",".rules")])
	if(ruleflname!=""):	
		os.popen('iptables-restore < '+ruleflname,"r")
		tkinter.messagebox.showinfo("Restored","Firewall Rules have been restored from: "+ruleflname)

