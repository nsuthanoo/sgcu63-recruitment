import re
import requests

#Create a list of URLs to scrape from
def get_baan_url(url):
    info=requests.get(url)
    #Find all baan names
    baan_list=re.findall('nameURL:"(.+?)",', info.text)
    #Create a list of URLs to pages of each baan
    url_list=['https://rubnongkaomai.com/baan/'+baan for baan in baan_list]
    return(url_list)

#Get baan names and slogans from the list of URLs
def get_slogan(url_list):
    #Create dictionary to store baan names and slogans
    baan_slogan={}
    #Loop inside the url list to scrape each page inside the list
    for url in url_list:
        info=requests.get(url)
        #Find baan's name in Thai
        baan=re.findall('<h1 type="header">(.+?)</h1>',info.text)[0]
        #Find the slogan
        slogan=re.findall('<h3 type="header">(.+?)</h3>',info.text)[0]
        baan_slogan[baan]=slogan
    return(baan_slogan)

def write_html(baan_slogan):
    #Create a html file
    with open('Prob#1 - The scraper/table.html','w', encoding='utf8') as html:
        #Write header to file
        html.write('''<!DOCTYPE html>
    <html>
        <head>
            <title>Baan Rub Nong Slogan Table</title>
            <link href="http://www.amiels.lnw.mn/css/bootstrap-4.3.1.css" rel="stylesheet">
        </head>
        <body  class="bg-secondary">
            <div class="container">
                <table class="table table-hover table-bordered table-dark table-striped">
                    <thead class="text-center">
                        <tr>
                            <th scope="col">ชื่อบ้าน</th>
                            <th scope="col">สโลแกน</th>
                        </tr>
                    </thead>
                    <tbody class="text-center">\n''')
        #Write each baan's name and slogan to the file
        for baan in baan_slogan.keys():
            #Tabs or spaces are there just to make the HTML file easier to read
            html.write('                        <tr>\n'+'                            <td>'+baan+'</td>\n                            <td>'+baan_slogan[baan]+'</td>\n                        </tr>\n')
        #Write footer to the file
        html.write('''                    </tbody>
                </table>
            </div>
        </body>
    </html>''')
        #Inform user that the file is created
        print('HTML File created successfully')

#Combine all 3 defs to be usable in one command
def create_table(url):
    write_html(get_slogan(get_baan_url(url)))

#The URL to javascript file that has all baan's names/links
url='https://rubnongkaomai.com/component---src-pages-baan-js-b2ff2cb9f7799cf2b1de.js'
create_table(url)