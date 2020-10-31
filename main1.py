from tkinter import Button, Tk, HORIZONTAL
from tkinter.ttk import Progressbar
import tkinter
import tkinter as tk
from tkinter import ttk  
from tkinter import *
import tkinter.messagebox
import datetime
from datetime import datetime
import signal
import sqlite3
import nltk.classify
from nltk.corpus import movie_reviews
from nltk.corpus import opinion_lexicon
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import random
import nltk
import nltk.classify
class Login:
	def __init__(self,master):
		#self.tablemaker() # creating tables in the database for account and for meetings
		self.master=master
		self.master.title("EatUp")
		self.master.geometry("800x420+231+200")

		#self.master.geometry('750x300+0+0')
		self.master.config(bg='LightSkyBlue4')
		self.frame= Frame(self.master,bg='LightSkyBlue4')
		self.frame.pack()
		self.Username=StringVar()
		self.Password=StringVar()
		self.Del=StringVar()
		self.Title=Label(self.frame,text='EatUp',font=('arial',70,'bold'),bg='LightSkyBlue4',fg='gray20')
		self.Title.grid(row=0,column=0,columnspan=2)

		self.Logfr1=LabelFrame(self.frame,width=750,height=200,font=('arial',20,'bold'),relief='ridge',bg='cyan4',bd=10)
		self.Logfr1.grid(row=1,column=0)

		self.User=Label(self.Logfr1,text='Input your unique code',font=('arial',30,'bold'),bd=22,bg='cyan4')
		self.User.grid(row=0,column=0)
		self.txtUser=Entry(self.Logfr1,font=('arial',30,'bold'),bg='aquamarine3',textvariable=self.Username, justify='center')#
		self.txtUser.grid(row=1,column=0)
		self.nextButton=Button(self.Logfr1, text='Next',font=('arial',20,'bold'),width=16,command=self.nextBtn)
		self.nextButton.grid(row=2,column=0,pady=20)
	def nextBtn(self):
		self.master.destroy()
		#we launch the actual thing 
		root=tkinter.Tk()
		app=App(root)
		root.mainloop()
class App(Tk):
	def __init__(self,master):
		self.master=master
		self.master.title("Auto-joiner")
		self.master.config(bg='LightSkyBlue4')
		self.master.geometry("580x359+300+220")
		self.frame= Frame(self.master)
		self.frame.pack()
		self.frame.config(bg='LightSkyBlue4')
		self.trb=Label(self.frame,text='\n',font=('arial',20,'bold'),bg='LightSkyBlue4',fg='gray20')
		self.trb.grid(row=0,column=0)
		self.Logfr1=LabelFrame(self.frame,width=750,height=200,font=('arial',20,'bold'),relief='ridge',bg='cyan4',bd=10)
		self.Logfr1.grid(row=1,column=0)

		self.trb=Label(self.Logfr1,text='Menu element1',font=('arial',20,'bold'),bg='cyan4',fg='gray20')
		self.trb.grid(row=0,column=0)

		self.trb=Label(self.Logfr1,text='Menu element2',font=('arial',20,'bold'),bg='cyan4',fg='gray20')
		self.trb.grid(row=1,column=0)

		self.trb=Label(self.Logfr1,text='Menu element3',font=('arial',20,'bold'),bg='cyan4',fg='gray20')
		self.trb.grid(row=2,column=0)
		self.var=[]
		for i in range(0,3):
			self.var.append(IntVar())
		self.checks=Checkbutton(self.Logfr1,font=('arial',20,'bold'),bg='cyan4',fg='gray20', variable=self.var[0])
		self.checks.grid(row=0,column=2)

		self.checks=Checkbutton(self.Logfr1, font=('arial',20,'bold'),bg='cyan4',fg='gray20', variable=self.var[1])
		self.checks.grid(row=1,column=2)

		self.checks=Checkbutton(self.Logfr1, font=('arial',20,'bold'),bg='cyan4',fg='gray20', variable=self.var[2])
		self.checks.grid(row=2,column=2)
		self.ok=0
		self.nextButton=Button(self.Logfr1, text='Order',font=('arial',20,'bold'),width=16,command=self.Finish)
		self.nextButton.grid(row=3,column=0,columnspan=2,pady=20,padx=20)
	def Finish(self):
		for i in range(3):
			if self.var[i].get()==1:
				self.ok=1
		if self.ok==0:
			tkinter.messagebox.showwarning("Warning","You haven't selected any item")
			return
		self.master.destroy()
		#we launch the actual thing 
		root=tkinter.Tk()
		app=endBtn(root)
		root.mainloop()

