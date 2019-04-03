import subprocess

# Example of command line used 
# curl -L www.yahoo.com | grep -oE 'href=\"(\S*)'

def getURLS(page):
    # curl and follow redirect
    command  = "curl -L "
    # Pull out string that start with href=" followed by repeating non-whitespace
    grep_filter = "| grep -oE 'href=\"(\S*)'"
    # Call the curl and pipe the output to grep
    url_data = subprocess.Popen(command + " " + page + " " + grep_filter, shell=True, stdout=subprocess.PIPE).stdout.read()
    # Split the output based on carriage returns (each line of output from grep)
    url_data = url_data.strip().split('\n')
    urls = []
    for line in url_data:
        if ("http" in line):
            left = line.find("\"")
            right = line.rfind("\"")
            s = line[left+1:right]
            if (len(s) > 0):
                urls.append(line[left+1:right])
    return urls


# Number of line to read from Alexa top 100K
LINES_TO_READ = 50
# Path to Alexa csv file
fin = open("./data/alexa_100k.csv", "r")
# Path to URL file we will generate
fout = open("./data/urls.csv","w+")
# Count of urls output
line_count = 1
for i in range(LINES_TO_READ):
  # Strip the whitespace and separate by ',' and take just the domain part of Alexa entry
  s = fin.readline().strip().split(',')[1]
  # Crawl the page and pull out list of URLS
  urls = getURLS(s)
  # Write these URLS to our new URL output file
  for u in urls:
    fout.write(str(line_count) + "," + u + "\r\n")
    line_count = line_count + 1
    
# Close the files
fin.close()
fout.close()



