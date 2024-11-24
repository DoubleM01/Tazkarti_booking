# import required modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options

import time
import datetime
from datetime import datetime

#from sinch import Client

# create instance of Chrome webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
import requests

from time import sleep
#from sinchsms import SinchSMS

#Fan ID
tazkarti_id = "Your tazkart ID"
tazkarti_pass = "Your tazkart password"

## Match Data
team_name = 'Ahly'
#team_name = 'Pyramids'
#team_name = 'Al Ahly FC'
tournament_name = 'CAF'
#tournament_name = 'EPL'
#tournament_name = 'CAF'
keywords = ''
# driver = None
#
# def browser_exts():
# 	#~/.config/google-chrome/Default/Extensions
# 	global driver
# 	from selenium.webdriver.chrome.options import Options
#
#
#
# 	chrome_options = Options()
# 	chrome_options.add_extension('buster-main.zip')
#
# 	driver = webdriver.Chrome( options=chrome_options)
# browser_exts()

#driver.get("https://tazkarti.com/#/matches")
#time.sleep(7)
driver.get("https://tazkarti.com/#/login")

# find the element where we have to
# enter the xpath
# fill the email
driver.find_element(By.XPATH,'/html/body/app-root/login/div[2]/div/form/div[1]/input').send_keys(tazkarti_id)

# click on next button
#driver.find_element(By.XPATH,
#	'//*[@id="root"]/div/div[2]/div[1]/div/div/div/div/div/div/form/div[3]/button/span').click()

# find the element where we have to
# enter the xpath
# fill the password
driver.find_element(By.XPATH,'/html/body/app-root/login/div[2]/div/form/div[2]/input').send_keys(tazkarti_pass)
driver.find_element(By.XPATH,'/html/body/app-root/login/div[2]/div/form/button').click()
#time.sleep(12)
sign_in = False


def get_details(match_index):
	second_team_div = driver.find_element(By.XPATH, '/html/body/app-root/app-matches/div[4]/div/div[3]/div[' + str(
		match_index) + ']/div/div[1]/div[1]/div[3]/div[2]/div[2]')
	first_team_div = driver.find_element(By.XPATH, '/html/body/app-root/app-matches/div[4]/div/div[3]/div[' + str(
		match_index) + ']/div/div[1]/div[1]/div[3]/div[1]')
	tournament_div = driver.find_element(By.XPATH,
															 '/html/body/app-root/app-matches/div[4]/div/div[3]/div['+ str(match_index) +']/div/div[2]/div[1]/div[2]')
	date_div = driver.find_element(By.XPATH,
										 '/html/body/app-root/app-matches/div[4]/div/div[3]/div[' + str(
											 match_index) + ']/div/div[1]/div[2]/div[2]/div[2]/div[1]')
	time_div = driver.find_element(By.XPATH,
											 '/html/body/app-root/app-matches/div[4]/div/div[3]/div[' + str(
											 match_index) + ']/div/div[1]/div[2]/div[2]/div[2]/div[2]')
	print("Match details:----")
	print("First Team: " + first_team_div.text)
	print("Second Team: " + second_team_div.text)
	print("Tournament: " + tournament_div.text)
	print("Match date: " + date_div.text)
	print("Match time: " + time_div.text)


#/html/body/app-root/app-matches/div[4]/div/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[1]
#/html/body/app-root/app-matches/div[4]/div/div[3]/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]

while not sign_in:
	try:
		driver.find_element(By.XPATH,'/html/body/app-root/app-dashboardprofile/app-navbar-user/div/div[1]/ul/li[2]/a').click()
		sign_in = True
	except:
		...
