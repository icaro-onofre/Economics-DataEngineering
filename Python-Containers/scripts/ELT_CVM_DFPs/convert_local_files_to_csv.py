import objects 
import schemas
import datetime
import pandas as pd
from os import listdir
from os.path import isfile, join
import os
import re


today = datetime.date.today()           
YearMonthDateFolder = objects.folderpath(year = str(today.year),month = str(today.month).zfill(2),day = str(today.day).zfill(2))

LandingZone = f"{objects.s3path(innerpath='landing').fullpath}/{YearMonthDateFolder}"
RawZone = f"{objects.s3path(innerpath='raw').fullpath}/{YearMonthDateFolder}"
ConsumeZone = f"{objects.s3path(innerpath='consume').fullpath}/{YearMonthDateFolder}"
EnrichedZone = f"{objects.s3path(innerpath='enriched').fullpath}/{YearMonthDateFolder}"

# Functions created to test if enviroment is up to dated
def path_check():  
    '''
    This function tests if the folder path is available 
    for Landing/year/month/day
    '''  
    if not os.path.exists(f"{objects.s3path(innerpath='landing').fullpath}/{YearMonthDateFolder}"):
        resp = f"Path {objects.s3path(innerpath='landing').fullpath}/{YearMonthDateFolder} isn't available"
    else:
        resp = f"Path {objects.s3path(innerpath='landing').fullpath}/{YearMonthDateFolder} is available" 
        return resp
        

'''
First Step
Unzip files from Landing Zone and then saving it into RawZone as CSV file
'''
def UnzipLandingToRaw():
    for file_name in os.listdir(LandingZone):
        objects.transform.ToRaw(file_name)

def FindDREfiles(param:str) -> list:
    """
    Finds and Lists all files that matches with DRE
    """
    FileList = []
    for file in os.listdir(RawZone):
        
        if re.findall(param,file):
            
            FileList.append(file)
           
    return FileList

def ReadDREFilesTransformAndSaveAsParquet():
# ,dtype=schemas.dre,na_values=schemas.dreNA
    fileList = FindDREfiles('DRE')
    # partition_cols='DENOM_CIA'
    for file in fileList[:]:  
        foldername = f"{str(file).strip('.csv')}/"
        schema = schemas.dre
        df = pd.read_csv(f'{RawZone}{file}',delimiter=';',encoding='ISO-8859-1')
        df['Transform_Date'] = pd.to_datetime('today').to_datetime64()
        os.makedirs(f"{ConsumeZone}{foldername}",exist_ok=True)
        file = str(file).strip('.csv')
        df.to_parquet(f"{ConsumeZone}{foldername}{file}_{pd.to_datetime('today').date()}.parquet",engine='pyarrow',partition_cols='DT_INI_EXERC')
        file = None
    return None
if __name__ == "__main__":
    print('Step 1 - Processing')
    print('Collecting data from landing and then unzinpping to rawzone')
    UnzipLandingToRaw()
    # print('Etapa 2 - Transformação')
    # print('Transferência da landing para raw completa')
    # print('coletando dados da camada raw e salvando na camada consume no formato parquet')
    # ReadDREFilesTransformAndSaveAsParquet()
    print('Files successfully stored into rawzone!')