import subprocess, sys

command = "arp -a > arp_file"

subprocess.run(command, shell = True, executable="/bin/bash")

with open('arp_file', 'r') as fd:
    read=fd.read().split(' ')

# Words to be skipped
skip_words = set(["[ether]", "on", "at"])

for i in range(0, len(read)):
    for j in range(i+1, len(read)):
        if(read[i] == read[j]) and read[i] not in skip_words:
            print(read[j]);
