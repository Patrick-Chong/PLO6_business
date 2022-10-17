The bot will play according to this:
- I will follow the teaching of the Omaha books, and only play hands with REAL value.
- There will be 3 functions that will help to 'value' our current hand that we will use to reach our decision on what to do, namely suitedAce(), highPair(), Wrap(), and also a special handsToPlayFromAnyPosition().


Assumtions: 
- we are on a 0.3/0.6 table.
- we will not return anything until the very end, we will only return the action; i.e. call, raise/bet, fold, check. 
- any function that ends with the name 'action' means it will return one of the actions. 


How the bot will work:
The entire bot will consist of three parts; PRE_flop_play, POST_flop_play  +2 mixin (identifying positions & acion-behind me).


Mixins: 
- Both mixins will run everytime it is my turn to act- make it easier as it is not much computationally for the computer- identify_positions_mixin.py will run first as action_behind_me_mixin.py inherits from this.

1. In PRE_PRE_flop_play, we identify: 
	- which seats are still in the pot; 
	- whether it's multiway or hu; 
	- my relative position to the button. 


2. In PRE_flop_play (i.e. before the 3 community cards are shown there is a round of betting), we:
	- state the 3 functions that will determine if we play a hand or not. 
	- the combinations of these 3 functions - there are 6 in total (+1 hand to play from any position. 
	- 

1. Continuously move from one table to the next, simpyl by clicking on each of the 4 tables one by one
2. Then determine when it is our turn to act (this will be indicated by a timebar running down- this is the amount of time we have to act, otherwise it will automatically FOLD our current hand)
3. Read our current hand- total of 6 cards- and create two lists num_list and suit_list; where the former will hold the numbers of the 6 cards, and the latter will hold the suits of the 6 cards
4. Insert these two lists into my Python play log script, and then should do one of three thigns(fold, call, raise/bet); this is done by clicking the 'fold' or 'call' button, or in the case of 'raise/bet' it should click the button and enter the amoutn to raise/bet to. 


For POST-FLOP(i.e. after PRE-FLOP betting, 3 community cards will be dealt where there is another round of betting, then a 4th card will be dealth where there is yet another round of betting, then a 5th and final card will be dealt with a final round of betting)- POST-FLOP there is a total of 3 round of betting inbetween each community card being dealt. 
