""""""
"""  		  	   		 	   		  		  		    	 		 		   		 		  
Template for implementing QLearner  (c) 2015 Tucker Balch  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 	   		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		 	   		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 	   		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		 	   		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		 	   		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		 	   		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	   		  		  		    	 		 		   		 		  
or edited.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		 	   		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		 	   		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 	   		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
Student Name: Ndubusi Anyanwu (replace with your name)  		  	   		 	   		  		  		    	 		 		   		 		  
GT User ID: nanyanwu3 (replace with your User ID)  		  	   		 	   		  		  		    	 		 		   		 		  
"""

import numpy as nlp
import random

class QLearner(object):
    def __init__(
        self,
        num_states,
        num_actions,
        alpha=0.2,
        gamma=0.9,
        rar=0.5,
        radr=0.99,
        dyna=0,
        verbose=False,


    ):
        """
        My Constructor
        """
        self.gamma = gamma  # Discount

        self.rar = rar      # Random

        self.radr = radr    # Random  decay rate

        self.dyna = dyna    # Dyna-Q iterations

        self.verbose = verbose

        self.num_actions = num_actions

        self.num_states = num_states

        self.alpha = alpha  #  rate


        # Create my table to start

        self.Q = nlp.zeros((num_states, num_actions))

        # THis is for the  Dyna-Q model
        self.model = {} if self.dyna > 0 else None

        # create state
        self.s = 0
        # create  acction
        self.a = 0

    def choose_action(self, state):
        """
        EPS strategy
        """
        if random.uniform(0, 1) < self.rar:
            newaction = random.randint(0, self.num_actions - 1)

        else:
            newaction = nlp.argmax(self.Q[state, :])


        return newaction

    def querysetstate(self, s):
        """
        Get state without updating qtable
        """
        # create state
        self.s = s
        action = self.choose_action(s)
        #  action
        self.a = action
        if self.verbose:
            print(f"q-state: s = {s}, a = {action}")
        return action

    def query(self, s_prime, r):
        """
        Update the Q-table, choose next action, decay rar, and return the action.
        """
        # Update Q-Table
        best_nxt_act = nlp.argmax(self.Q[s_prime, :])
        self.Q[self.s, self.a] += self.alpha * (
            r + self.gamma * self.Q[s_prime, best_nxt_act] - self.Q[self.s, self.a]
        )

        # Update the model with the new experience for D-Q
        if self.dyna > 0:
            self.model[(self.s, self.a)] = (r, s_prime)
            self.run_dyna()

        # Decay random action rate
        self.rar *= self.radr

        # Choose next action
        action = self.choose_action(s_prime)
        self.s = s_prime
        self.a = action

        if self.verbose:
            print(f"query: s = {s_prime}, a = {action}, r = {r}")

        return action

    def run_dyna(self):
        """
        Perform Dyna-Q
        """
        if self.model:
            for _ in range(self.dyna):
                # Randomly sample a state-action pair

                (s, a), (r, s_prime) = random.choice(list(self.model.items()))
                # Update Q-table

                #best_nxt_act = nlp.argmax(self.Q[s_prime-1, :])
                best_nxt_act = nlp.argmax(self.Q[s_prime, :])

                # self.Q[s, a] += self.alpha * (
                #    r + self.gamma * self.Q[s_prime, best_nxt_act] + self.Q[s, a]
                #)
                self.Q[s, a] += self.alpha * (
                    r + self.gamma * self.Q[s_prime, best_nxt_act] - self.Q[s, a]
                )

    def author(self):
        return "nanyanwu3"
    def study_group(self):
        return "nanyanwu3"


if __name__ == "__main__":
    # Example usage:
    #print("Remember Q from Star Trek? Well, this isn't him")
    learner = QLearner(
        num_states=100,
        num_actions=4,
        alpha=0.2,
        gamma=0.9,
        rar=0.5,
        radr=0.99,
        dyna=200,
        verbose=True,
    )
    # learner = QLearner(
    #     num_states=100,
    #     num_actions=4,
    #     alpha=0.5,
    #     gamma=0.7,
    #     rar=0.1,
    #     radr=0.99,
    #     dyna=200,
    #     verbose=False,
    # )
    # learner = QLearner(
    #     num_states=100,
    #     num_actions=4,
    #     alpha=0.3,
    #     gamma=0.9,
    #     rar=0.6,       `
    #     radr=0.98,
    #     dyna=100,
    #     verbose=True,
    # )
    # learner = QLearner(
    #     num_states=100,
    #     num_actions=4,
    #     alpha=0.1,
    #     gamma=0.95,
    #     rar=0.2,
    #     radr=0.99,
    #     dyna=150,
    #     verbose=False,
    # )
    # loop for testing
    s = 0  # Initial state
    a = learner.querysetstate(s)
    for _ in range(10):
        s_prime = (s + 1) % learner.num_states
        r = -1
        a = learner.query(s_prime, r)
        s = s_prime
