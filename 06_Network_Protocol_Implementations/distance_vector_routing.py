# Distance Vector project for CS 6250: Computer Networks
#
# This defines a DistanceVector (specialization of the Node class)
# that can run the Bellman-Ford algorithm. The TODOs are all related 
# to implementing BF. Students should modify this file as necessary,
# guided by the TODO comments and the assignment instructions. This 
# is the only file that needs to be modified to complete the project.
#
# Student code should NOT access the following members, otherwise they may violate
# the spirit of the project:
#
# topolink (parameter passed to initialization function)
# self.topology (link to the greater topology structure used for message passing)
#
# Copyright 2017 Michael D. Brown
# Based on prior work by Dave Lillethun, Sean Donovan, Jeffrey Randow, new VM fixes by Jared Scott and James Lohse.
from Node import *
from helpers import *

class DistanceVector(Node):
    def __init__(self, name, topolink, outgoing_links, incoming_links):
        super(DistanceVector, self).__init__(name, topolink, outgoing_links, incoming_links)
        self.disVec = {self.name: 0}

    def send_initial_messages(self):
        for incoming_link in self.incoming_links:
            link_name = incoming_link.name
            self.send_message(link_name)

    def send_message(self, link_name):
        msg = dict()
        msg["origin_node"] = self.name
        msg["origin_node_distance_vector"] = self.disVec
        self.send_msg(msg, link_name)

    def process_BF(self):
        TruthChecker = False

        for index in range(len(self.messages)):
            msg = self.messages[index]
            TruthChecker = self.process_message(msg) or TruthChecker

        self.messages = []

        if TruthChecker:
            self.send_initial_messages()

    def process_message(self, msg):
        TruthChecker = False

        origin_node = msg['origin_node']
        origin_node_distance_vector = msg['origin_node_distance_vector']

        for vector_name in origin_node_distance_vector:
            vectorweight = origin_node_distance_vector[vector_name]
            if self.name != vector_name:
                TruthChecker = self.update_distance_vector(origin_node, vector_name, int(vectorweight)) or TruthChecker

        return TruthChecker

    def update_distance_vector(self, origin_node, vector_name, vectorweight):
        OrginSeeker = int(self.get_outgoing_neighbor_weight(origin_node))
        FinalCost = vectorweight + OrginSeeker
        TruthChecker = False

        if vector_name not in self.disVec:
            self.disVec[vector_name] = FinalCost
            TruthChecker = True
        else:
            currentCost = self.disVec[vector_name]
            if currentCost != -500:
                if FinalCost <= -500:
                    self.disVec[vector_name] = -500
                    TruthChecker = True
                elif FinalCost < currentCost:
                    self.disVec[vector_name] = FinalCost
                    TruthChecker = True
        return TruthChecker

    def log_distances(self):
        distVecStr = self.create_dis_vec_string()
        add_entry(self.name, distVecStr)

    def create_dis_vec_string(self):
        distVecStr = ""

        for name in sorted(self.disVec):
            weight = self.disVec[name]
            if weight <= -100:
                weight = -99

            distVecStr += "{}{}".format(name, weight)
            distVecStr += ","
        distVecStr = distVecStr[:-1]

        return distVecStr