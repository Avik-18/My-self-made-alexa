import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import random
import webbrowser
from tkinter import *   
import pandas as pd
import numpy as np
import PyPDF2 
  
top = Tk()  
  
top.geometry("700x500")  

top.title("My First Alexa")

bg = PhotoImage(file = "./resource/background.png")

button_bg = PhotoImage(file = "./resource/mic.png")

# Create Canvas 
canvas1 = Canvas( top, width = 500,height = 400) 
  
canvas1.pack(fill = "both", expand = True) 
  
# Display image 
canvas1.create_image( 0, 0, image = bg,anchor = "nw") 


listener=sr.Recognizer()
engine=pyttsx3.init()




def talk(text):

	engine.say(text)

	engine.runAndWait()


def get_command():
	try:
		with sr.Microphone() as source:

			

			voice=listener.listen(source)

			try:

				command=listener.recognize_google(voice)

				command=command.lower()

				#if 'alexa' in command:

				print(command)

				command=command.replace('alexa','')

				#else:

				#	talk("Command should contain the word alexa")
				#	return 'Command should contain the word alexa'

			except:
				return 'Some audio problem'

	except:
		return 'exit'


	return command

def run_alexa(command):

	
	if 'play' in command:

		if 'quiz' in command or 'game' in command:


			qtr=pd.read_csv('./resource/quiz_topic.csv',sep=",",header=None)

			a=qtr.to_numpy()

			r=a.shape[0]

			k=random.randint(1, r-1)

			name=a[k][0]

			talk('Playing '+name)
			print('Playing '+name)


			name='./resource/'+name+'.csv'



			str=pd.read_csv(name,sep=",",header=None)

			arr=str.to_numpy()

			row=arr.shape[0]

			col=arr.shape[1]



			for i in range(1,row):
			    
			    print(arr[i][0])
			    talk(arr[i][0])
			    
			    for j in range(1,col-1):
			        
			        print(j,") ",arr[i][j])
			        talk(j)
			        talk(arr[i][j])

			        arr[i][j]=arr[i][j].lower()
			    
			    #ans=input("Enter your answer : ")
			    arr[i][5]=arr[i][5].lower()
			    
			    print('Tell you Answer : ')
			    talk('Tell you Answer : ')


			    num=get_command()
			        
			    f=0
			    
			    if arr[i][5] in num and len(num)>len(arr[i][5]):
			        print("Speak the answer only. You are disqualified")
			        talk("Speak the answer only. You are disqualified")
			        f=0
			        exit()

			    elif len(arr[i][5])==len(num):
			        f=1
			        
			    talk("The Answer you gave is")
			    talk(num)
			    print("The Answer you gave is ",num)
			    
			    if arr[i][5] in num and f==1:
			        
			        print("Answer is correct\n\n")
			       	talk("Answer is correct\n\n")
			        
			    else:
			        print("Answer is wrong\n\n")
			        talk("Answer is wrong\n\n")

		else:

			song=command.replace('play','')

			talk('playing '+song)

			print('playing '+song)

			pywhatkit.playonyt(song)


	elif 'listen' in command:

		if 'news' in command:

			news_channel=('ABP Ananda Live','Zee 24 Ghanta Live','Republic Tv Live','NDTV Live','ABP Live')

			j=random.randint(0, 4)

			news_name=news_channel[j]

			talk('playing '+news_channel[j])

			print('playing '+news_channel[j])

			pywhatkit.playonyt(news_channel[j])



		elif 'jokes' in command or 'joke' in command:

			talk('Playing some jokes for you')

			talk(pyjokes.get_joke())

 	



	elif 'search' in command:

		search=command.replace('search','')

		url='https://google.com/search?q='+search

		webbrowser.get().open(url)

		talk('Here is you search for '+search)

		print('Here is you search for '+search)


	elif 'find location' in command or 'location' in command:

		search=command.replace('find location','')

		url='https://google.nl/maps/place/'+search+'/&amp'
		
		webbrowser.get().open(url)

		talk('Here is you location of '+search)

		print('Here is you location of '+search)


	elif 'time' in command:
		time=datetime.datetime.now().strftime('%I:%M %p')

		talk('The current time is '+time)

		print('The current time is '+time)



	elif 'jokes' in command or 'joke' in command:

		talk('Playing some jokes for you')

		talk(pyjokes.get_joke())


	elif 'Alexa are you single' in command:

		talk('Nooo not at all.')
		talk('I am in relationship with your wifi')

		print('Nooo not at all.')
		print('I am in relationship with your wifi')

	elif 'what is my relationship status' in command:

		talk('Single')
		print('Single')

	elif 'Why i am single' in command:

		talk('Karoon tuuuii goorrib')
		talk('Karoon tuuuii goorrib')


	elif 'open' in command:
		sites=command.replace('open','')

		if 'hotstar' in command:

			url='https://www.hotstar.com/in'
			webbrowser.get().open(url)

			talk('Opening '+sites)
	
			print('Opening '+sites)

		elif 'zee5' in command:

			url='https://www.zee5.com/'

			webbrowser.get().open(url)

			talk('Opening '+sites)

			print('Opening '+sites)

		elif 'sony liv' in command:

			url='https://www.sonyliv.com/'

			webbrowser.get().open(url)

			talk('Opening '+sites)

			print('Opening '+sites)

		elif 'hoichoi' in command:

			url='https://www.hoichoi.tv/'

			webbrowser.get().open(url)

			talk('Opening '+sites)

			print('Opening '+sites)

		elif 'flipkart' in command:

			url='https://www.flipkart.com/'

			webbrowser.get().open(url)

			talk('Opening '+sites)

			print('Opening '+sites)

		elif 'amazon' in command:

			url='https://www.amazon.in/'

			webbrowser.get().open(url)

			talk('Opening '+sites)

			print('Opening '+sites)

		elif 'whatsapp' in command:

			url='https://web.whatsapp.com'

			webbrowser.get().open(url)

			talk('Opening '+sites)

			print('Opening '+sites)


		elif 'youtube' in command:

			url='https://www.youtube.com/?gl=IN'

			webbrowser.get().open(url)

			talk('Opening '+sites)

			print('Opening '+sites)


			

	elif 'story' in command or 'book' in command or 'read' in command:


		qtr=pd.read_csv('./resource/Book_name.csv',sep=",",header=None)

		a=qtr.to_numpy()

		r=a.shape[0]

		j=random.randint(1, r-1)

		name=a[j][0]

		talk('Playing '+name)
		print('Playing '+name)

		name='./resource/'+name+'.pdf'


		pdfFileObj=open(name,'rb')


		pdfReader=PyPDF2.PdfFileReader(pdfFileObj)

		n=pdfReader.numPages

		for i in range(0,n):

			pageObj=pdfReader.getPage(i)

			talk(pageObj.extractText())

			print(pageObj.extractText())

		pdfFileObj.close()


	elif 'exit' in command:

		exit()



def turn_on():

	talk("Alexa is back on work, how can i help you")

	command=get_command()

	if command!='':

		run_alexa(command)



def turn_on_text(command):

	if command!='':

		run_alexa(command)

name_var=StringVar()


def read_command():

	name=name_var.get()

	print('The command is : '+name)

	turn_on_text(name)

	name_var.set("")


def get_input():
	

	l1=Label(top, text="Type")

	l1.place(x=260, y=450)

	e1 = Entry(top,textvariable = name_var)

	e1.place(x=300, y=450)

	b3 = Button(top,text = "Run",command = read_command,activeforeground = "white",activebackground = "blue")  
  
	b3.place(x=440, y=450)




b1 = Button(top,text = "Click to Speek",image=button_bg,command = turn_on,activeforeground = "white",activebackground = "blue",pady=10)  
  
b1.place(x=280, y=150) 


b2 = Button(top,text = "Type your command",command = get_input,activeforeground = "white",activebackground = "blue",pady=10)  
  
b2.place(x=290, y=350)
  

  
top.mainloop()  
