import pyshark
#interface is en1
#within the virtual environment you have to run this with python3 specifically 
capture = pyshark.LiveCapture(interface="en1")
