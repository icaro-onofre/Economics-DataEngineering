import extract_to_local_path as extract_to_local_path

# import workspaces.pythonContainer.scripts.ELT.extract_to_local_path as extract_to_local_path
# from workspaces.pythonContainer.scripts.ELT import extract_to_local_path
def test_connection_status():
    '''Testing the extract_to_local_path'''
    url = extract_to_local_path.url
    api = extract_to_local_path.connection_status
    actual = str(api(url))
    expected = '200'
    assert actual == expected
    

    
    

    
