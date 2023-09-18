import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import datetime
import os
import numpy as np

# Read the Excel file to get the URLs
excel_filename = "sku_list.xlsx"
df_urls = pd.read_excel(excel_filename)


# Create empty lists to store the device names and values
device_names_mzm = []     # use to store device name from Mazuma
values_good = []    # use to store good value
values_excellent = []    # use to store excellent value
values_poor = []    # use to store poor value
sku_devices = []    # store SKU for final spreadsheet
device_names_mm = []     # use to store device name from MM
values_working_mm = []    # use to store working value from MM
values_asnew_mm = []    # use to store as new value from MM
values_dead_mm = []    # use to store dead value from MM

# Announce the process
print(f"Now Scraping {len(df_urls)} items, you can add more by using the excel list SKU_list within the installation folder.")

# Create a progress bar
progress_bar = tqdm(total=len(df_urls), desc="Scraping progress")

# Iterate over the URLs in the DataFrame
for index, row in df_urls.iterrows():

    # checking SKU 
    sku_device = row["SKU"]
    if pd.notna(sku_device):
       sku_devices.append(sku_device)
    else:
       sku_devices.append("Missing SKU")
    
    # Scraping Mazuma Prices
    # Sorting Mazuma URL from excel
    mzm_url = row["Mazuma URL"]
    
    # Send a GET request to the website only if the URL is valid
    if pd.notna(mzm_url) and isinstance(mzm_url, str) and len(mzm_url) > 0 and mzm_url.startswith('http'):


       # Send a GET request to the website
       response = requests.get(mzm_url)
       
       # Create a BeautifulSoup object to parse the HTML content
       soup_mzm = BeautifulSoup(response.text, "html.parser")

       # Find the device name
       device_name_element = soup_mzm.find("span", class_="cnf-model")
       device_name_mzm = device_name_element.text.strip() if device_name_element else "Check URL"

       # Find the good value element
       value_good_element = soup_mzm.find("a", {"data-condition": "Good"})
       value_good = value_good_element["data-condition-price"] if value_good_element else "N/A"

       # Find the excellent value element
       value_excellent_element = soup_mzm.find("a", {"data-condition": "Excellent"})
       value_excellent = value_excellent_element["data-condition-price"] if value_excellent_element else "N/A"

       # Find the poor value element
       value_poor_element = soup_mzm.find("a", {"data-condition": "Poor"})
       value_poor = value_poor_element["data-condition-price"] if value_poor_element else "N/A"

       # Append the device name and value to the respective lists for Mazuma
       device_names_mzm.append(device_name_mzm)
       values_good.append(value_good)
       values_excellent.append(value_excellent)
       values_poor.append(value_poor)
    

    else:
       

       device_names_mzm.append("Invalid URL")
       values_good.append("N/A")
       values_excellent.append("N/A")
       values_poor.append("N/A")
       
    

    # Scraping Mobile Monster Prices
    mm_url = row["Moblie Monster URL"]

    # Send a GET request to the website only if the URL is valid
    if pd.notna(mm_url) and isinstance(mm_url, str) and pd.notna(mm_url):
        response = requests.get(mm_url)

        # Create a BeautifulSoup object to parse the HTML content
        soup_mm = BeautifulSoup(response.text, "html.parser")

        # Find the device name from Mobile Monster
        device_name_element = soup_mm.find("div", class_="grey_box-heading")
        device_name_mm = device_name_element.text.strip() if device_name_element else "Check URL"

        # Find the working value element from Mobile Monster
        value_working_element = soup_mm.find("h1", {"id": "per_unit_final_pricing", "class": "amount_text"})
        value_working_mm = value_working_element.text if value_working_element else "N/A"

        # Find the as new value element from Mobile Monster
        value_asnew_element = soup_mm.find("h1", {"id": "NewPricing", "class": "amount_text selected-price-holder"})
        value_asnew_mm = value_asnew_element.text if value_asnew_element else "N/A"

        # Find the dead value element from Mobile Monster
        value_dead_element = soup_mm.find("h1", {"id": "", "class": "amount_text"})
        value_dead_mm = value_dead_element.text if value_dead_element else "N/A"

        # Append the device name and value to the respective lists for Mobile Monster
        device_names_mm.append(device_name_mm)
        values_working_mm.append(value_working_mm)
        values_asnew_mm.append(value_asnew_mm)
        values_dead_mm.append(value_dead_mm)

    else:
        # Handle the case where the URL is missing or invalid
        device_names_mm.append("Invalid URL")
        values_working_mm.append("N/A")
        values_asnew_mm.append("N/A")
        values_dead_mm.append("N/A")

    # Update the progress bar
    progress_bar.update(1)

# Close the progress bar
progress_bar.close()

# Create a DataFrame to hold the combined data
data = {
    "SKU": sku_devices,
    "Device Name Mazuma": device_names_mzm,
    "Mazuma Excellent Value": values_excellent,
    "Mazuma Good Value": values_good,
    "Mazuma Poor Value": values_poor,
    "Device Name Mobile Monster": device_names_mm,
    "Mobile Monster As New Value": values_asnew_mm,
    "Mobile Monster Working Value": values_working_mm,
    "Mobile Monster Dead Value": values_dead_mm
}
df_combined = pd.DataFrame(data)

# Check time and date
time_now = datetime.datetime.now().strftime('%d-%m-%Y_%H_%M')

# Make Folder / change folder for Save code
if os.path.exists(r"C:\Price Scrap"):
    os.chdir(r"C:\Price Scrap")
    print("Price Scrap Folder Detected.")
else:
    os.mkdir(r"C:\Price Scrap")
    os.chdir(r"C:\Price Scrap")
    print("No Price Scrap Folder, Creating one.")

# Export the DataFrame to an Excel file
output_excel_filename = "Master Price Scrap_" + time_now + ".xlsx"
df_combined.to_excel(output_excel_filename, index=False)
print("That is a lot of Data. Your file has been saved to the Price Scrap folder in C Drive.")
print(f"Data exported to {output_excel_filename}")
print("  ")
print("If Prices is NA, it means Mazuma no longer offers any value.")
print("Tuan Chu")
print("Press Enter to Close")

input()
