import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options

# List of websites
websites = [
    "https://www.facebook.com",
    "https://www.youtube.com",
    "https://www.twitter.com",
    "https://www.instagram.com",
    "https://www.amazon.com",
    "https://www.google.com",
    "https://www.reddit.com",
    "https://www.netflix.com",
    "https://www.linkedin.com",
    "https://www.pinterest.com",
    "https://www.tumblr.com",
    "https://www.whatsapp.com",
    "https://www.spotify.com",
    "https://www.ebay.com",
    "https://www.microsoft.com",
    "https://www.twitch.tv",
    "https://www.airbnb.com",
    "https://www.imdb.com",
    "https://www.wikipedia.org",
    "https://www.github.com",
    # Additional websites
    "https://www.apple.com",
    "https://www.tiktok.com",
    "https://www.slack.com",
    "https://www.dropbox.com",
    "https://www.medium.com",
    "https://www.quora.com",
    "https://www.etsy.com",
    "https://www.wordpress.com",
    "https://www.zoom.us",
    "https://www.udemy.com",
    "https://www.khanacademy.org",
    "https://www.stackoverflow.com",
    "https://www.buzzfeed.com",
    "https://www.cnn.com",
    "https://www.nytimes.com",
    "https://www.bbc.co.uk",
    "https://www.nationalgeographic.com",
    "https://www.ted.com",
    "https://www.adobe.com",
]


# Delay in seconds between each website visit
delay = 5

# Create Edge options
options = Options()

# Initialize the Edge web driver
driver_path = r"PATH_TO_EDGE_WEBDRIVER"
driver = webdriver.Edge(executable_path=driver_path, options=options)

# Visit each website and wait for the specified delay
for website in websites:
    # Open the website
    driver.get(website)
    
    # Wait for the specified delay
    time.sleep(delay)
    
    # Close the browser
    driver.quit()
    
    # Re-initialize the web driver
    driver = webdriver.Edge(executable_path=driver_path, options=options)

# Close the driver after visiting all websites
driver.quit()
