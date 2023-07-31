import datetime
import time
import zipfile

class folderpath():
    """This object builds folder structure to store daily data 
    within year-month-date
    """
    def __init__(self,year:str,month:str,day:str):
        
        self.year = year
        self.month = month
        self.day = day

    @property
    def daily(self) -> str:
        return f"{self.year}/{self.month}/{self.day}"
    
    def __str__(self) -> str:
        return f"{self.year}/{self.month}/{self.day}/"
    
class s3path():
    """This object builds folder structure of S3 datalake
    """
    def __init__(self,innerpath:str):        
        self.innerpath = innerpath
        
    @property   
    def fullpath(self) -> str:
        if self.innerpath == 'landing':
            return "C:/Users/SALA443/Desktop/Okonomicus-Containers/S3/LandingZone"
        elif self.innerpath == 'raw':
            return "C:/Users/SALA443/Desktop/Okonomicus-Containers/S3/RawZone"
        elif self.innerpath == 'consume':
            return "C:/Users/SALA443/Desktop/Okonomicus-Containers/S3/ConsumeZone"
        elif self.innerpath == 'enriched':
            return "C:/Users/SALA443/Desktop/Okonomicus-Containers/S3/EnrichedZone"
        else:
            return "caminho inexistente"  
        
class transform():
    
    def ToRaw(file:str):
        """
        This method extracts zip files from a folder and stores inside another given folder
        """
        with zipfile.ZipFile(f"{s3path(innerpath='landing').fullpath}/{folderpath(year = str(datetime.date.today().year),month = str(datetime.date.today().month).zfill(2),day = str(datetime.date.today().day).zfill(2))}/{file}", 'r') as zip_ref:
            zip_ref.extractall(f"{s3path(innerpath='raw').fullpath}/{folderpath(year = str(datetime.date.today().year),month = str(datetime.date.today().month).zfill(2),day = str(datetime.date.today().day).zfill(2))}")

    # def ToConsume():
    #     """
    #     This method reads csv files from a folder, transform and stores inside another given folder
    #     adding the loaded_date field.
    #     """
class aws_s3_buckets():
    def __init__(self,innerpath:str):        
        self.innerpath = innerpath
        
    @property   
    def fullpath(self) -> str:
        if self.innerpath == 'landing':
            return "de-okkus-landing-zone-dev-727477891012"
        elif self.innerpath == 'bronze':
            return "de-okkus-bronze-layer-dev-727477891012"
        elif self.innerpath == 'gold':
            return "de-okkus-gold-layer-dev-727477891012"
        elif self.innerpath == 'silver':
            return "de-okkus-silver-layer-dev-727477891012"
        elif self.innerpath == 'scripts':
            return "de-okkus-scripts-dev-727477891012"
        else:
            return "caminho inexistente"  
    

        

        

