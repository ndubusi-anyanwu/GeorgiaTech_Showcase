#!/usr/bin/env python3
from collections import defaultdict
import re
import pybgpstream

"""
CS 6250 BGP Measurements Project

Notes:
- Edit this file according to the project description and the docstrings provided for each function
- Do not change the existing function names or arguments
- You may add additional functions but they must be contained entirely in this file
"""


# Task 1A: Unique Advertised Prefixes Over Time
def unique_prefixes_by_snapshot(cache_files):
    """
    Retrieve the number of unique IP prefixes from each of the input BGP data files.

    Args:
        cache_files: A chronologically sorted list of absolute (also called "fully qualified") path names

    Returns:
        A list containing the number of unique IP prefixes for each input file.
        For example: [2, 5]
    """
    # the required return type is 'list' - you are welcome to define additional data structures, if needed
    unique_prefixes_by_snapshot = []



    for fpath in cache_files:
        stream = pybgpstream.BGPStream(data_interface="singlefile")
        stream.set_data_interface_option("singlefile", "rib-file", fpath)

        # implement your solution here

        prefixes = set()
        for elem in stream:
            if elem.type == "R" or elem.type == "A":
                prefixes.add(elem.fields['prefix'])
                
        unique_prefixes_by_snapshot.append(len(prefixes))



    return unique_prefixes_by_snapshot


# Task 1B: Unique Autonomous Systems Over Time
def unique_ases_by_snapshot(cache_files):
    """
    Retrieve the number of unique ASes from each of the input BGP data files.

    Args:
        cache_files: A chronologically sorted list of absolute (also called "fully qualified") path names

    Returns:
        A list containing the number of unique ASes for each input file.
        For example: [2, 5]
    """
    # the required return type is 'list' - you are welcome to define additional data structures, if needed
    
    
    
    unique_ases_by_snapshot = []



    for fpath in cache_files:
        stream = pybgpstream.BGPStream(data_interface="singlefile")
        stream.set_data_interface_option("singlefile", "rib-file", fpath)

        # implement your solution here
        ases = set()

        for elem in stream:
            if elem.type == "R" or elem.type == "A":
                as_path = elem.fields['as-path']
                ases.update(as_path.split())
        
        unique_ases_by_snapshot.append(len(ases))


    return unique_ases_by_snapshot


# Task 1C: Top-10 Origin AS by Prefix Growth


def top_10_ases_by_prefix_growth(cache_files):
    """
    Compute the top 10 origin ASes ordered by percentage increase (smallest to largest) of advertised prefixes.

    Args:
        cache_files: A chronologically sorted list of absolute (also called "fully qualified") path names

    Returns:
        A list of the top 10 origin ASes ordered by percentage increase (smallest to largest) of advertised prefixes
        AS numbers are represented as strings. In the event of a tie, the AS with the lower number should come first.

        For example: ["777", "1", "6"]
          corresponds to AS "777" as having the smallest percentage increase (of the top ten) and AS "6" having the
          highest percentage increase (of the top ten).
      """
    
    
    # the required return type is 'list' - you are welcome to define additional data structures, if needed
    top_10_ases_by_prefix_growth = []
    
    
    prefix_growth = {}


    for ndx, fpath in enumerate(cache_files):
        stream = pybgpstream.BGPStream(data_interface="singlefile")
        stream.set_data_interface_option("singlefile", "rib-file", fpath)

        # implement your solution here
        as_prefix_count = {}


        for elem in stream:
            if elem.type == "R" or elem.type == "A":
                as_path = elem.fields.get('as-path')
                if as_path:
                    path_parts = as_path.split()
                    if path_parts:  # check list not empty
                        origin_as = path_parts[-1]  
                        prefix = elem.fields['prefix']
                        if origin_as in as_prefix_count:
                            as_prefix_count[origin_as].add(prefix)
                        else:
                            as_prefix_count[origin_as] = set([prefix])


        for as_number, prefixes in as_prefix_count.items():
            if as_number in prefix_growth:
                prefix_growth[as_number].append(len(prefixes))
            else:
                prefix_growth[as_number] = [len(prefixes)]

    as_growth_percentage = {as_number: (counts[-1] - counts[0]) / counts[0] for as_number, counts in prefix_growth.items() if counts[0] != 0}

    sorted_as_growth_percentage = sorted(as_growth_percentage.items(), key=lambda x: (-x[1], x[0]))

    top_10_ases_by_prefix_growth = [as_number for as_number, growth in sorted_as_growth_percentage[:10]]
    
    top_10_ases_by_prefix_growth = top_10_ases_by_prefix_growth[::-1]


    return top_10_ases_by_prefix_growth


