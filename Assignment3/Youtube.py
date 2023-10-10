from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver (You need to have the browser driver installed)
driver = webdriver.Chrome()

# Open YouTube
driver.get("https://www.youtube.com")

# Find the search input field and enter a search query
search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("Python programming tutorial")
search_box.send_keys(Keys.RETURN)

# Wait for search results to load
time.sleep(5)

# Click on the first video in the search results
video_link = driver.find_element(By.XPATH,
                                 "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div["
                                 "1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div["
                                 "2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div["
                                 "1]/div/h3/a/yt-formatted-string")
video_link.click()

# Wait for the video page to load
time.sleep(5)

# Verify the video title and description
video_description = driver.find_element(By.XPATH,
                                        "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div["
                                        "1]/div/div[2]/ytd-watch-metadata/div/div[4]/div["
                                        "1]/div/ytd-text-inline-expander/tp-yt-paper-button[1]")
video_description.click()
time.sleep(5)

# Close the browser
driver.quit()
