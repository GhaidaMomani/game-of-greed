# Lab: Game of Greed 1

**Authors**:

    Ammar Abul-Feilat
    Salim Hassouneh
    Mohammad Salhab  
    Ghaida Al Momani

---

**Version**: 0.1.0

## Overview

The classic dice game of all or nothing! Greed is quick to learn and impossible to put down! To win the game, players need to obtain the highest score over 10,000 points. Roll all six dice, take out the dice which score, and roll again. Players may roll as long as they score, but don't get too greedy or you'll lose it all!

---

# Calculate Score

    zilch - roll with no scoring dice should return 0
    ones - rolls with various number of 1s should return correct score
    twos - rolls with various number of 2s should return correct score
    threes - rolls with various number of 3s should return correct score
    fours - rolls with various number of 4s should return correct score
    fives - rolls with various number of 5s should return correct score
    sixes - rolls with various number of 6s should return correct score
    straight - 1,2,3,4,5,6 should return correct score
    three_pairs - 3 pairs should return correct score
    two_trios - 2 sets of 3 should return correct score
    leftover_ones - 1s not used in set of 3 (or greater) should return correct score
    leftover_fives - 5s not used in set of 3 (or greater) should return correct score

## Architecture

This app is written using Python 3.9.5, following best practices.

## Change Log

version 0.1.0 ; 14/3/2022 Initiated
