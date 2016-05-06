#!/usr/bin/env python
import sys
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
Metal_MotorA = 12
Metal_MotorB = 16
Paper_MotorA = 6
Paper_MotorB = 13
Plastic_MotorA = 19
Plastic_MotorB = 26
Glass_MotorA = 21
Glass_MotorB = 20
class StudentInfo:
        stud_id = [9181817171001,9181817172002,9181817173003,9181817174004,9181817175005]
	stud_score = [0,0,0,0,0]

	
StudentInfo

Workers_id = [2131314141001,2131314142002,2131314143003,2131314144004,2131314145005]
metal_barcode = [5285000328551,5285000327813,788930518221,5201004021328]
paper_barcode = [5281028467135,8690504034506,5281034010677,515161614144004]
plastic_barcode = [5283003400847,5283007434053,5283003400748,6281022107067]
glass_barcode = [80177425,5285000326892,3179730010058,788930204124]
def readBarcode():
	hid = { 4: 'a', 5: 'b', 6: 'c', 7: 'd', 8: 'e', 9: 'f', 10: 'g', 11: 'h', 12: 'i', 13: 'j', 14: 'k', 15: 'l', 16: 'm', 17: 'n', 18: 'o', 19: 'p', 20: 'q', 21: 'r', 22: 's', 23: 't', 24: 'u', 25: 'v', 26: 'w', 27: 'x', 28: 'y', 29: 'z', 30: '1', 31: '2', 32: '3', 33: '4', 34: '5', 35: '6', 36: '7', 37: '8', 38: '9', 39: '0', 44: ' ', 45: '-', 46: '=', 47: '[', 48: ']', 49: '\\', 51: ';' , 52: '\'', 53: '~', 54: ',', 55: '.', 56: '/'  }

	hid2 = { 4: 'A', 5: 'B', 6: 'C', 7: 'D', 8: 'E', 9: 'F', 10: 'G', 11: 'H', 12: 'I', 13: 'J', 14: 'K', 15: 'L', 16: 'M', 17: 'N', 18: 'O', 19: 'P', 20: 'Q', 21: 'R', 22: 'S', 23: 'T', 24: 'U', 25: 'V', 26: 'W', 27: 'X', 28: 'Y', 29: 'Z', 30: '!', 31: '@', 32: '#', 33: '$', 34: '%', 35: '^', 36: '&', 37: '*', 38: '(', 39: ')', 44: ' ', 45: '_', 46: '+', 47: '{', 48: '}', 49: '|', 51: ':' , 52: '"', 53: '~', 54: '<', 55: '>', 56: '?'  }

	fp = open('/dev/hidraw3','rb')
	ss = ""
	shift = False

	done = False

	while not done:
   		## Get the character from the HID
   		buffer = fp.read(8)
   		for c in buffer:
      			if ord(c) > 0:

         		##  40 is carriage return which signifies
        		##  we are done looking for characters
         			if int(ord(c)) == 40:
           			 	done = True
           				break;
        		##  If we are shifted then we have to 
         		##  use the hid2 characters.
         			if shift: 

      				## If it is a '2' then it is the shift key
           				if int(ord(c)) == 2 :
              					shift = True

            			## if not a 2 then lookup the mapping
            				else:
               					ss += hid2[ int(ord(c)) ]
               					shift = False

        			##  If we are not shifted then use
         			##  the hid characters

         			else:

            				## If it is a '2' then it is the shift key
            				if int(ord(c)) == 2 :
               					shift = True
	
            			## if not a 2 then lookup the mapping
            				else:
               					ss += hid[ int(ord(c)) ]
         	
	k = int(ss)
	return k

