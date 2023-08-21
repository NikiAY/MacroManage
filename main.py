import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import StaleElementReferenceException
import concurrent.futures
from multiprocessing.pool import ThreadPool
import time
import json
import re


from Paragraphs import fetch_para_se, write_to_file, write_to_df, wait_for_future
from Urls import urls_string, text_to_urls, validate_urls

# sample_urls = ['https://hbr.org/2018/07/collaborative-intelligence-humans-and-ai-are-joining-forces', 
#                 'https://paperswithcode.com/paper/neighborhood-enlargement-in-graph-neural', 
#                 'https://machinelearningmastery.com/what-are-generative-adversarial-networks-gans/', 
#                 ]

#'https://archive.is/eV0dY', 'https://meatba11.medium.com/keras-loading-and-processing-images-in-batches-1cff1b0f4aa4', 'https://archive.is/HDqNr',

# with open("urls_round2", "r") as file:
#     data = json.load(file)
#     urls = []
#     for url in data:
#         urls.append(url["url"])

        
urls = text_to_urls(urls_string, "edited")

urls_list = [url for url in urls if not re.search(r"youtube", url)  
             and not re.search(r"\.pdf$", url)]

df_txt = pd.DataFrame(columns= ["header", "text", "url"])


driver = webdriver.Chrome()
 
start = time.time()


with ThreadPool() as pool:
    results = pool.map(fetch_para_se, [url for url in urls_list[:3]])
    for result in results:
        #df_txt = write_to_df(result, df_txt)
        print(result)


# result = wait_for_future(url= url, driver= driver)
# print(result)

driver.quit()
end = time.time()
elapsed_time = end - start
print('Execution time:', elapsed_time, 'seconds')
      
# df_txt.to_csv("df_txt.csv")
#df_txt.to_csv('df_txt.csv', mode='a', index=False, header=False)

    





    