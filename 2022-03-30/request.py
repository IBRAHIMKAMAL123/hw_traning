from lxml import html
import requests
import json
    

property_counter = 0
 
def propertyCrawler(url):
    global property_counter
    r = requests.get(url)
    tree = html.fromstring(r.content)
    property_url = tree.xpath("//a[@aria-label='Listing link']/@href")
    
	
    for page_url in property_url:
        property_details ={}
        single_page = requests.get('https://www.bayut.com/'+ page_url)
        single_page_html = html.fromstring(single_page.content)
        property_details['prpperty_url'] = ('https://www.bayut.com/'+ page_url)
        property_details['property_id'] =  single_page_html.xpath('//span[@aria-label="Reference"]/text()')
        property_details['purpose ']  = single_page_html.xpath('//span[@aria-label= "Purpose"]/text()')
        property_details['type']  = single_page_html.xpath('//span[@aria-label= "Type"]/text()')
        property_details['added_on '] = single_page_html.xpath('//span[@aria-label="Reactivated date"]/text()')
        property_details['furnishing '] = single_page_html.xpath('//span[@aria-label="Furnishing"]/text()')
        property_details['location '] = single_page_html.xpath('//div[@aria-label="Property header"]/text()')
        property_details['price']  = single_page_html.xpath('//span[@aria-label="Price"]/text()')
        property_details['bed_bath_size']  = {
            "bedroom": single_page_html.xpath('//span[@aria-label="Beds"]/span/text()'),
            "bathrooms": single_page_html.xpath('//span[@aria-label="Baths"]/span/text()'),
             "size" : single_page_html.xpath('//span[@aria-label="Area"]/span/span/text()')
             }
        property_details['permit_number']  = single_page_html.xpath('//div[@aria-label="Agency info"]/div/div[2]/span[2]/text()')
        property_details['agent_name']  = single_page_html.xpath('//a[@aria-label="Agent name"]/text()')
        property_details['breadcrumbs']  = single_page_html.xpath('//span[@aria-label="Link name"]/text()')
        property_details['descripition']  = single_page_html.xpath('//div[@aria-label="Property description"]/div/span/text()')
        
        
        
        with open("request.json","a") as f :
            if property_counter < 200:
                f.write(json.dumps(property_details, indent=2)+ ",")
        
        property_counter = property_counter + 1 
        
    
    
    next_page = tree.xpath('//a[@title="Next"]/@href')[0]
    next_page_fullulr = ('https://www.bayut.com' + next_page)
    if next_page and property_counter < 201:
        propertyCrawler(next_page_fullulr)
    
    print(property_counter) 
        # print()

    
    
propertyCrawler('https://www.bayut.com/to-rent/property/dubai/')
# propertyCrawler('//a[@title="Next"]/@href')

 