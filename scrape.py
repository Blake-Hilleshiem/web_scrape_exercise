import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"

page = requests.get(url)
#            ^^ htttp get request

# print(page)
# page is a response object

# print(page.text)

page_text = page.text

soup = BeautifulSoup(page.content,'html.parser')

# print(soup)
# ----
# job_titles = soup.find_all('h2')
## print(job_titles)

# for job in job_titles:
#     print(job.text)
# ---

card_content_tags = soup.find_all('div', class_='card-content')

print('\n\n\n\n\n')
print(f'{"Job Title":<50}{"Company":<35}{"Location":<25}{"DateTime":<13}')
print(f'{"-"*49:<50}{"-"*34:<35}{"-"*24:<25}{"-"*12:<13}')

for job in card_content_tags:

    job_title = job.find('h2')   
    if job_title:
        job_title = job_title.text.strip()
    
    company = job.find('h3', class_='company')
    if company:
        company = company.text.strip()

    location = job.find('p', class_='location')
    if location:
        location = location.text.strip()
    
    datetime = job.find('time')
    if datetime:
        datetime = datetime.text.strip()

    footer = job.find('footer')
    if footer:
        links = footer.find_all('a')

        description = ''
        link_href = ''
        for link in links:
            if link.text == 'Apply':

                link_href = link['href']
                # load and get the data

                detail_page = requests.get(link_href)
                detail_page_soup = BeautifulSoup(detail_page.content, 'html.parser')

                content = detail_page_soup.find('div', class_='content')
                description = content.find('p')

                if description:
                    description = description.text.strip()

    

    print(f'{job_title:<50}{company:<35}{location:<25}{datetime:<10}\n{description}\n{link_href}\n')

# Next try to write out to write to a csv
# ----



