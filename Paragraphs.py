from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures 
import time

driver = webdriver.Chrome()

def handle_stale_elements(elements):
    cleaned_elements = []
    for element in elements:
        try:
            # Check if the element is stale by accessing a property like 'text'
            _ = element.text
            cleaned_elements.append(element)
        except StaleElementReferenceException:
            # If the element is stale, replace it with an empty string
            cleaned_elements.append("")

    return cleaned_elements

def fetch_para_se(url):
    
    driver.get(url)
    body_txt = driver.find_element(By.TAG_NAME, "body").text
    #clean_elements = handle_stale_elements(para_elements)
    #combined_text = " ".join([element.text for element in clean_elements if element.is_displayed()])
    header = driver.find_element(By.TAG_NAME, "h1").text
    return {"header":[header], "text":[body_txt], "url":[url]}


def wait_for_future(url):
  print("-------- Wait for future --------")
  start_time = time.time()
  
  with ThreadPoolExecutor() as executor:
      
    future = executor.submit(fetch_para_se, url, driver)
    print("future created", "|", time.time() - start_time)
    print("waiting for future...", "|", time.time() - start_time)
    result = future.result()
    print("Result created at ",time.time() - start_time)
  return result

def write_to_file(results, file):
      header = results["header"]
      web_content = results["text"]
      with open(file, "a") as file:
        file.write("\n\n")
        file.write(f"H1: {header}")
        file.write("\n\n")
        file.write(web_content)
        file.write("\n\n")
        file.write("##################################")

def write_to_df(results, df):
    df = pd.concat([df, pd.DataFrame.from_dict(results)], axis= 0)
    return df
    



