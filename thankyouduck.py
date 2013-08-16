import subprocess

command = "twitter replies"  # the shell command
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

#Launch the shell command:
output = process.communicate()
each_mentions = output[0].split("\n")
first_mention = each_mentions[0]

#open the last mention for comparison
last_mention = open('last_mention.txt')
last = last_mention.readline()

#Read the most recent mention file and save in current.txt file
current_mention = open('current.txt','w')
current_mention.write(first_mention)
current_mention.close()
current_mention = open('current.txt')
current = current_mention.readline()

print "\n"
print "Start compare current and last mention"

#print "\n"
#print "Read last mention :" + last
#print "Read current mention:" + current
if current == last:
    print "Hmm...it seems like nobody mentions you at this time."

elif not current == last:
    print "Somebody mentioned you!! Let's inflate the ducky!"
    if ":)" in current:
        print "I am happy now:)"
        subprocess.call(["python","on.py"])
    elif ":(" in current:
        print "I am sad now :("
    else:
        print " No command found"

#store current to mention to last mention
current_to_last = open('last_mention.txt','w')
current_to_last.truncate()
current_to_last.write(current)