# Task 2: Routing Table Growth: AS-Path Length Evolution Over Time
def shortest_path_by_origin_by_snapshot(cache_files):
   

    shortest_path_by_origin_by_snapshot = defaultdict(list)

     
    set_as_regex = re.compile(r'{[\d,]+}')

    for ndx, fpath in enumerate(cache_files):
        stream = pybgpstream.BGPStream(data_interface="singlefile")
        stream.set_data_interface_option("singlefile", "rib-file", fpath)

        shortest_path = defaultdict(lambda: float('inf'))

        for elem in stream:
            
            as_list = elem.fields["as-path"].split(' ')

            origin_as = as_list[-1]

            as_set = set()

            for as_ in as_list:
                if set_as_regex.match(as_):
                    
                    as_set.add(as_)
                else:
                      
                    as_set.add(as_)

            path_length = len(as_set)

            if path_length > 1:
                
                shortest_path[origin_as] = min(shortest_path[origin_as], path_length)

        for origin_as in shortest_path_by_origin_by_snapshot.keys():
            if origin_as in shortest_path:
                shortest_path_by_origin_by_snapshot[origin_as].append(shortest_path[origin_as])
            else:
                shortest_path_by_origin_by_snapshot[origin_as].append(0)

        for origin_as in shortest_path.keys():
            if origin_as not in shortest_path_by_origin_by_snapshot:
                
                shortest_path_by_origin_by_snapshot[origin_as] = [0] * ndx
                
                shortest_path_by_origin_by_snapshot[origin_as].append(shortest_path[origin_as])

    return dict(shortest_path_by_origin_by_snapshot)
# Task 3

def aw_event_durations(cache_files):
    event_durations = {}
    last_announcement = {}
    """
    Identify Announcement and Withdrawal events and compute the duration of all explicit AW events in the input BGP data

    Args:
        cache_files: A chronologically sorted list of absolute (also called "fully qualified") path names

    Returns:
        A dictionary where each key is a string representing the address of a peer (peerIP) and each value is a
        dictionary with keys that are strings representing a prefix and values that are the list of explicit AW event
        durations (in seconds) for that peerIP and prefix pair.

        For example: {"127.0.0.1": {"12.13.14.0/24": [4.0, 1.0, 3.0]}}
        corresponds to the peerIP "127.0.0.1", the prefix "12.13.14.0/24" and event durations of 4.0, 1.0 and 3.0.
    """
    for filename in cache_files:
        stream = pybgpstream.BGPStream(data_interface="singlefile")
        stream.set_data_interface_option("singlefile", "upd-file", filename)

        for elem in stream:
            peer_ip = elem.peer_address

            if elem.type == 'A':
                if 'prefix' in elem.fields:
                    prefix = elem.fields["prefix"]
                   
                    last_announcement[(peer_ip, prefix)] = elem.time

            elif elem.type == 'W':
                if 'prefix' in elem.fields:
                    prefix = elem.fields["prefix"]
                    if (peer_ip, prefix) in last_announcement:
                        aw_duration = elem.time - last_announcement[(peer_ip, prefix)]
                        if aw_duration > 0:
                            if (peer_ip, prefix) not in event_durations:
                                event_durations[(peer_ip, prefix)] = [aw_duration]
                            else:
                                event_durations[(peer_ip, prefix)].append(aw_duration)
                       
                        del last_announcement[(peer_ip, prefix)]

    aw_event_durations = {}
    for (peer_ip, prefix), durations in event_durations.items():
        if peer_ip not in aw_event_durations:
            aw_event_durations[peer_ip] = {prefix: durations}
        else:
            aw_event_durations[peer_ip][prefix] = durations

    
    return aw_event_durations



def is_rtbh(elem):
    
    if 'communities' not in elem.fields:
        return False
    return any(community.endswith(':666') for community in elem.fields['communities'])

def rtbh_event_durations(cache_files):
    rtbh_event_durations = {}

    data = defaultdict(dict)

    announcements_rtbh = defaultdict(dict)

    for fpath in cache_files:
        stream = pybgpstream.BGPStream(data_interface='singlefile')
        stream.set_data_interface_option('singlefile', 'upd-file', fpath)

        for elem in stream:
            if 'prefix' not in elem.fields:
                continue
            tp, tm, addr, prefix = elem.type, elem.time, elem.peer_address, elem.fields['prefix']



            if tp == 'A':
                if is_rtbh(elem):



                    if prefix in announcements_rtbh.get(addr, {}):
                        del announcements_rtbh[addr][prefix]
                    announcements_rtbh[addr][prefix] = tm
                elif prefix in announcements_rtbh.get(addr, {}) and not is_rtbh(elem):
                    del announcements_rtbh[addr][prefix]
            elif tp == 'W':
                if prefix in announcements_rtbh.get(addr, {}):
                    duration = tm - announcements_rtbh[addr][prefix]
                    if duration > 0:
                        if addr not in rtbh_event_durations.keys():
                            rtbh_event_durations[addr] = {}
                        if prefix not in rtbh_event_durations[addr].keys():
                            rtbh_event_durations[addr][prefix] = []
                        rtbh_event_durations[addr][prefix].append(duration)
                    del announcements_rtbh[addr][prefix]



    return rtbh_event_durations













# The main function will not be run during grading.
# You may use it however you like during testing.
#
# NB: make sure that check_solution.py runs your
#     solution without errors prior to submission
if __name__ == '__main__':
    # do nothing
    pass
