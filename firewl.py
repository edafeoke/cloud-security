import os
import tkinter.messagebox


def disable():
	if (not tkinter.messagebox.askyesno("Disable", "Do you really want to Disable Firewall?")):
		return "no"
	os.popen('iptables-save > ~/Desktop/firewall.rules',"r")
	os.popen('iptables -t nat -F',"r")
	os.popen('iptables -t nat -X',"r")
	os.popen('iptables -t mangle -F',"r")
	os.popen('iptables -t mangle -X',"r")
	os.popen('iptables -P INPUT ACCEPT',"r")
	os.popen('iptables -P FORWARD ACCEPT',"r")
	os.popen('iptables -P OUTPUT ACCEPT',"r")
	tkinter.messagebox.showinfo("Disabled","The Firewall has been Disabled.")
	return "yes"

	

def enable():
	os.popen('iptables-restore < ~/Desktop/firewall.rules',"r")
	tkinter.messagebox.showinfo("Enabled","The Firewall has been Enabled.")
	

def flush():
	if (not tkinter.messagebox.askyesno("Flush", "Do you really want to Flush Firewall?")):
		return
	res=os.popen('iptables -F',"r")
	tkinter.messagebox.showinfo("Flushed","The Firewall has been Flushed.")

	
