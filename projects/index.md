---
title: Seleted projecs that I am involved
date: 2016-12-01 00:00:32
---
## Tic Tac Toe AI using MDP and Q-learning

Tic Tac Toe is classic board game and the [algorithmic approach](https://en.wikipedia.org/wiki/Minimax) of designing AI for it has been extensively studies, which usually requires building model according to the rules of game. It is desirable if we can design an AI without having the knowledge of the rule but by letting the agent **learn how to play** simply by trial and error. 

![Q-learning](../../assets/Q-learning.png)

<!-- Some questions remains:
- How do we trade-off between exploration and exploitation?
- How do we design the decay of discount rate? -->

This project addresses this issue by using model-free Q-learning. That is, the agent won't be able to, or need to, understand the rule of the game. It masters the game by playing it for many times, usually more than 10 thousands of time.

As the total number (5478) of game states of TicTacToe is manageable, we can use a simple Q function - a Python dictionary. 

The following video shows the Q value of different possible actions in the board (i.e. where to put the 'X' or 'O'). The agent always choose the highest Q value because Q value is a quantitative measure of how good the move is.

{% video '<iframe src="https://player.vimeo.com/video/193814558" width="640" height="845" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
<p><a href="https://vimeo.com/193814558">Tic Tac Toe AI</a> from <a href="https://vimeo.com/user28072024">Jason</a> on <a href="https://vimeo.com">Vimeo</a>.</p>' %}