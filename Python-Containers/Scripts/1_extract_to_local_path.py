import requests
from bs4 import BeautifulSoup
import re
import os
import objects
import datetime 
import boto3
from botocore.exceptions import ClientError
import logging

'''
Variables
'''
today = datetime.date.today()           
YearMonthDateFolder = objects.folderpath(year = str(today.year),month = str(today.month).zfill(2),day = str(today.day).zfill(2))

url = 'https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')
'''
First Step
This piece aims to extract data from https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/
and to save into landing path as zipfiles
'''
LandingZone = f"{objects.s3path(innerpath='landing').fullpath}/{YearMonthDateFolder}"

def create_path_folder():
    if not os.path.exists(LandingZone):
        os.makedirs(LandingZone)
        describe = "Function deveoped to extract data from cvm"

url_list = list()
def storing_files():
    files_text = soup.get_text()
    file_list = re.findall(r'\b\w+\.zip\b',files_text)
        
    for i in file_list:
        ul = f'https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/{i}'
        # r = requests.get(f'https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/{i}')
        url_list.append(ul)    

    for url in url_list:
        _file = requests.get(url) 
        for fl in file_list:
            with open(f'{LandingZone}{fl}', 'wb') as file:
                file.write(_file.content)


if __name__ == "__main__":
    print('Step 1 - Setting up folder path')
    create_path_folder()
    print('Step 2 - Saving files into local Landing Zone ')
    storing_files() 
    print('Done!!')
    
    
