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
page_soup.findAll("div",{"class":"row course-summary-paragraph"})
containers = page_soup.findAll("div",{"class":"row course-summary-paragraph"})

filename = "ClassInformation___.csv"
f = open(filename, "w")

headers = "Class Description\n"
f.write(headers)

# Loop that grabs every value:
for container in containers:

    home = page_soup.find('div', attrs={'class': 'col-xs-12 col-sm-12 col-md-12 text-left full-width-column'}).find('span').text
    course_description = home

    # course_description_container = container.findAll("span",{"class": "row course-summary-paragraph"})
    # course_description = course_description_container[0].text

    # course_name_countainer = container.findAll("span",{"class":"course-entry-subject"})
    # course_name = course_name_countainer[0].text

    print("Course Description: " + course_description)
    # print("Course Number: " + course_number)

    f.write(course_description + "\n\n")

f.close()


# col-xs-12 col-sm-12 col-md-12 text-left full-width-column
