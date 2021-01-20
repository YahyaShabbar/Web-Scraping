import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


# Opens up connection
my_url = 'https://ucdavis.pubs.curricunet.com/Catalog/computer-science'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# HTML Parcing
page_soup = soup(page_html, "html.parser")
page_soup.findAll("div",{"class":"row block-entry course-entry"})
containers = page_soup.findAll("div",{"class":"row block-entry course-entry"})

filename = "ClassNamesandNumber.csv"
f = open(filename, "w")

headers = "Class Name, Class Number\n"
f.write(headers)

# Loop that grabs every value:
for container in containers:

    course_number_container = container.findAll("span",{"class":"course-entry-course-number"})
    course_number = course_number_container[0].text

    course_name_countainer = container.findAll("span",{"class":"course-entry-subject"})
    course_name = course_name_countainer[0].text

    print("Course Name: " + course_name)
    print("Course Number: " + course_number)

    f.write(course_name + ", " + course_number + "\n")

f.close()
