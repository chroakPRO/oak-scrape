#Todo
#Remove duplicate links

from multiprocessing import Pool
import requests
import bs4 as bs
import string
import argparse
import urllib.request
import re

current_links = []

def get_links(url):
    try:
        #Get the main link to the link
        current_links.append(url)
        #Source code.
        source = urllib.request.urlopen(url).read()
        soup = bs.BeautifulSoup(source, 'lxml')
        #Find all the href links in the source code.
        links = [link.get('href') for link in soup.find_all('a')]
        #Remove outgoing links, only keep local links.
        for link in links:
            if url in link:
                #if url is in link, add to list.
                current_links.append(link)
            elif not 'http' in link:
                #if name has a . or / add to list
                if '/' in link[0] or '.' in link[0]:
                    new_link = ''.join([url,link])
                    current_links.append(new_link)
                #if not, add / to item and then add to list.
                else:
                    new_link = ''.join([url,'/',link])
                    current_links.append(new_link)
            else:
                pass
    #check if errors.
    except TypeError as e:
        print(e)
        print("Got a Typerror")
        return []
    except IndexError as e:
        print(e)
        return []
    except AttributeError as e:
        print(e)
        return []
    #Instead of dispalying the error, put into error log.
    except Exception as e:
        with open('error.txt', 'w') as f:
            f.write(str(e))
        return[]

def email_scraper(url):
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'lxml')
    print(soup.find_all("Christopehr"))
    gmail = (c for c in soup.find_all(string=re.compile('@gmail')))
    hotmail = (c for c in soup.find_all(string=re.compile('@hotmail')))
    if not 'https' in url:
        new_string = url[7:9]
    else:
        new_string = url[8:10]
    private = (c for c in soup.find_all(string=re.compile('@{}'.format(new_string))))
    with open('emails.txt', 'w', newline='') as f:
        f.write(''.join(['Gmail\t',str(list(gmail)),'\n\n']))
        f.write(''.join(['Hotmail\t',str(list(hotmail)),'\n\n']))
        f.write(''.join(['Other\t',str(list(private)),'\n\n']))
    #print(emails)

def main():
    parser = argparse.ArgumentParser(description='Web-Scraper')
    #Add group so either U or u is required.
    group = parser.add_mutually_exclusive_group(required=True)
    #Arg for list of urls
    group.add_argument('--urllist', '-U', metavar="",help='Input location to list with urls, 1 url per line. Example -U ~/folder/list.txt')
    #Single url. (https://google.coom)
    group.add_argument('--url', '-u', metavar="",help='Input single url Example -u https://google.com')
    parser.add_argument('--processes', '-p',metavar="",type=int, help='Type how many processes you wanna run. Empty = max, which is the amount of links scraped.')
    args = parser.parse_args()
    #check so there isnt more process then items in list.
    if not args.processes:
        args.processes = len(current_links)
    elif args.processes > len(current_links):
        args.process = len(current_links)
    #Check that argument is used.
    if not args.urllist:
        get_links(args.url) 
    #if -U is used.
    else:
        print(12)
        #Deal with file uploads
        with open(args.urllist, 'r', newline='') as f:
            p2 = Pool(processes=processes)
            data2 = p2.map(get_links, (line for line in f))
    
    p = Pool(processes=args.processes)
    data = p.map(email_scraper, (link for link in current_links))

if __name__ == "__main__":
   main()
