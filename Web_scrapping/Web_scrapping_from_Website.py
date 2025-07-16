#  Import required libraries

import bs4     # This is the BeautifulSoup library (used for parsing HTML)
from bs4 import BeautifulSoup as bs
import requests      Used to send HTTP requests to web pages

#  Define the URL of the product page
link="https://www.boat-lifestyle.com/products/airdopes-alpha-true-wireless-earbuds?_gl=1*1asuzs9*_up*MQ..&gclid=CjwKCAjw0aS3BhA3EiwAKaD2ZUE1Z2Y1zY8L8vqS0r_ZywCCySZGLKmMMvpC4FI_5fZjG4ZTTBcMOBoCbO4QAvD_BwE"

#  Send an HTTP GET request to the page
page = requests.get(link)

#  Check the status of the response (optional but good practice)
print(page)          # Output will show <Response [200]> if successful

#  Get the raw HTML content from the page
html_content = page.content

# Parse the HTML using BeautifulSoup
soup = bs(html_content, 'html.parser')   # 'html.parser' is a built-in parser in Python

# Prettify and print the parsed HTML content
print(soup.prettify())   # Formats the HTML with proper indentation for readability

#when you parse HTML using BeautifulSoup, you are converting the 
#raw HTML content of a web page into a structured format, 
#like a tree, where you can easily locate and manipulate individual 
#elements (such as tags, attributes, or text).

#page.content=> provides the raw HTML content,
#while soup.prettify()=> offers a formatted, human-readable version of the parsed HTML content.

## now let us scrap the contents
names=soup.find_all('span',class_="jdgm-rev__author")
names
### but the data contains with html tags,let us extract names from html tags
cust_names=[]
for i in range(0,len(names)):
    cust_names.append(names[i].get_text())
    
cust_names
len(cust_names)
#cust_names.pop(-1)
#len(cust_names)


### There are total 6 users names 
#Now let us try to identify the titles of reviews

title=soup.find_all('b',class_="jdgm-rev__title")
title
# when you will extract the web page got to all reviews rather top revews.when you
# click arrow icon and the total reviews ,there you will find span has no class
# you will have to go to parent icon i.e.a
#now let us extract the data
review_titles=[]
for i in range(0,len(title)):
    review_titles.append(title[i].get_text())
review_titles

len(review_titles)
##now let us scrap ratings
rating=soup.find_all('span',class_="jdgm-rev__rating")
rating
###we got the data
ratings = [int(span['data-score']) for span in soup.find_all('span', {'class': 'jdgm-rev__rating'})]

# Print the ratings
print(ratings)

len(ratings)



## now let us scrap review body
reviews=soup.find_all("div",class_="jdgm-rev__body")
reviews
review_body=[]
for i in range(0,len(reviews)):
    review_body.append(reviews[i].get_text())
review_body
review_body=[ reviews.strip('\n\n')for reviews in review_body]
review_body
len(review_body)
