"""
I'll need to add adjustments ot the code below to factor for if there are fewer players in the pot, since below - I think the only adjustment will be to my_relative_position, everything else should be fine since it is based on the position of the button. 

We start by inheriting from class playerPosition, so we know if we are in a multiway or hu pot. Also, we will know if we are ip or oop. 

class PreFlopHandCombinations is 
- Used to set up the 3 criterias for 'playable hands', namely wrap, highPair or suited ace'. 
- Then we look at all combinations (6 in total) of these 3 criterias. 

class PreFlopPlay:
- Start by checking if we have a good enough hand to play from any position (if so it will return call, bet/raise, etc)

I NEED TO ADD A CLASS THAT DETERMINES THE ACTION BEHIND ME SO FAR. THIS IS FOR PRE-FLOP BUT I'LL ALSO NEED IT FOR POST FLOP, BUT THAT'S IN A DIFFERENT SCRIPT. 
THIS IS WHERE KNOWING WHAT POSITION I AM IN WILL HELP.
AND ALSO WHAT THE STAKES OF THE TABLE IS, because then I know whether it has been 3-bet or more or less. 



EXTRA NOTES:

- Note the 'raise'/'bet' button always says 'bet' after the flop and 'raise' before the flop; but they represent the same thing. 
- #Note that hands are always dealt with the HIGHEST CARD to the far left and the LOWEST CARD to the far right, this should help a lot with indexing;
	#nums_list = [2,3,4,5,6,7,8,9,10,11,12,13,14] ; 11=J, 12=Q, 13=K, 14=A
	#suit_list = ['Diamonds','Clubs','Hearts','Spades'] = ['D','C','H','S']
	#e.g. nums_list = [13,12,12,7,5,3] , suit_list = ['D','D','C','H','S','S']


"""

from home.plo6.mixin import action_behind_me_mixin

from collections import defaultdict


class PreFlopHandCombinations(ActionBehindMe): 
	def __init__(self,nums_list, suit_list, suited_ace, high_pair, oneHighPair, twoHighPair):
		super().__init__()
		self.nums_list = []
		self.suit_list = []
		self.suited_ace = False
		self.oneHighPair = False
		self.twoHighPair = False
		self.wrap = False
		
		#Below when I say 'bet', I mean always bet POT
	
	
	def fill_my_hand(self, nums_list, suit_list): 
		######tesseract/OCR to fill in nums_list and suit_list#########
	

	#determines if we have a suited ace in our hand
	def suitedAce(self, nums_list, suit_list):
		#suited ace: 
		self.nums_list[0] == 14 and self.suit_list[0] >1: 
			self.suited_ace = True

	#determines if we have one high pair, two high pairs or no high pair
	def highPair(self, nums_list, suit_list, oneHighPair, twoHighPair): 
		dict_of_numbers = defaultdict(int)
		for i in self.nums_list: 
			dict_of_numbers[i] += 1

		number_of_high_pairs = 0 

		for i in dict_of_numbers: 
			if i >= 10 and dict_of_numbers[i] >=2: 
				number_of_high_pairs += 1

		if number_of_high_pairs == 2: 
			self.twoHighPair = True 

		elif number_of_high_pairs == 1: 
			self.oneHighPair = True


	#this function determines if there is any full wrap potential in our hand (with smallest card being 5, e.g. smallest no gap wrap is 5,6,7)
	def Wrap(self, nums_list, suit_list):
		current_three = []
		for i in range(len(self.nums_list)-3): 
			if self.nums_list[i] <5: 
				break
			current_three.append(self.nums_list[i])
			current_three.append(self.nums_list[i+1])
			current_three.append(self.nums_list[i+2])

			#if pair in current three
			if len(set(current_three)) <3: 
				continue

			#Calculate if we have a potential full-wrap; 3 ways to achieve this
			total_gap = 0 
			for i in range(0, len(current_three)-2):
				total_gap += current_three[i] - current_three[i+1]

			if total_gap = 2: 
				self.wrap = True

			if total_gap = 3: 
				self.wrap = True   #note that one_gapper hgih or low and no_gapper have the same full wrap potential

			current_three = []
	
	
	def hand_combinations(self): 
		if self.suited_ace and self.oneHighPair: 
			self.suited_ace_one_pair = True
		if self.suited_ace and self.twoHighPair: 
			self.suited_ace_two_pair = True
		if self.suited_ace and self.wrap: 
			self.suited_ace_wrap = True
		if self.oneHighPair and self.wrap: 
			self.one_pair_wrap = True
		if self.TwoHighPair and self.wrap: 
			self.two_pair_wrap = True
	
	
class PreflopPlay(): 
	
	def __init__(self):
		PreFlopHandCombinations.__init__(self)
		ActionBehindMe.__init__(self)
		self.suited_ace_one_pair = False
		self.suited_ace_two_pair = False
		self.suited_ace_wrap = False
		self.one_pair_wrap = False
		self.two_pair_wrap = False

		self.no_raise = False 
		self.one_raise = False
		self.three_bet = false 

		
	def handsToPlayFromAnyPosition(self, nums_list, suit_list):
		#Double suited kings (add kings with straight 3 run down)
		if (self.nums_list[0], self.nums_list[1]) == (13,13):
			if self.suit_list[0] >1 and self.suit_list[1] >1: 
				return 'bet' or 'call (if previously raised, but fold to three bet)' 

		if  (self.nums_list[1], self.nums_list[2]) == (13,13) #if there's an ace, thekings will be in position 1,2 in nums_list
			if self.suit_list[1] >1 and self.suit_list[2] >1: 
				return 'bet' or 'call (if previously raised, but fold to three bet)' 

		#Double suited aces	
		if (self.nums_list[0],self.nums_list[1]) == (14,14):
			if self.suit_list[0] >1 and self.suit_list[1] >1: 
				return 'bet max' or 'raise max' #get all the money in is poss


		#Single suited ace + either 3 run down with one gapper anywhere OR a high pair
		if self.suited_ace: 
			if connectivityWrapPotential(self, nums_list, suit_list): 
				return 'bet' or 'call (if previously raised, but fold to three bet)'

			if self.high_pair:
				return 'bet' or 'call (if previously raised, but fold to three bet)'

			#if just suited ace alone
			return 'call, only to a single raise, and if it has not been three bet' or 'check'
		
		return None
	
	
	
	""" Need to finish filling
	#refer to PRE-FLOP logic notes to see what action to take in each hand scenario
	def pre_flop_play_action(self, nums_list, suit_list):
		
		if handsToplayfromAnyposition: 
			#play as stated by function 
		
		else: #on button or button + 1
			if self.my_position in (0,1): 
				if any(self.two_pair_wrap, self.one_pair_wrap, self.suited_ace_wrap, self.suited_ace_two_pair, 			
					self.suited_ace_one_pair):
						return 'call' 
						
		
		
		.... 
		check_flop = ActionBehindMe()
		check_flop.check_if_still_on_flop()
		
						
				
			
		
	
	
	


	




