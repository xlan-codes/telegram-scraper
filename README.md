"# telegram-scraper" 

• API Setup
    
    Go to http://my.telegram.org and log in.
    
    Click on API development tools and fill the required fields.
    
    put app name you want & select other in platform Example :
    
    copy "api_id" & "api_hash" after clicking create app ( will be used in setup.py )
    
    

Install requierments and usage
    
    python setup.py -i

    Scrape contacts
    > python main.py --scrape-contact --file-name [filename.csv]

    Send sms To Collected contacts
    > python main.py --send-sms --file-name [filename.csv]
    
