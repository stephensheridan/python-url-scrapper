#!/usr/bin/python

# Author: Stephen Sheridan
# 05/04/2019
# https://github.com/stephensheridan/

import sys
import subprocess

# Example of command line used 
# curl -L --max-time 10 www.yahoo.com | grep -oE 'href=\"(\S*)'

def getURLS(url_set, page):
  # curl and follow redirect
  command  = "curl -L --max-time 10"
  # Pull out string that start with href=" followed by repeating non-whitespace
  grep_filter = "| grep -oE 'href=\"(\S*)'"
  # Call the curl and pipe the output to grep
  url_data = subprocess.Popen(command + " " + page + " " + grep_filter, shell=True, stdout=subprocess.PIPE).stdout.read()
  # Split the output based on carriage returns (each line of output from grep)
  url_data = url_data.strip().split('\n')
  for line in url_data:
      left = line.find("\"")
      right = line.rfind("\"")
      s = line[left+1:right]
      if ("http" in s[0:4]):
        url_set.add(line[left+1:right])


def main(input_file, output_file, num_pages_to_scrape):
  # Open Alexa csv file
  fin = open(input_file, "r")
  # Open output file for writing
  fout = open(output_file,"w+")
  # Create a set to contain unique Url's
  unique_urls = set()
  # Count of urls output
  line_count = 0
  for i in range(num_pages_to_scrape):
    # Strip the whitespace and separate by ',' and take just the domain part of Alexa entry
    s = fin.readline().strip().split(',')[1]
    # Crawl the page and pull out list of URLS
    getURLS(unique_urls, s)

  # Write these URLS to our new URL output file
  for u in unique_urls:
    fout.write(str(line_count) + "," + u + "\r\n")
    line_count = line_count + 1
    
  # Close the files
  fin.close()
  fout.close()
  print "Done, " + str(line_count) + " URL's scrapped from  " + str(num_pages_to_scrape) + " pages."

if __name__ == "__main__":
    if (len(sys.argv) < 4):
      print "USAGE: url_scrapper <input_file> <output_file> <num_pages_to_scrape>"
    elif (len(sys.argv) == 4):
      main(sys.argv[1], sys.argv[2], int(sys.argv[3]))


