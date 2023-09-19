import os
import tkinter.messagebox

def flush(prntwin):
	job=0
	if (not tkinter.messagebox.askyesno("Flush", "Do you really want to Flush checked Tables?")):
		return	
	#Flush Filter Table
	if(prntwin.fltfls.get()==True):
		try:
			os.popen('iptables -F',"r")
			job=1
		except:
			pass

	
	#Flush NAT Table
	if(prntwin.natfls.get()==True):
		try:
			os.popen('iptables -F -t nat',"r")
			job=1
		except:
			pass


	#Flush Mangle Table
	if(prntwin.mnglfls.get()==True):
		try:
			os.popen('iptables -F -t mangle',"r")
			job=1
		except:
			pass
	
	if(job==1):
		tkinter.messagebox.showinfo("Flushed","Checked Tables has been Flushed.")


def delete(prntwin):
	if (not tkinter.messagebox.askyesno("Delete", "Do you really want to Delete specified rule?")):
		return	
	#Delete from Filter Table
	if(prntwin.tbl.get()=="filter"):
		if(prntwin.chn.get()=="INPUT" or prntwin.chn.get()=="OUTPUT" or prntwin.chn.get()=="FORWARD"):
			try:
				os.popen('iptables -D '+prntwin.chn.get()+' '+prntwin.delpos.get()+' -t filter',"r")
			except:
				pass

	
	#Delete from NAT Table
	if(prntwin.tbl.get()=="nat"):
		if(prntwin.chn.get()=="PREROUTING" or prntwin.chn.get()=="POSTROUTING"):
			try:
				os.popen('iptables -D '+prntwin.chn.get()+' '+prntwin.delpos.get()+' -t nat',"r")
				tkinter.messagebox.showinfo("Deleted","Specified rule has been Deleted.")
			except:
				pass

	
	
