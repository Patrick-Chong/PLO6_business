"""
Aciton_behind_me_pre_flop will record how much each person behind me has bet. And since we are playing on 0.3/0.6 tables, we will be able to determine if the pot has been bet/3-bet/called; this will of course determine what our action will be!

All other scripts that determine what action I take should inherit from this script.
"""

from home.plo6.mixins import identifying_positions_mixin.py
from home.plo6.1.PRE_flop_play import PreFlopHandCombinations, PreflopPlay

from collections import defaultdict

class ActionBehindMe(playerPosition):
	
	def __init__(self): 
		super().__init__(self)
		self.pot = 0
		self.opp_bet_behind = defaultdict(float)
		self.called = False
		self.raised = False 
		self.three_bet = False
		self.move_to_flop = False
	
	
	# to record how much each opponent has bet so far behind us (this will be used to determine next whether we are in a bet/3-bet/call pot)
	def opponents_bet_behind_me(self): 
		self.opp_bet_behind[1] = #tesseract fill; if no bet then default to 0 - including if they're yet to act
		self.opp_bet_behind[2] = #tesseract fill
		self.opp_bet_behind[3] = #tesseract fill 
		self.opp_bet_behind[4] = #tesseract fill 
		self.opp_bet_behind[5] = #tesseract fill 
		self.opp_bet_behind[6] = #tesseract fill 
	
	
	def action_behind_me_pre_flop(self): 
		for i in range(len(self.opp_bet_behind)): #iterating over players behind me
			if not self.opponents_in_pot[i]: 
				pass 
			else: 
				if self.opp_bet < 1.19: #accounting for players with negligible stack.
					self.called = True
				elif self.opp_bet <= 1.80 and self.opp_bet >= 1.20: 
					self.raised = True
				else: 
					self.three_bet = True
	
	#Initialization- basically run all of pre_flop.py script! 
	handcombi = PreFlopHandCombinations(self, *args)
	handcombi.fill_my_hand(self, [], [])
	pre_flop = PreflopPlay(self)
	pre_flop.handsToPlayFromAnyPosition(self, nums_list, suit_list)
	pre_flop.pre_flop_play_action(self, nums_list, suit_list)
	
	
	def check_if_still_on_flop():
		#if we are still pre-flop; this can happen if there is any sort of raise after we act
		if not self.move_to_flop: 
			A = ActionBehindMe() 
			#Add more code here to:
			#Run the whole class ActionBehindMe again
		else: 
			pre_flop_play_action()
			
						
	
