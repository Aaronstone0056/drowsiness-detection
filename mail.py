
# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 

# creates SMTP session 
def sendmail():
	pass
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	  
	# start TLS for security 
	s.starttls() 
	  
	# Authentication 
	s.login("narendranandu.b@gmail.com", "Aaron@007") 
	  
	# message to be sent 
	message = "drowsy"
	  
	# sending the mail 
	s.sendmail("narendranandu.b@gmail.com", "narendranani.b@gmail.com", message) 
	  
	# terminating the session 
	s.quit() 