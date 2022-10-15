#at this point pre-flop decision has been made, and we should only run this script if the result of the PRE-FLOP play was NOT 'fold'; 
"""
POST-FLOP PLAY




We now have enough info to calculate odds, etc for each of the post flop (3) streets of betting; let's break flop, turn and river into three classes. 

- Then calcualte SPR of each player in the pot before betting; not just largest SPR, because this player may fold. 
(Note that SPR is nothing more than calculating how many times of the pot the opponent has!) 

""""


#Each time we need to make a post flop deiciosn, we will run the following player_profile_class




	
	#need tesseract to input opponent's stack
	def stackToPotRatioOfEachOpponent(self): 
		if self.opp1: 
			self.opp1_SPR = SPRCalculator(opp1_stack, pot) 
		if self.opp2: 
			self.opp2_SPR = SPRCalculator(opp2_stack, pot) 
		if self.opp3: 
			self.opp3_SPR = SPRCalculator(opp3_stack, pot) 
		if self.opp4: 
			self.opp4_SPR = SPRCalculator(opp4_stack, pot) 
		if self.opp5: 
			self.opp5_SPR = SPRCalculator(opp5_stack, pot) 
	
	
	def myOutsPercentage(self, hand): 
		
	
	#calculate my equity and return if I should check/bet/call on current street
	def myEquityCalculator(self, my_stack, bet_to_call, pot):
		if bet:
			myEquity = bet_to_call / (pot + "opponents' called money") 
		else: 	
			myEquity = bet_to_call / pot
		
		myOutsPercentage = OutsPercentageCalculator()
		 
		 if myOutsPercentage >= myEquity:
		 	return 'call' 
		 
		 
		
	

class Postflopplay:


	def on_flop(self):
		return 'play flop'
			


	def on_turn()
		return 'play turn'

	def on_river()
		return 'play river'
