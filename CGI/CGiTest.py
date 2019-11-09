"""
@Brief Solution to CGI Test
@Brief A script that takes configured list of url(s) for check using Regular Expression
@Date  11-08-2019
@ Author Olutosin Ademola
"""

import re
import urllib.request
import urllib.response
import urllib.error
import urllib.parse
import datetime
import signal
from signal import signal, SIGINT
from sys import exit
from os import system, name 


# Handler for Keyboard interrupt
def handler(signal_received, frame):
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)

Url_List = []

print('''
      @Note  Unix style file path can be used or windows filepath format as shown:
      @Note  Double blackslahes was used because single backslash will throw error    
      @Param UNIX-style: C:/Users/SUSE/Desktop/CGI/URLLIST/urllist.txt
      @Param Windows-style: C:\\Users\\SUSE\\Desktop\\CGI\\URLLIST\\urllist.txt"
      ''')

#file_path = input("Input the path of the file containing the configured grouped list of url: ")
file_path = "C:\\Users\\SUSE\\Desktop\\CGI\\URLLIST\\urllist.txt"

Url_list = []

try: 
    url_file=open(file_path, 'r')
    
except IOError:
    print("File not found or path is incorrect")
    
finally:
    pass

for url in url_file:
    Url_List.append(url)

length = len(Url_List)

def main():
        url_list = []
        matched_content = []
        time_checked = []
        time_respone = []
        status = []
        content = []
        
        result = {"url": url_list, "content": content, "matched_content": matched_content,  "time_checked": time_checked, "time_respone": time_respone, "status": status}
        for link in Url_List:
            try:
                time_checked.append(datetime.datetime.now()) 
                resp = urllib.request.urlopen(link)
                url_list.append(link)
                html = resp.read().decode("utf-8")
                res = re.findall('<p>(.*?)</p>', str(html))
                status.append(resp.code)
                content.append(res)
                time_respone.append(datetime.datetime.now()) 
                
                # Asks for user input for user's regular expression to be checked for content matching
                print("*************************************************************************\n")
                user_search = input("Enter Regular Expression: ")
                
                search_converted= "%r"%user_search
                pattern = re.compile(search_converted)
                matches = pattern.finditer(str(res))
            
                for s in matches:
                        content_match = s.string
                        print("*************************************************************************\n")
                        print(content_match)
                matched_content.append(s.string)
                
            except Exception as e:
                status.append(str(e))
            
        return result

if __name__ == "__main__":
    
    # Calls the handler when Ctrl + C is pressed
    signal(SIGINT, handler)
    output = main()
    print(output)
    print("\n")
    print("*************************************************************************\n")
    print("End of program")




        
        
        

        
        
