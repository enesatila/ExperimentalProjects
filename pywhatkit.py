from asyncore import loop
import pywhatkit 
try:
   
  # sending message to receiver
  # using pywhatkit
  pywhatkit.sendwhatmsg("+905534307145",
                        "Seni sewiom",
                        2, 26)
  print("Successfully Sent!")
 
except:
   
  # handling exception
  # and printing error message
  print("An Unexpected Error!")