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

class DTLearner:
    def __init__(self, leaf_size=1, verbose=False):
        self.leaf_size = leaf_size

        self.verbose = verbose

        self.tree = None

    def author(self):
        return 'nanyanwu3'

    def add_evidence(self, data_x, data_y):

        newdata = np.hstack((data_x, data_y.reshape(data_y.shape[0], -1)))

        self.tree = self.create_tree(newdata)

    def create_tree(self, data):

        if data.shape[0] <= self.leaf_size:

            return np.array([[-1, data[:, -1].mean(), np.nan, np.nan]])

        if np.all(data[:, -1] == data[0, -1]):

            return np.array([[-1, data[0, -1], np.nan, np.nan]])

        link = np.array([np.corrcoef(data[:, i], data[:, -1])[0, 1]
                                 for i in range(data.shape[1] - 1)])
        b_feat = np.argmax(np.abs(link))

        split_value = np.median(data[:, b_feat])

        l_data = data[data[:, b_feat] <= split_value]

        r_data = data[data[:, b_feat] > split_value]

        if len(l_data) == 0 or len(r_data) == 0:
            return np.array([[-1, data[:, -1].mean(), np.nan, np.nan]])


        l_tree = self.create_tree(l_data)

        r_tree = self.create_tree(r_data)

        theroot = np.array([[b_feat, split_value, 1, l_tree.shape[0] + 1]])

        return np.vstack((theroot, l_tree, r_tree))

    def query(self, points):

        predictions = np.array([self.query_thepoint(point) for point in points])
        return predictions

    def query_thepoint(self, point):

        node = 0
        while self.tree[node, 0] != -1:
            feature = int(self.tree[node, 0])
            split_val = self.tree[node, 1]

            if point[feature] <= split_val:
                node += int(self.tree[node, 2])
            else:
                node += int(self.tree[node, 3])

        return self.tree[node, 1]