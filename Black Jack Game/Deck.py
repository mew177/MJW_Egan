#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 16:53:39 2018

@author: Rycemond
"""

from random import shuffle
from Card import Card
    
class Deck:
    deck = []
    suits = ["Diamond", "Heart", "Spade", "Club"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    def __init__(self):
        cards = [[Card(suit, rank) for suit in self.suits] for rank in self.ranks]
        for card in cards:
            self.deck += card
            
    def shuffle(self):
        shuffle(self.deck)
        
    def draw(self):
        return self.deck.pop()
        
    def showDeck(self):
        for card in self.deck:
            print(card)