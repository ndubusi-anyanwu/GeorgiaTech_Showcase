""""""
"""  		  	   		 	   		  		  		    	 		 		   		 		  
Template for implementing StrategyLearner  (c) 2016 Tucker Balch  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
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
  		  	   		 	   		  		  		    	 		 		   		 		  
Student Name: Tucker Balch (replace with your name)  		  	   		 	   		  		  		    	 		 		   		 		  
GT User ID: tb34 (replace with your User ID)  		  	   		 	   		  		  		    	 		 		   		 		  
"""

"""  
Template for implementing StrategyLearner  (c) 2016 Tucker Balch  

Copyright 2018, Georgia Institute of Technology (Georgia Tech)  
Atlanta, Georgia 30332  
All Rights Reserved  

Template code for CS 4646/7646  

Georgia Tech asserts copyright ownership of this template and all derivative  
works, including solutions to the projects assigned in this course. Students  
and other users of this template code are advised not to share it with others  
or to make it available on publicly viewable websites including repositories  
such as GitHub and GitLab. This copyright statement should not be removed  
or edited.  

We do grant permission to share solutions privately with non-students such  
as potential employers. However, sharing with other current or future  
students of CS 7646 is prohibited and subject to being investigated as a  
GT honor code violation.  

-----do not edit anything above this line---
"""
import datetime as dt
import pandas as pd
import numpy as np
import util as ut
from indicators import sma, bollinger_bands, rsi, macd, momentum, adx  # Ensure indicators.py includes these functions
from QLearner import QLearner
import matplotlib.pyplot as newplt


def author():
    return "nanyanwu3"


