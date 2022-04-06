from lxml import html
import requests
import csv

from req import saree
field =['count','product_name','product_code','image_url']
saree_details ={'count':0}

def sareeCrawler(start_url):
    r = requests.get(start_url)
    tree = html.fromstring(r.content)
    saree_url = tree.xpath('//a[@class="product photo product-item-photo"]/@href')
    
    for url in saree_url:
        saree_page(url=url)
    

def saree_page(url): 
    r = requests.get(url)
    tree = html.fromstring(r.content) 
    saree_details['count'] +=1 
    saree_details['product_name'] = tree.xpath('//span[@class="base"]/text()')
    saree_details['product_code'] = tree.xpath('//div[@class="product attribute sku"]/div/text()')
    saree_details['image_url'] = tree.xpath('//img[@class="no-sirv-lazy-load"]/@src')
    saree_data = [saree_details]
    if saree_details['count'] <11:
        with open('saree.csv', 'a') as f:
            writer = csv.DictWriter(f, fieldnames=field)
            writer.writerows(saree_data)
        print(saree_details)    
        
        
        
sareeCrawler('https://www.saree.com/saree')       
        