class endBtn(Tk):
	def __init__(self,master):
		self.master=master
		self.master.title("Auto-joiner")
		self.master.config(bg='LightSkyBlue4')
		self.master.geometry("580x280+400+400")
		self.frame= Frame(self.master)
		self.frame.pack()
		self.frame.config(bg='LightSkyBlue4')
		self.trb=Label(self.frame,text='\n',font=('arial',20,'bold'),bg='LightSkyBlue4',fg='gray20')
		self.trb.grid(row=0,column=0)
		self.Logfr1=LabelFrame(self.frame,width=750,height=200,font=('arial',20,'bold'),relief='ridge',bg='cyan4',bd=10)
		self.Logfr1.grid(row=1,column=0)
		self.orderBtn=Button(self.Logfr1, text='Finish Your Order',font=('arial',30,'bold'),width=16,command=self.Review)
		self.orderBtn.grid(row=3,column=0,pady=20,padx=20)
	def Review(self):
		self.master.destroy()
		#we launch the actual thing 
		root=tkinter.Tk()
		app=revFinal(root)
		root.mainloop()
class revFinal(Tk):
	def __init__(self,master):
		self.master=master
		self.master.title("Auto-joiner")
		self.master.config(bg='LightSkyBlue4')
		self.master.geometry("800x580+300+300")
		self.frame= Frame(self.master)
		self.frame.pack()
		self.frame.config(bg='LightSkyBlue4')
		self.trb=Label(self.frame,text='Leave us a review',font=('arial',20,'bold'),bg='LightSkyBlue4',fg='gray20')
		self.trb.grid(row=0,column=0)
		self.Logfr1=LabelFrame(self.frame,width=150,height=100,font=('arial',20,'bold'),relief='ridge',bg='cyan4',bd=10)
		self.Logfr1.grid(row=1,column=0)
		self.w=Text(self.Logfr1,font=('arial',20,'bold'),bg='cyan4',fg='gray20',height=10, width=50)
		self.w.grid(row=0,column=0)
		self.nxtBtn=Button(self.Logfr1, text='Send your review',font=('arial',30,'bold'),width=16,command=self.respawn)
		self.nxtBtn.grid(row=3,column=0,pady=20,padx=20)
		self.stop_words = stopwords.words("english")
		self.clf = self.get_classifier()
		conn= sqlite3.connect('orders.db')
		c=conn.cursor()
		c.execute("""CREATE TABLE IF NOT EXISTS order (
					cdkey int,
					orders text
					)""")
		conn.commit()
		conn.close()
	def create_word_features_pos(self,words):
		use_words = [word for word in words if word not in self.stop_words]
		my_list = [({word: True}, 'positive') for word in use_words]
		return my_list


	def create_word_features_neg(self,words):
		use_words = [word for word in words if word not in self.stop_words]
		my_list = [({word: True}, 'negative') for word in use_words]
		return my_list


	def create_word_features(self,words):
		use_words = [word for word in words if word not in stopwords.words("english")]
		
		pos_txt = self.get_tokenized_file(u"pos.txt")
		neg_txt = self.get_tokenized_file(u"neg.txt")
		
		my_dict = dict([(word, True) for word in pos_txt if word in use_words])
		my_dict1 = dict([(word, False) for word in neg_txt if word in use_words])
		
		my_dict.update(my_dict1)
		
		return my_dict

	def get_tokenized_file(self,file):
		return word_tokenize(open(file, 'r').read())

	def get_data(self):
		neg_txt = self.get_tokenized_file(u"negative-words.txt")
		neg_features = self.create_word_features_neg(neg_txt)

		pos_txt = self.get_tokenized_file(u"positive-words.txt")
		pos_features = self.create_word_features_pos(pos_txt)
		return pos_features + neg_features

	def process(self,data):
		return [word.lower() for word in word_tokenize(data)]
	def get_classifier(self):

		data = self.get_data()
		random.shuffle(data)

		split = int(0.8 * len(data))

		train_set = data[:split]
		test_set =  data[split:]

		clas = nltk.NaiveBayesClassifier.train(train_set)

		accuracy = nltk.classify.util.accuracy(classifier, test_set)
		print("Accuracy: ", accuracy)
		return clas


	def main_op(self):
		review = self.w.get('1.0',END)
		test = self.process(review)

		test1 =self.create_word_features(test)
		self.test2 = ('review is:'+self.clf.classify(test1))

	def respawn(self):
		#file=open("mlthink.txt","w")
		#a=self.txtRev.get("1.0",END)
		#file.writelines(a)
		#file.close()
		self.main_op()
		tkinter.messagebox.showwarning("Warning",self.demo2)
		'''self.master.destroy()
		root=tkinter.Tk()
		app=Login(root)
		root.mainloop()'''
def main():
	root=tkinter.Tk()
	app=Login(root)
	root.mainloop()


if __name__ == '__main__':
	main()
