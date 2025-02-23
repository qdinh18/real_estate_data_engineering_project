import scrapy
import numpy as np
class BdsSpider(scrapy.Spider):
    name = "bds"
    allowed_domains = ["batdongsan.com.vn"]
    def start_requests(self):
        # Start by making a request using curl_cffi
        yield scrapy.Request(
            url='https://batdongsan.com.vn/ban-can-ho-chung-cu-quan-2',
            meta={'use_curl_cffi': True},
            callback=self.parse_list
        )

    def parse_detail(self, response):
        # Process the raw data
        raw_title = response.xpath("//h1[@class='re__pr-title pr-title js__pr-title']/text()").get()
        raw_price_per_m2 = response.xpath("//span[@class = 'ext']/text()").get()
        raw_project = response.xpath("//div[@class = 're__project-title']/text()").get()
        raw_address = response.xpath("//span[@class = 're__pr-short-description js__pr-address']/text()").get()
        raw_price = response.xpath("(//span[@class='re__pr-specs-content-item-value'])[1]/text()").get()
        raw_area = response.xpath("(//span[@class='re__pr-specs-content-item-value'])[2]/text()").get()
        raw_bedroom = response.xpath("(//span[@class='re__pr-specs-content-item-value'])[3]/text()").get()
        raw_bathroom = response.xpath("(//span[@class='re__pr-specs-content-item-value'])[4]/text()").get()
        raw_posted_date = response.xpath("(//div[@class = 're__pr-short-info-item js__pr-config-item'])[1]/span[2]/text()").get()
        raw_expired_date = response.xpath("(//div[@class = 're__pr-short-info-item js__pr-config-item'])[2]/span[2]/text()").get()
        raw_status = response.xpath("(//span[@class = 're__long-text'])[1]/text()").get()
        raw_investor = response.xpath("(//span[@class = 're__long-text'])[2]/text()").get()
        raw_broker_name = response.xpath("(//a[@class = 'js__agent-contact-name'])[1]/text()").get()
        raw_broker_rank = response.xpath("//div[@class = 're__ldp-contact-box re__ldp-agent-contact re__ldp-contact-tablet']/div[@class = 're__ldp-agent-desc']/text()").get()
        raw_project_area_range = response.xpath("(//span[contains(@aria-label,'Diện tích')]/text())[last()]").get()
        raw_number_of_apartments = response.xpath("(//span[contains(@aria-label,'căn hộ')]/text())[last()]").get()
        raw_number_of_buildings = response.xpath("(//span[contains(@aria-label,'tòa nhà')]/text())[last()]").get()
        # Clean the raw data and handle exceptions
        title = raw_title.strip() if raw_title else 'Updating'
        price_per_m2 = raw_price_per_m2.strip() if raw_price_per_m2 else np.nan
        project_name = raw_project.strip() if raw_project else 'Updating'
        address = ','.join((str(raw_address.strip()).split(","))[1:]) if raw_address else 'Updating'
        price = raw_price.strip() if raw_price else np.nan
        area = raw_area.strip() if raw_area else np.nan
        bedroom = raw_bedroom.strip() if raw_bedroom else np.nan
        bathroom = raw_bathroom.strip() if raw_bathroom else np.nan
        posted_date = raw_posted_date.strip() if raw_posted_date else np.nan
        expired_date = raw_expired_date.strip() if raw_expired_date else np.nan
        status = raw_status.strip() if raw_status else 'Updating'
        investor = raw_investor.strip() if raw_investor else 'Updating'
        broker_name = raw_broker_name.strip() if raw_broker_name else 'Unknown'
        broker_rank = raw_broker_rank.strip() if raw_broker_rank else 'Updating'
        project_area_range = raw_project_area_range.strip() if raw_project_area_range else 'Updating'
        number_of_apartments = raw_number_of_apartments.strip() if raw_number_of_apartments else np.nan
        number_of_buildings = raw_number_of_buildings.strip() if raw_number_of_buildings else np.nan
        
        
        data = {
            'title':title,
            'price_per_m²':price_per_m2,
            'project_name':project_name, 
            'address':address, 
            'price':price, 
            'area':area, 
            'bedroom':bedroom,
            'bathroom':bathroom,
            'url':response.url,
            'posted_date':posted_date,
            'expired_date':expired_date,
            'project_status':status,
            'investor':investor,
            'broker_name':broker_name,
            'broker_rank':broker_rank,
            'project_area_range':project_area_range,
            'number_of_apartments':number_of_apartments,
            'number_of_buildings':number_of_buildings
        }
        
        
        yield data
        

    def parse_list(self, response):
        # Extract URLs of individual apartments
        apartment_urls = response.xpath("//a[@class='js__product-link-for-product-id']/@href").getall()
        for apt_url in apartment_urls:
            yield scrapy.Request(
                url=response.urljoin(apt_url),
                meta={'use_curl_cffi': True},
                callback=self.parse_detail
            )

        # Handle pagination (go to next page if it exists)
        next_page = response.xpath("//div[@class='re__pagination-group']//a[last()]/@href").get()
        if next_page:
            yield scrapy.Request(
                url=response.urljoin(next_page),
                meta={'use_curl_cffi': True},
                callback=self.parse_list
            )
