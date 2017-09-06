#Copyright 2017 Leo Foster
import urllib2
from bs4 import BeautifulSoup
if __name__ == '__main__':
 website = 'http://magicseaweed.com/Hungry-bay-Surf-Report/3929/'
 page = urllib2.urlopen(website)
 soup = BeautifulSoup(page)
 name_box = soup.find('li',attrs={'class':'rating-text text-dark'})
 name = name_box.text.strip()
 print('Hungry Bay')
 print('Wave Height:')
 print(name)
 print('here is a calculator for converting the values to feet if thats what you want put the numbers like 0.7 enter 1.2 ect')
 def calculatorWaveHeight():
   a = float(raw_input('number one'))
   b = float(raw_input('number two'))
   print(a*3.25)
   print('to')
   print(b*3.25)
   print('ft')

 calculatorWaveHeight()
 print('.')
 print('.')
 print('.')
 print('.')
 print('.')
 print('.')
 print('.')
 print('.')
 print('loading next wave height')
 website1 = 'http://magicseaweed.com/Southlands-Surf-Report/3930/'
 page1 = urllib2.urlopen(website1)
 soup1 = BeautifulSoup(page1)
 name_box1 = soup.find('li',attrs={'class':'rating-text text-dark'})
 name1 = name_box1.text.strip()
 print('Southlands')
 print('Wave Height:')
 print(name1)
 print('here is a calculator for converting the values to feet if thats what you want put the numbers like 0.7 enter 1.2 ect')
 calculatorWaveHeight()
 print('.')
 print('.')
 print('.')
 print('.')
 print('.')
 print('.')
 print('.')
 print('.')
else:
 website = 'http://magicseaweed.com/Hungry-bay-Surf-Report/3929/'
 page = urllib2.urlopen(website)
 soup = BeautifulSoup(page)
 name_box = soup.find('li',attrs={'class':'rating-text text-dark'})
 name = same_box.text.strip()
 website1 = 'http://magicseaweed.com/Southlands-Surf-Report/3930/'
 page1 = urllib2.urlopen(website1)
 soup1 = BeautifulSoup(page1)
 name_box1 = soup.find('li',attrs={'class':'rating-text text-dark'})
 name1 = name_box1.text.strip()

     
