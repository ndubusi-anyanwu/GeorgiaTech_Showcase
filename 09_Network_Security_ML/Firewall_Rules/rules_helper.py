import subprocess
import argparse

def write_rules():
    f = open("/home/student/Desktop/eval.rules", 'w+')

    rules = [ #list starting bracket

######################################################
    ### DO NOT MODIFY ABOVE THIS LINE

    # Add your rules here, following the template of:
    # """
    # alert tcp 10.0.0.1 any -> any any (msg:"TCP traffic detected from IP 10.0.0.1"; sid:10000001; rev:001;)
    # """

    # Your rule, surrounded by 3 quotations, with a comma afterwards between each entry

    # Start adding your rules here. between the quotation marks. We have provided 3 entries for you already, but feel free to add more if needed.

    
 """



alert tcp 18.219.211.138/24 any -> 172.31.69.25/24 80 ( msg:"DoS"; detection_filter:track by_src, count 300, seconds 1; sid:1000345; rev:32; )

    """,

  """
alert tcp 18.221.219.4/24 any -> 172.31.69.25/24 21 (flags: S; msg:"Bruteforce"; sid:10000654; detection_filter:track by_dst, count 10, seconds 1;)

    """,
  
 """

alert http  18.218.115.60/24 any -> 172.31.69.28/24 80 ( msg:"WebAttack"; http_method; content:"GET"; http_uri; content:"DVWA"; sid:10000239; rev:122; )


    """,
"""

alert http  18.218.115.60/24 any -> 172.31.69.28/24 80 ( msg:"WebAttack"; http_method; content:"POST"; http_uri; content:"DVWA"; sid:10000239; rev:122; )


    """,
 
 """

alert http 172.31.69.23/24 any -> 18.219.211.138/24 8080 ( msg:"Botnet"; http_method; content:"POST"; http_uri; content:"Admin"; sid:10003468; rev:13; )



    """


    ### DO NOT MODIFY BELOW THIS LINE
######################################################

    ] #list closing bracket

    for i in rules:
        f.write(i+'\n\n')
    f.close()

def run_rules():
    proc = subprocess.Popen(['snort', '-c', '/usr/local/etc/snort/snort.lua', '-r', '/home/student/Desktop/evaluation.pcap', '-R', '/home/student/Desktop/eval.rules', '-s', '65535', '-k', 'none', '-l', '.'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This script is where you'll place your rules: within the write_rules function. Add them to the rules list, surrounded by three quotation marks and separated by a comma")
    parser.add_argument('--run', action='store_true', help='--run is a helper command that will run your rules with snort and generate the log file automatically')
    args = parser.parse_args()

    write_rules()
    if args.run:
        run_rules()
