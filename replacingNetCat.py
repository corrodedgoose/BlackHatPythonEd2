import argparse
import socket
import subprocess
import sys
import threading
import textwrap
import shlex

def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    return output.decode()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='NetCat Replacement Tool', formatter_class=argparse.RawTextHelpFormatter, epilog=textwrap.dedent(\
        '''Examples:
        netcat.py -t 192.168.0.108 -p 5555 -l -c
        netcat.py -t 192.168.0.108 -p 5555 -l -e="cat /etc/passwd"
        netcat.py -t 192.168.0.108 -p 5555 -l -u=mytest.txt
        echo 'ABCDEFGHI' | ./netcat.py -t 192.168.0.108 -p 13555
        netcat.py -t 192.168.0.108 -p 5555)'''))
    parser.add_argument('-p', '--port', type=int, default=5555, help='Port to connect to or listen on')
    parser.add_argument('-l', '--listen', action='store_true', help='Listen on [host]:[port] for incoming connections')
    parser.add_argument('-e', '--execute', help='Execute the given command upon receiving a connection')
    parser.add_argument('-c', '--command', action='store_true', help='Initialize a command shell')
    parser.add_argument('-t', '--target', default=' ', help='Target host')
    parser.add_argument('-u', '--upload', help='Upon receiving connection upload a file and write to [destination]')
    args = parser.parse_args() 
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()

    '''nc = NetCat(args, buffer.encode())
    nc.run()'''