while True:
	print "aa"
        GPIO.setup(Metal_MotorA,GPIO.OUT)
        GPIO.setup(Metal_MotorB,GPIO.OUT)
        GPIO.setup(Paper_MotorA,GPIO.OUT)
        GPIO.setup(Paper_MotorB,GPIO.OUT)
        GPIO.setup(Plastic_MotorA,GPIO.OUT)
        GPIO.setup(Plastic_MotorB,GPIO.OUT)
        GPIO.setup(Glass_MotorA,GPIO.OUT)
        GPIO.setup(Glass_MotorB,GPIO.OUT)
	l = readBarcode()
        print "Result" ,l
        for j in range(0,5):
            if StudentInfo.stud_id[j] == l:
                       for i in range(0,4):
                               print "scan your item barcode"
                               StudentInfo.stud_score[j] = StudentInfo.stud_score[j] + 1
                               print "score: ",StudentInfo.stud_score[j]
                               m = readBarcode()
                               if metal_barcode[i] == m:
                                      GPIO.output(Metal_MotorA,GPIO.HIGH)
                                      GPIO.output(Metal_MotorB,GPIO.LOW)
                                      sleep(2)
                                      GPIO.output(Metal_MotorA,GPIO.LOW)
                                      GPIO.output(Metal_MotorB,GPIO.LOW)
                                      sleep(3)
                                      GPIO.output(Metal_MotorA,GPIO.LOW)
                                      GPIO.output(Metal_MotorB,GPIO.HIGH)
                                      sleep(0.5)
                                      GPIO.output(Metal_MotorA,GPIO.LOW)
                                      GPIO.output(Metal_MotorB,GPIO.LOW)
                               elif paper_barcode[i] == m:
                                      GPIO.output(Paper_MotorA,GPIO.HIGH)
                                      GPIO.output(Paper_MotorB,GPIO.LOW)
                                      sleep(2)
                                      GPIO.output(Paper_MotorA,GPIO.LOW)
                                      GPIO.output(Paper_MotorB,GPIO.LOW)
                                      sleep(3)
                                      GPIO.output(Paper_MotorA,GPIO.LOW)
                                      GPIO.output(Paper_MotorB,GPIO.HIGH)
                                      sleep(0.5)
                                      GPIO.output(Paper_MotorA,GPIO.LOW)
                                      GPIO.output(Paper_MotorB,GPIO.LOW)
                               elif plastic_barcode[i] == m:
                                      GPIO.output(Plastic_MotorA,GPIO.HIGH)
                                      GPIO.output(Plastic_MotorB,GPIO.LOW)
                                      sleep(2)
                                      GPIO.output(Plastic_MotorA,GPIO.LOW)
                                      GPIO.output(Plastic_MotorB,GPIO.LOW)
                                      sleep(3)
                                      GPIO.output(Plastic_MotorA,GPIO.LOW)
                                      GPIO.output(Plastic_MotorB,GPIO.HIGH)
                                      sleep(0.5)
                                      GPIO.output(Plastic_MotorA,GPIO.LOW)
                                      GPIO.output(Plastic_MotorB,GPIO.LOW)
                               elif glass_barcode[i] == m:
                                      GPIO.output(Glass_MotorA,GPIO.HIGH)
                                      GPIO.output(Glass_MotorB,GPIO.LOW)
                                      sleep(2)
                                      GPIO.output(Glass_MotorA,GPIO.LOW)
                                      GPIO.output(Glass_MotorB,GPIO.LOW)
                                      sleep(3)
                                      GPIO.output(Glass_MotorA,GPIO.LOW)
                                      GPIO.output(Glass_MotorB,GPIO.HIGH)
                                      sleep(0.5)
                                      GPIO.output(Glass_MotorA,GPIO.LOW)
                                      GPIO.output(Glass_MotorB,GPIO.LOW)
            elif Workers_id[j] == l:
                                      GPIO.output(Metal_MotorA,GPIO.HIGH)
                                      GPIO.output(Metal_MotorB,GPIO.LOW)
                                      GPIO.output(Paper_MotorA,GPIO.HIGH)
                                      GPIO.output(Paper_MotorB,GPIO.LOW)
                                      GPIO.output(Plastic_MotorA,GPIO.HIGH)
                                      GPIO.output(Plastic_MotorB,GPIO.LOW)
                                      GPIO.output(Glass_MotorA,GPIO.HIGH)
                                      GPIO.output(Glass_MotorB,GPIO.LOW)
                                      sleep(2)
                                      GPIO.output(Metal_MotorA,GPIO.LOW)
                                      GPIO.output(Metal_MotorB,GPIO.LOW)
                                      GPIO.output(Paper_MotorA,GPIO.LOW)
                                      GPIO.output(Paper_MotorB,GPIO.LOW)
                                      GPIO.output(Plastic_MotorA,GPIO.LOW)
                                      GPIO.output(Plastic_MotorB,GPIO.LOW)
                                      GPIO.output(Glass_MotorA,GPIO.LOW)
                                      GPIO.output(Glass_MotorB,GPIO.LOW)
                                      sleep(6)
                                      GPIO.output(Metal_MotorA,GPIO.LOW)
                                      GPIO.output(Metal_MotorB,GPIO.HIGH)
                                      GPIO.output(Paper_MotorA,GPIO.LOW)
                                      GPIO.output(Paper_MotorB,GPIO.HIGH)
                                      GPIO.output(Plastic_MotorA,GPIO.LOW)
                                      GPIO.output(Plastic_MotorB,GPIO.HIGH)
                                      GPIO.output(Glass_MotorA,GPIO.LOW)
                                      GPIO.output(Glass_MotorB,GPIO.HIGH)
                                      sleep(0.5)
                                      GPIO.output(Metal_MotorA,GPIO.LOW)
                                      GPIO.output(Metal_MotorB,GPIO.LOW)
                                      GPIO.output(Paper_MotorA,GPIO.LOW)
                                      GPIO.output(Paper_MotorB,GPIO.LOW)
                                      GPIO.output(Plastic_MotorA,GPIO.LOW)
                                      GPIO.output(Plastic_MotorB,GPIO.LOW)
                                      GPIO.output(Glass_MotorA,GPIO.LOW)
                                      GPIO.output(Glass_MotorB,GPIO.LOW)
                                      
#the barcode is like a keyboard i couldn't disable it from writing its output
#the code works fine but when you scan something it will write the value of the barcode
#on the screen but it does not affect your code.

