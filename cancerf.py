def get_content_value(row_data):
    if(row_data.find('li')):
        return [row.get_text(" ",strip=True) for row in row_data.find_all('li') ]
    elif(', ' in row_data.get_text()):
        return row_data.get_text(" ",strip=True).split(', ')
    else:
        return row_data.get_text(" ",strip=True)