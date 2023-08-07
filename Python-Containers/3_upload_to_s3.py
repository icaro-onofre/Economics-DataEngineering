import logging
import boto3
from botocore.exceptions import ClientError
import os
import objects
import datetime
from dotenv import load_dotenv,dotenv_values
load_dotenv()

aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key = os.getenv("aws_secret_access_key")
region_name = 'us-east-2'

today = datetime.date.today()           
YearMonthDateFolder = objects.folderpath(year = str(today.year),month = str(today.month).zfill(2),day = str(today.day).zfill(2))

LandingZone = f"{objects.s3path(innerpath='landing').fullpath}/{YearMonthDateFolder}"
RawZone = f"{objects.s3path(innerpath='raw').fullpath}/{YearMonthDateFolder}"
ConsumeZone = f"{objects.s3path(innerpath='consume').fullpath}/{YearMonthDateFolder}"
EnrichedZone = f"{objects.s3path(innerpath='enriched').fullpath}/{YearMonthDateFolder}"

def s3_upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket
            :param file_name: File to upload
            :param bucket: Bucket to upload to
            :param object_name: S3 object name. If not specified then file_name is used
            :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3',
                             aws_access_key_id=aws_access_key_id, 
                            aws_secret_access_key=aws_secret_access_key, 
                            region_name=region_name)
    try:
        response = s3_client.upload_file(file_name, bucket, f'{YearMonthDateFolder}{object_name}')
    except ClientError as e:
        logging.error(e)
        return False
    return True


# file_name = r"C:/Users/SALA443/Desktop/Okonomicus-Containers/S3/RawZone/2023/07/25/dfp_cia_aberta_DVA_ind_2023.csv"
# bucket = "de-okkus-landing-zone-dev-727477891012"
# object_name = "dfp_cia_aberta_2023"
# upload_file(file_name, bucket, object_name=None)

directory = RawZone
# directory = r'C:\Users\SALA443\Desktop\Okonomicus-Containers\S3\RawZone\2023\07\25'
bucket = "de-okkus-landing-zone-dev-727477891012"
def s3_upload_file_iterate_source():    
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
    
        if os.path.isfile(f):
            s3_upload_file(f, bucket, object_name=None)
            # print(filename)

if __name__ == "__main__":
    print('Getting csv files from local path and saving it into s3 bucket')
    s3_upload_file_iterate_source()
    print('Done!!')