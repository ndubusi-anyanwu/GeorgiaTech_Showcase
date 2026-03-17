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

import pandas as pd
import datetime as dt
import util as ut
from indicators import sma, bollinger_bands, cci


def author():
    return "nanyanwu3"  # Replace with your GT username


class ManualStrategy:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def testPolicy(
        self,
        symbol="JPM",
        sd=dt.datetime(2008, 1, 1),
        ed=dt.datetime(2009, 12, 31),
        sv=100000,
    ):

        # Get price data
        dates = pd.date_range(sd, ed)
        prices = ut.get_data([symbol], dates)[symbol]

        # Ensure no missing data
        prices = prices.dropna()

        # Compute
        sma_values = sma(prices).dropna()
        bb_values = bollinger_bands(prices).dropna()
        cci_values = cci(prices).dropna()

        # Align indicators
        indicators = pd.DataFrame(index=prices.index)
        indicators["SMA"] = sma_values
        indicators["BB"] = bb_values
        indicators["CCI"] = cci_values
        indicators = indicators.dropna()  # Remove rows with missing values

        # Create a DataFrame
        trades = pd.DataFrame(0, index=prices.index, columns=[symbol])

        # Rule-based trading logic
        position = 0  # Tracks current position (1000, 0, or -1000 shares)
        for i in range(len(indicators)):
            # Oversold : Buy
            if (
                indicators["BB"].iloc[i] < 0.2
                and indicators["CCI"].iloc[i] < -100
                and position == 0
            ):
                trades.iloc[i] = 1000  # Enter a long position
                position = 1000

            # Overbought : Sell
            elif (
                indicators["BB"].iloc[i] > 0.8
                and indicators["CCI"].iloc[i] > 100
                and position == 1000
            ):
                trades.iloc[i] = -1000  # Exit the long position
                position = 0

            # Hold position otherwise
            else:
                trades.iloc[i] = 0

        # Ensure trades reflect changes in position (-1000, 0, or +1000)
        trades[symbol] = trades[symbol].cumsum().clip(-1000, 1000).diff().fillna(0)

        if self.verbose:
            print(trades)

        return trades
