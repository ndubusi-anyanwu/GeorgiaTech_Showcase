"""
  		  	   		 	   		  		  		    	 		 		   		 		  
Usage:  		  	   		 	   		  		  		    	 		 		   		 		  
- Switch to a student feedback directory first (will write "points.txt" and "comments.txt" in pwd).  		  	   		 	   		  		  		    	 		 		   		 		  
- Run this script with both ml4t/ and student solution in PYTHONPATH, e.g.:  		  	   		 	   		  		  		    	 		 		   		 		  
    PYTHONPATH=ml4t:MC3-P1/jdoe7 python ml4t/mc3_p1_grading/grade_learners.py  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
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
"""  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  


import numpy as np

from BagLearner import BagLearner

from LinRegLearner import LinRegLearner

class InsaneLearner:
    def __init__(self, learner=LinRegLearner, kwargs={}, bags=20, verbose=False):
        self.verbose = verbose
        self.bag_learners = [BagLearner(learner=learner, kwargs=kwargs, bags=20, verbose=verbose) for _ in range(bags)]

    def add_evidence(self, data_x, data_y):
        for learner in self.bag_learners:
            learner.add_evidence(data_x, data_y)

    def query(self, points):
        newpredict = np.array([learner.query(points) for learner in self.bag_learners])
        return np.mean(newpredict, axis=0)

    def author(self):
        return "nanyanwu3"