class StrategyLearner(object):


    def __init__(self, verbose=False, impact=0.0, commission=0.0):

        self.verbose = verbose
        self.impact = impact
        self.commission = commission


        self.num_bins = 3

        # indicators used
        self.num_indicators = 6

        # Number of possible positions
        self.num_positions = 3

        # Total number of states
        self.num_states = (self.num_bins ** self.num_indicators) * self.num_positions

        # Initialize Q-Learner
        self.learner = QLearner(
            num_states=self.num_states,
            num_actions=3,  # 0: Hold, 1: Buy, 2: Sell
            alpha=0.3,      # Further reduced learning rate for stability
            gamma=0.9,      # Maintained discount factor
            rar=0.95,       # High initial exploration rate
            radr=0.99,      # Slower decay to maintain exploration
            dyna=0,         # No planning steps
        )

    def add_evidence(self, symbol="IBM", sd=dt.datetime(2008, 1, 1),
                     ed=dt.datetime(2009, 12, 31), sv=10000):
        """Trains your strategy learner over a given time frame."""
        # Fetch price data
        thedates = pd.date_range(sd, ed)
        prices = ut.get_data([symbol], thedates)[symbol]
        prices = prices.fillna(method='ffill').fillna(method='bfill')

        if self.verbose:
            print("Price data head:\n", prices.head())

        # Compute
        theindicators = self._compute_indicators(prices)

        # Discretize
        theindicators = theindicators.dropna()
        discretized_indicators = self._discretize_indicators(theindicators)

        # Combine
        indicator_state_ids = self._combine_indicators(discretized_indicators)


        unique_indicator_states = indicator_state_ids.drop_duplicates().shape[0]
        tot_possible_states = self.num_bins ** self.num_indicators
        if unique_indicator_states > tot_possible_states:
            raise ValueError(
                f"Number of unique indicator states ({unique_indicator_states}) exceeds expected ({tot_possible_states})."
            )

        # Training phase
        num_episodes = 2000
        for episode in range(num_episodes):
            position = 0  # Start with no position
            self.learner.rar = max(0, self.learner.rar * self.learner.radr)  # Decay exploration rate

            for i in range(len(indicator_state_ids) - 1):
                cur_indicator_state = indicator_state_ids.iloc[i]
                current_state = cur_indicator_state * self.num_positions + position  # Include position in state

                # Action selection
                action = self.learner.querysetstate(current_state)


                reward = self._compute_reward(prices, action, position, i)

                # Update position
                new_position = position
                if action == 1 and position == 0:
                    new_position = 1  # Buy to go long
                elif action == 2 and position == 1:
                    new_position = 0  # Sell to go out
                elif action == 2 and position == 0:
                    new_position = 2  # Sell to go short
                elif action == 1 and position == 2:
                    new_position = 0  # Buy to go out from short


                # Next state
                nxt_ind_state = indicator_state_ids.iloc[i + 1]
                next_state = nxt_ind_state * self.num_positions + new_position

                # Q-Learner update
                self.learner.query(next_state, reward)

                # Update position for next iteration
                position = new_position

            # Optional: Periodic Logging
            if self.verbose and (episode + 1) % 500 == 0:
                print(f"Episode {episode + 1}/{num_episodes} completed.")

        if self.verbose:
            print("Training completed.")

    def testPolicy(self, symbol="IBM", sd=dt.datetime(2010, 1, 1),
                  ed=dt.datetime(2011, 12, 31), sv=10000):

        # Fetch price data
        dates = pd.date_range(sd, ed)
        prices = ut.get_data([symbol], dates)[symbol]
        prices = prices.fillna(method='ffill').fillna(method='bfill')

        # Compute indicators
        indicators = self._compute_indicators(prices)
        indicators = indicators.dropna()
        discretized_indicators = self._discretize_indicators(indicators)

        # Combine discretized indicators into unique state IDs
        indicator_state_ids = self._combine_indicators(discretized_indicators)

        # Initialize trades DataFrame
        trades = pd.DataFrame(0, index=prices.index, columns=[symbol], dtype=float)

        position = 0  # Start with no position

        for i in range(len(indicator_state_ids)):
            current_indicator_state = indicator_state_ids.iloc[i]
            current_state = current_indicator_state * self.num_positions + position  # Include position in state

            # Action selection
            action = self.learner.querysetstate(current_state)

            # Execute action
            if action == 1 and position == 0:
                trades.iloc[i] = 1000  # Buy 1000
                position = 1
            elif action == 2 and position == 1:
                trades.iloc[i] = -1000  # Sell 1000
                position = 0
            elif action == 2 and position == 0:
                trades.iloc[i] = -1000  # Sell 1000
                position = 2
            elif action == 1 and position == 2:
                trades.iloc[i] = 1000  # Buy 1000
                position = 0


        return trades

    def _compute_indicators(self, prices):

        sma_vals = sma(prices, window=20)
        bbp_vals = bollinger_bands(prices, window=20)
        rsi_vals = rsi(prices, window=14)
        macd_vals = macd(prices, fast_window=12, slow_window=26, signal_window=9)
        momentum_vals = momentum(prices, window=10)
        adx_vals = adx(prices, window=14)

        indicators = pd.concat([
            sma_vals,
            bbp_vals,
            rsi_vals,
            macd_vals,
            momentum_vals,
            adx_vals
        ], axis=1)
        indicators.columns = ["SMA", "BB", "RSI", "MACD", "Momentum", "ADX"]

        # Removed normalization
        return indicators

    def _discretize_indicators(self, indicators):

        discretized = indicators.copy()
        for col in indicators.columns:
            # Discretize each indicator
            discretized[col] = pd.qcut(
                indicators[col].rank(method='first'),
                q=self.num_bins,
                labels=False,
                duplicates='drop'
            )
        return discretized

    def _combine_indicators(self, discretized_indicators):


        state_id = 0
        for i, col in enumerate(discretized_indicators.columns[::-1]):  # Reverse to assign higher weights to earlier indicators
            state_id += discretized_indicators[col] * (self.num_bins ** i)
        return state_id.astype(int)

    def _compute_reward(self, prices, action, position, idx):

        if idx < len(prices) - 1:
            current_price = prices.iloc[idx]
            next_price = prices.iloc[idx + 1]
            price_change = next_price - current_price

            # Correct reward
            if position == 1:  # Long
                reward = price_change
            elif position == 2:  # Short
                reward = -price_change
            else:  # No position
                reward = 0

            # Subtract market impact cost
            reward -= self.impact * np.abs(position * price_change)

            # Subtract
            if action != 0:
                reward -= self.commission

            return reward
        return 0

    def plot_portfolio(self, prices, trades, sv=10000):

        # Compute
        holdings = trades.cumsum()

        # Compute
        cash = sv - (trades * prices).cumsum().sum(axis=1)

        # Compute portfolio value
        portfolio = holdings.mul(prices, axis=0).sum(axis=1) + cash

        newplt.figure(figsize=(10, 6))
        newplt.plot(portfolio, label='Portfolio Value')
        newplt.legend()
        newplt.xlabel('Date')
        newplt.ylabel('Portfolio Value')
        newplt.title('Portfolio Performance')
        newplt.show()



    # def run():
    #     learner = StrategyLearner(verbose=True)
    #     learner.add_evidence(
    #         symbol="JPM",
    #         sd=dt.datetime(2008, 1, 1),
    #         ed=dt.datetime(2009, 12, 31),
    #         sv=100000,
    #     )
    #     trades = learner.testPolicy(
    #         symbol="JPM",
    #         sd=dt.datetime(2010, 1, 1),
    #         ed=dt.datetime(2011, 12, 31),
    #         sv=100000,
    #     )
    #     print(trades)
    #
    #     # Fetch price data for visualization
    #     dates = pd.date_range(dt.datetime(2010, 1, 1), dt.datetime(2011, 12, 31))
    #     prices = ut.get_data(["JPM"], dates)["JPM"].fillna(method='ffill').fillna(method='bfill')
    #
    #     # Plot portfolio performance
    #     learner.plot_portfolio(prices, trades, sv=100000)

    if __name__ == "__main__":
        run()