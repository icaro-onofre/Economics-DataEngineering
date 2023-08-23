import convert_local_files_to_csv as convert_local_files_to_csv
import datetime 
import objects as objects

convert_local_files_to_csv.path_check()

today = datetime.date.today()           
YearMonthDateFolder = objects.folderpath(year = str(today.year),month = str(today.month).zfill(2),day = str(today.day).zfill(2))

def test_path_check():
    '''This function asserts if the landing path is up to dated
    for today in the format year/month/day'''
    path = convert_local_files_to_csv.path_check
    actual = path()
    expected = f"Path {objects.s3path(innerpath='landing').fullpath}/{YearMonthDateFolder} is available"
    assert actual == expected
    
def test_FindDREfiles():
    '''Testing if DRE files were saved in today's rawzone folder path'''
    find = convert_local_files_to_csv.FindDREfiles
    actual = bool(find('DRE'))
    expected = True
    assert actual == expected
    
    

    