found = False
match_index_final = -1
while 1:
	while not found:
		print('start')
		time.sleep(5)
		#time.sleep(3)
		driver.get("https://tazkarti.com/#/matches")
		#driver.find_element(By.XPATH,'/html/body/app-root/app-matches/app-navbar-user/div/div[1]/ul/li[2]/a').click()
		#/html/body/app-root/app-matches/app-navbar-user/div/div[1]/ul/li[2]/a
		print(datetime.now())
		time.sleep(3)
		if 1:
			#/html/body/app-root/app-matches/div[4]/div/div[3]/div[3]/div/div[1]/div[1]/div[3]/div[2]/div[2]
			#/html/body/app-root/app-matches/div[4]/div/div[3]/div[3]/div/div[1]/div[1]/div[3]/div[1]
			#/html/body/app-root/app-matches/div[4]/div/div[3]/div[1]/div/div[2]/div[1]/div[2]
			#/html/body/app-root/app-matches/div[4]/div/div[3]/div[2]/div/div[2]/div[1]/div[2]
			#/html/body/app-root/app-matches/div[4]/div/div[3]/div[4]/div/div[2]/div[1]/div[2]
			#/html/body/app-root/app-matches/div[4]/div/div[3]/div[3]/div/div[2]/div[1]/div[2]
			found_team = False
			found_tournament = False
			found_keyword = False
			found_match = False
			for i in range(1, 10):
				try:

					second_team_div = driver.find_element(By.XPATH,'/html/body/app-root/app-matches/div[4]/div/div[3]/div[' + str(i) + ']/div/div[1]/div[1]/div[3]/div[2]/div[2]')
					first_team_div = driver.find_element(By.XPATH,'/html/body/app-root/app-matches/div[4]/div/div[3]/div[' + str(i) + ']/div/div[1]/div[1]/div[3]/div[1]')
					first_team_text = first_team_div.text
					second_team_text = second_team_div.text
					print("checking match: " + str(i))
					if team_name in first_team_text:
						print("found a match for " + team_name)
						print(first_team_text)
						print("wait till check for the tournament")
						found_team = True
					if team_name in second_team_text:
						print("found a match for " + team_name)
						print(first_team_text)
						print("wait till check for the tournament")
						found_team = True
					if found_team:
						tournament_div = driver.find_element(By.XPATH,
															 '/html/body/app-root/app-matches/div[4]/div/div[3]/div['+ str(i) +']/div/div[2]/div[1]/div[2]')
						tournament_div_text = tournament_div.text
						print(tournament_div_text)
						if tournament_name in tournament_div_text:
							print("found a match for " + team_name + " in " + tournament_name)
							found_tournament = True
						if found_tournament and found_team:
							found_match = True
						else:
							found_team = False
							found_tournament = False
							found_keyword = False
							found_match = False
						if found_match:
							print("match posted in tazkarti")
							match_index_final = i

							break

				except Exception as e:
					#print(e)
					...





				#btn = driver.find_element(By.XPATH,'/html/body/app-root/app-matches/div[4]/div/div[3]/div[' + str(i) + ']/div/div[1]/div[2]/button')
			#/html/body/app-root/app-matches/div[4]/div/div[3]/div[4*d]/div/div[1]/div[2]/button
			#/html/body/app-root/app-matches/div[4]/div/div[3]/div[3]/div/div[1]/div[2]/button
		try:
			if not found_match:
				driver.refresh()
		except:
			print("error refresh")
		try:
			if found_match:
				get_details(match_index_final)
				print("please wait, check for available tickets")
				btn = driver.find_element(By.XPATH, '/html/body/app-root/app-matches/div[4]/div/div[3]/div[' + str(
					match_index_final) + ']/div/div[1]/div[2]/button')
				print(btn.text)

				if btn.text == 'Book Ticket':
					# No Noftifications Version
					#send_PushNotification(team_name,datetime.now().strftime("%H:%M"))

					print("tickets found")
					print("Choose the category and pay quickly")
					print("time now is:")
					print(datetime.now().strftime("%H:%M:%S"))
					found = True
					btn.click()
					#sendSMS()
				elif "Booking Closed" in btn.text:
					found = True
					print("sry Booking Closed")
		except Exception as er:
			found=False
			# print(er)





#'/html/body/app-root/app-matches/div[4]/div/div[3]/div[1]/div/div[1]/div[2]/button'

# find the element Sign in
# request using xpath
# clicking on that element
#driver.find_element_by_xpath(
#	'//*[@id="root"]/div/div[2]/div[1]/div/div/div/div/div/div/form/button/span').click()
