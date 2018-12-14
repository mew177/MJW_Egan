#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 16:24:34 2018

@author: Egan
"""

from Deck import Deck

def newGame():
    deck = Deck()
    deck.shuffle()
    return deck


print("Welcome to Black Jack Playroom!!")
total = 500
bet = 500
while(total > 0):
    # welcome in
    print("*** You now have ${} ***".format(total))
    # place bet
    bet = input("Please enter your bet: $")
    bet = int(bet)
    if bet <= total:
        total -= bet
        EndGame = False
        deck = newGame()
        player, banker = [], []
        while not EndGame:
            player.append(deck.draw())
            banker.append(deck.draw())
            print("Cards in hand:")
            for card in player:
                print(card)
            if not input("Draw another card?[Y/N]") == "Y":
                EndGame = True 
        
    else:
        print("You don't have enough money.")


        
        