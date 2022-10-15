"""
Here we will identify whether we are in a "multiway pot or hu", and "if we are IP or OOP".

We analyse positions in the playerPosition class:
- From the button, we will go clockwise and label each opponent (including ourselves) 1 - 6 ; i.e. 6 will be the button.
- Start with determining the number of players in the pot (multiway or hu pot)
- Then my whether I am IP or OOP - in a multiway pot I will only be IP if I am last to act.
- Finally it also calculates my exact position (relative to button); 6 being best and 1 being worst

""""


#The following class playerPosition will be the base class that we run every time it is our turn; this is the first thing we must run everytime, since players fold before and after each hand so this accounts for it. 

from collections import defaultdict
class playerPosition:
	def __init__(self, opp1, opp2, opp3, opp4, opp5, opp6): 
		self.opponents_in_pot = defaultdict(bool)
		number_of_players_in_pot = 0 
		self.multiway = False 
		self.hu = False
		self.my_position = float("inf")
		self.my_in_position = False
		
	
	def fill_opponents_in_pot_dict(self, opponents_in_pot): 
		#need some Ocular/Tesseract magic to destermine if players are still in the hand (they will be greyed out on screen if they've folded
		#########RUN TESSERACT TO FILL THIS########
		self.opponents_in_pot[1] = True/False 
		self.opponents_in_pot[2] = True/False
		...
		self.opponents_in_pot[6] = True/False  
		
		multiway_or_hu_pot(self, opponents_in_pot, *args)
	
	def multiway_or_hu_pot(self, opponents_in_pot, multiway, hu, opponents_in_pot): 
		number_of_players_in_pot = 0 
		for player in self.opponents_in_pot: 
			if opponents_in_pot[player] == True: 
				number_of_players_in_pot += 1
		
		if number_of_players_in_pot >2:
			self.multiway = True 
		else:
			self.hu = True 
			
		self.my_relative_position(self)
	
	#Determine position of button, then where we are and where opps are relative to it, thus if we are IP or OOP
	#Need Ocular/Tesseract to see where the button is, or where I am relative to button
	#my_position == 0 if I am on the button, 1 if I am to the direct left of button, 2 if two away from button, etc. 
	def my_relative_position(self): 
		self.my_position = #########RUN TESSERACT TO FILL THIS########
		if self.hu: 
			if self.my_position == 6: 
				self.my_in_position = True
			
			else: 
				temp = self.my_position - 1 
				for i in range(temp): 
					if self.opponents_in_pot[i] == True: 
						my_in_position = False 
		
		else: #multiway 
			temp = 6 - self.my_position - 1
			if any(self.opponents_in_pot[i] == True for i in range(temp, 6):
				my_in_position = False 
			else: 
				my_in_position = True 
				
			
