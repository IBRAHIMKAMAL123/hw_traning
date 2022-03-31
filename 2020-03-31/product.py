from lxml import html
import requests
import json
import csv

property_counter = 0
field = ["property_url", "property_id", "purpose ", "type", "added_on ", "furnishing ", "location ","price" ,"bed_bath_size", "permit_number", "agent_name", "breadcrumbs", "descripition"]
properties = []

def propertyCrawler(url):
    global property_counter
    r = requests.get(url)
    tree = html.fromstring(r.content)
    property_url = tree.xpath("//a[@aria-label='Listing link']/@href")
    
    for page_url in property_url:
        property_details = {}
        single_page = requests.get('https://www.bayut.com/' + page_url)
        single_page_html = html.fromstring(single_page.content)
        property_details['property_url'] = ('https://www.bayut.com/' + page_url)

        property_id = single_page_html.xpath('//span[@aria-label="Reference"]/text()')
        id = ' '.join([str(elem) for elem in property_id])
        property_details['property_id'] = id

        property_purpose = single_page_html.xpath('//span[@aria-label= "Purpose"]/text()')
        purpose = ' '.join([str(elem) for elem in property_purpose])
        property_details['purpose '] = purpose

        property_type = single_page_html.xpath('//span[@aria-label= "Type"]/text()')
        types = ' '.join([str(elem) for elem in property_type])
        property_details['type'] = types

        property_added = single_page_html.xpath('//span[@aria-label="Reactivated date"]/text()')
        added = ' '.join([str(elem) for elem in property_added])
        property_details['added_on '] = added

        property_furnishing = single_page_html.xpath('//span[@aria-label="Furnishing"]/text()')
        furnishing = ' '.join([str(elem) for elem in property_furnishing])
        property_details['furnishing '] = furnishing

        property_location = single_page_html.xpath('//div[@aria-label="Property header"]/text()')
        location = ' '.join([str(elem) for elem in property_location])
        property_details['location '] = location
        
        property_price = single_page_html.xpath('//div[@class="c4fc20ba"]/span/text()')
        d = {"currency":property_price [0], "amount": property_price[1]}
        property_details['price'] = d

        property_num = single_page_html.xpath('//div[@aria-label="Agency info"]/div/div[2]/span[2]/text()')
        num = ' '.join([str(elem) for elem in property_num])
        property_details['permit_number'] = num

        property_agent = single_page_html.xpath('//a[@aria-label="Agent name"]/text()')
        agent = ' '.join([str(elem) for elem in property_agent])
        property_details['agent_name'] = agent

        property_breadcrumbs = single_page_html.xpath('//span[@aria-label="Link name"]/text()')
        breadcrumbs = ' '.join([str(elem) for elem in property_breadcrumbs])
        property_details['breadcrumbs'] = breadcrumbs

        property_details['descripition'] = single_page_html.xpath(
            '//div[@aria-label="Property description"]/div/span/text()')

        print(property_details)
        properties.append(property_details)

        with open('property.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=field)
            writer.writeheader()
            writer.writerows(properties)
        property_counter = property_counter + 1

    next_page = tree.xpath('//a[@title="Next"]/@href')[0]
    next_page_fullulr = ('https://www.bayut.com' + next_page)
    if next_page and property_counter < 201:
        propertyCrawler(next_page_fullulr)

    # print(property_counter)
    # print()​
propertyCrawler('https://www.bayut.com/to-rent/property/dubai/')
# propertyCrawler('//a[@title="Next"]/@href')