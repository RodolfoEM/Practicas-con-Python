import requests
import lxml.html as html
import datetime
import os

HOME_URL = 'https://www.larepublica.co/'
XPATH_LINK_TO_ARTICLE = '//text-fill/a/@href'
XPATH_TITLE = '//div[@class="mb-auto"]/h2/span/text()'
XPATH_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="html-content"]/p[not(@class)]/descendant-or-self::*/text()' #to do: check how to extract the u html


def parse_notice(link, today):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            notice = response.content.decode('utf-8') #save the content of the page in a variable
            parsed = html.fromstring(notice) #parse the html content
            try:
                title = parsed.xpath(XPATH_TITLE)[0]
                title.replace('\"', '') #remove the quotes from the title
                title = title.replace('\'', '') #remove the quotes from the title
                title = title.replace('\n', '') #remove the newlines from the title
                title = title.replace('\t', '') #remove the tabs from the title
                title = title.replace('\r', '') #remove the carriage returns from the title
                title = title.strip() #remove the whitespaces from the title
                title = title.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u') #replace the accents from the title
                title = title.replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U') #replace the accents from the title
                title = title.replace('?', '').replace('¿', '').replace('!', '').replace('¡', '') #remove the question marks and exclamation marks from the title
                title = title.replace(':', '').replace(';', '').replace(',', '').replace('.', '').replace('(', '').replace(')', '') #remove the colons, semicolons, commas, dots, parentheses and spaces from the title
                title = title.replace('%', '').replace('$', '').replace('#', '').replace('@', '').replace('&', '').replace('*', '').replace('+', '').replace('=', '').replace('-', '').replace('_', '').replace('/', '').replace('\\', '').replace('|', '').replace('<', '').replace('>', '').replace('"', '').replace('\'', '') #remove the special characters from the title
                summary = parsed.xpath(XPATH_SUMMARY)[0] #get the summary of the article
                body = parsed.xpath(XPATH_BODY) #get the body of the article
            except IndexError:
                return

            with open(f'{today}/{title}.txt', 'w', encoding='utf-8') as f:
                f.write(title)
                f.write('\n\n')
                f.write(summary)
                f.write('\n\n')
                for p in body:
                    f.write(p)
                    f.write('\n')
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)


def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8') #save the content of the page in a variable
            parsed = html.fromstring(home) #parse the html content
            link_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE) #get the links to the articles
            #print(link_to_notices)

            today = datetime.date.today().strftime('%d-%m-%Y') #get the current date
            if not os.path.isdir(today): #if the directory doesn't exist, create it
                os.mkdir(today)

            for link in link_to_notices: #for each link
                parse_notice(link, today)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

def run():
    parse_home()

if __name__ == '__main__':
    run()