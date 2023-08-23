import upload_to_s3 as upload_to_s3
import datetime 
import objects as objects

today = datetime.date.today()           
YearMonthDateFolder = objects.folderpath(year = str(today.year),month = str(today.month).zfill(2),day = str(today.day).zfill(2))
schema = """['CNPJ_CIA', 'DT_REFER', 'VERSAO', 'DENOM_CIA', 'CD_CVM', 'GRUPO_DFP', 'MOEDA', 'ESCALA_MOEDA', 'ORDEM_EXERC', 'DT_INI_EXERC', 'DT_FIM_EXERC', 'CD_CONTA', 'DS_CONTA', 'VL_CONTA', 'ST_CONTA_FIXA']"""
 
def test_gettingDREschemas():
    '''This function asserts if DRE file schemas are correct'''
    schemas = upload_to_s3.gettingDREschemas
    actual = str(schemas())
    expected = schema
    print(actual)
    assert actual == expected
    
# test_gettingDREschemas()

    
    

    
