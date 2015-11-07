from urllib import request
from bs4 import BeautifulSoup
from splinter import Browser
import time, random

__author__ = 'Chris Thurber, Drew University'

with Browser() as browser:
	# Login to Facebook.com
	url = "https://www.facebook.com/login?_rdr=p"
	browser.visit(url)
	browser.fill('email', input("Username: "))	# Username field
	browser.fill('pass', input("Password: "))	# Password field
	button = browser.find_by_name('login') 		# Login button
	button.click()

	baseURL = "http://facebook.com/profile.php?id="
	with open('first100.csv','w') as fonek:
		print("number,id,name",file=fonek)
		userNum = 1
		for i in range(1,100):
			profile = baseURL+str(i)
			browser.visit(profile)
			profileSource = BeautifulSoup(browser.html)

			srcT = profileSource.find('h2',{'id':'standard_error'})
			try:
				error = srcT.text
				print(" Can't find profile #"+str(i))
			except:
				print(" Got profile #"+str(i))
				name = profileSource.find('title')
				print(name.text)
				print(userNum,",",i,",",name.text,file=fonek)
				userNum+=1
			time.sleep(random.randint(3,7)) 	# Prevent DOSing
