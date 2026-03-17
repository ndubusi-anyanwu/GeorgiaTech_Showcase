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


class RTLearner:
    def __init__(self, leaf_size=1, verbose=False):
        self.leaf_size = leaf_size
        self.verbose = verbose
        self.tree = None

    def author(self):
        return "nanyanwu3"

    def add_evidence(self, data_x, data_y):

        newdata = np.hstack((data_x, data_y.reshape(data_y.shape[0], -1)))
        self.tree = self.b_tree(newdata)

    def b_tree(self, data):

        if data.shape[0] <= self.leaf_size or len(set(data[:, -1])) == 1:
            return np.array([[-1, np.mean(data[:, -1]), np.nan, np.nan]])

        f_idx = np.random.randint(0, data.shape[1] - 1)

        split_value = np.median(data[:, f_idx])

        if np.all(data[:, f_idx] == data[0, f_idx]):
            return np.array([[-1, np.mean(data[:, -1]), np.nan, np.nan]])

        l_mask = data[:, f_idx] <= split_value
        r_mask = data[:, f_idx] > split_value

        if np.sum(l_mask) == 0 or np.sum(r_mask) == 0:
            return np.array([[-1, np.mean(data[:, -1]), np.nan, np.nan]])

        l_tree = self.b_tree(data[l_mask])
        r_tree = self.b_tree(data[r_mask])

        theroot = np.array([[f_idx, split_value, 1, l_tree.shape[0] + 1]])

        if self.verbose:
            print(f"Feature {f_idx}, split_value {split_value}")

        return np.vstack((theroot, l_tree, r_tree))

    def query(self, points):
        result = np.apply_along_axis(self.query_point, 1, points)
        return result

    def query_point(self, point):
        basenode = 0

        while self.tree[basenode, 0] != -1:
            newfeature = int(self.tree[basenode, 0])
            split_value = self.tree[basenode, 1]

            if point[newfeature] <= split_value:
                basenode += int(self.tree[basenode, 2])
            else:
                basenode += int(self.tree[basenode, 3])
        return self.tree[basenode, 1]



