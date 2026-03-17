"""
/*
 * Copyright © 2022 Georgia Institute of Technology (Georgia Tech). All Rights Reserved.
 * Template code for CS 6250 Computer Networks
 * Instructors: Maria Konte
 * Head TAs: Johann Lau and Ken Westdorp
 *
 * Georgia Tech asserts copyright ownership of this template and all derivative
 * works, including solutions to the projects assigned in this course. Students
 * and other users of this template code are advised not to share it with others
 * or to make it available on publicly viewable websites including repositories
 * such as GitHub and GitLab. This copyright statement should not be removed
 * or edited. Removing it will be considered an academic integrity issue.
 *
 * We do grant permission to share solutions privately with non-students such
 * as potential employers as long as this header remains in full. However,
 * sharing with other current or future students or using a medium to share
 * where the code is widely available on the internet is prohibited and
 * subject to being investigated as a GT honor code violation.
 * Please respect the intellectual ownership of the course materials
 * (including exam keys, project requirements, etc.) and do not distribute them
 * to anyone not enrolled in the class. Use of any previous semester course
 * materials, such as tests, quizzes, homework, projects, videos, and any other
 * coursework, is prohibited in this course.
 */
"""

# Spanning Tree Protocol project for GA Tech OMSCS CS-6250: Computer Networks
#
# Copyright 2022 Vincent Hu
#           Based on prior work by Sean Donovan, Jared Scott, James Lohse, and Michael Brown

"""
/*
 * Copyright © 2022 Georgia Institute of Technology (Georgia Tech). All Rights Reserved.
 * Template code for CS 6250 Computer Networks
 * Instructors: Maria Konte
 * Head TAs: Johann Lau and Ken Westdorp
 *
 * Georgia Tech asserts copyright ownership of this template and all derivative
 * works, including solutions to the projects assigned in this course. Students
 * and other users of this template code are advised not to share it with others
 * or to make it available on publicly viewable websites including repositories
 * such as GitHub and GitLab. This copyright statement should not be removed
 * or edited. Removing it will be considered an academic integrity issue.
 *
 * We do grant permission to share solutions privately with non-students such
 * as potential employers as long as this header remains in full. However,
 * sharing with other current or future students or using a medium to share
 * where the code is widely available on the internet is prohibited and
 * subject to being investigated as a GT honor code violation.
 * Please respect the intellectual ownership of the course materials
 * (including exam keys, project requirements, etc.) and do not distribute them
 * to anyone not enrolled in the class. Use of any previous semester course
 * materials, such as tests, quizzes, homework, projects, videos, and any other
 * coursework, is prohibited in this course.
 */
"""

# Spanning Tree Protocol project for GA Tech OMSCS CS-6250: Computer Networks
#
# Copyright 2022 Vincent Hu
#           Based on prior work by Sean Donovan, Jared Scott, James Lohse, and Michael Brown
from Message import Message
from StpSwitch import StpSwitch

class Switch(StpSwitch):
    def __init__(self, switchID: int, topolink: object, neighbors: list):
        super().__init__(switchID, topolink, neighbors)
        
        self.root = self.switchID
        #distance try 1
        self.distance = 0
        #
        self.active_links = []
        #
        self.path_through = None
#send message/logic
    def process_message(self, message: Message):
        if message.pathThrough:
            if message.origin not in self.active_links:
                self.active_links.append(message.origin)

        elif not message.pathThrough and message.origin != self.path_through and message.origin in self.active_links:
            self.active_links.remove(message.origin)

        if message.root < self.root:
            self.root = message.root
            self.distance = message.distance + 1
            self.path_through = message.origin
            if self.path_through not in self.active_links:
                self.active_links.append(self.path_through)
            for glue in self.links:
                new_message = Message(self.root, self.distance, self.switchID, glue, self.path_through == glue)
                self.send_message(new_message)

        if message.root == self.root and message.distance + 1 < self.distance:
            self.distance = message.distance + 1
            new_path_through = message.origin

            for glue in self.links:
                new_message = Message(self.root, self.distance, self.switchID, glue, new_path_through == glue)
                self.send_message(new_message)

            self.active_links.remove(self.path_through)
            self.path_through = new_path_through
            if new_path_through not in self.active_links:
                self.active_links.append(new_path_through)

        if message.root == self.root and message.distance + 1 == self.distance and self.path_through > message.origin:
            new_path_through = message.origin

            for glue in self.links:
                new_message = Message(self.root, self.distance, self.switchID, glue, new_path_through == glue)
                self.send_message(new_message)

            self.active_links.remove(self.path_through)
            self.path_through = new_path_through
            if new_path_through not in self.active_links:
                self.active_links.append(new_path_through)

    def generate_logstring(self):
        link_strings = []
        self.active_links.sort()
        for glue in self.active_links:
            link_strings.append(str(self.switchID) + ' - ' + str(glue))
        return ', '.join(link_strings)



