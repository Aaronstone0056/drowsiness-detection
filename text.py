from gtts import gTTS
import os
from playsound import playsound

def audio():
	pass
	mytext = 'Alert! driver is drowsy'
	  
	# Language in which you want to convert 
	language = 'en'
	 

	pass
	myobj = gTTS(text=mytext, lang=language, slow=True) 
		  
		# Saving the converted audio in a mp3 file named 
		# welcome  
	myobj.save("drowsy.mp3") 
	pass
		  
		# Playing the converted file

	playsound(r'C:\Users\nandu\Desktop\drowsy\Drowsiness_Detection-master\drowsy.mp3');
	playsound(r'C:\Users\nandu\Desktop\drowsy\Drowsiness_Detection-master\drowsy.mp3');
	playsound(r'C:\Users\nandu\Desktop\drowsy\Drowsiness_Detection-master\drowsy.mp3');
	playsound(r'C:\Users\nandu\Desktop\drowsy\Drowsiness_Detection-master\drowsy.mp3');
	playsound(r'C:\Users\nandu\Desktop\drowsy\Drowsiness_Detection-master\drowsy.mp3');
	playsound(r'C:\Users\nandu\Desktop\drowsy\Drowsiness_Detection-master\drowsy.mp3');
