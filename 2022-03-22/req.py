from lxml import html
import requests
    

def propertyCrawler(url):
    r = requests.get(url)
    tree = html.fromstring(r.content)
    property_url = tree.xpath("//a[@aria-label='Listing link']/@href")


    for page_url in property_url:
        single_page = requests.get('https://www.bayut.com/'+ page_url)
        single_page_html = html.fromstring(single_page.content)
        price_value = single_page_html.xpath('//span[@aria-label="Price"]/text()')
        purpose = single_page_html.xpath('//span[@aria-label= "Purpose"]/text()')
        type = single_page_html.xpath('//span[@aria-label= "Type"]/text()')
        added_on = single_page_html.xpath('//span[@aria-label="Reactivated date"]/text()')
        furnishing = single_page_html.xpath('//span[@aria-label="Furnishing"]/text()')

   

        print(price_value,purpose,type,added_on,furnishing)
    
property=propertyCrawler('https://www.bayut.com/to-rent/property/dubai/')
print(property)
 
