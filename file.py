from pathlib import Path

def read_file(path: str,seperator:str,sep_num:int|None) -> str|list[str]:
    '''
    reads information from path:
    returns content between sep_num-1 and sep_num seperator
    returns everything if no seperator is found or if seperator is empty str
    
    '''
    with open(path) as f:
        content = f.read()

    if seperator == '' or content.find(seperator) == -1:
        return content


    #seperate strings in array
    content_array = []

    array = content.partition(seperator)
    while array[-1] != "":
        content_array.append(array[0])
        array = array[-1].partition(seperator)
    else:
        content_array.append(array[0])

    #return string or content array
    if sep_num is None:
        return content_array
    else:
        return content_array[sep_num-1]


def create_file(path:str):
    with open(path,"w") as f:
        f.write('')

def write_file(path:str,prompt:str,content:str):
    with open(path,"a") as f:
        f.write(f'prompt: {prompt} \n')
        f.write(f'response: {content} \n\n')
