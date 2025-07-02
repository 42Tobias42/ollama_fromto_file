import file

import ollama
from ollama import chat
from ollama import ChatResponse

from tqdm import tqdm



def load_system_prompt(path:str = 'files/system_prompt.txt'):
    system_prompt = file.read_file(path,'',None)
    return system_prompt

def load_prompts(path:str = 'files/prompt.txt',seperator:str = '_'):
    prompts = file.read_file(path,seperator,None)
    return prompts

def generate_prompt(role:str,content:str):
    return {'role':role, 'content': content}

def generate_response(model:str,role:str,content:str,system_prompt:str|None)->ChatResponse:
    if system_prompt is not None:    
        return chat(model=model,messages= [generate_prompt('system',system_prompt),generate_prompt(role,content)],think=False)
    else: 
        return chat(model=model,messages= [generate_prompt(role,content)],think=False)


def run_LLM():
    
    #collect information
    model = input('model name:')
    conversation_name = input('conversation name:')
    system_prompt_path = input('system prompt path (empty if standard):')
    prompt_path = input('prompt path (empty if standard):')

   
    #check information
    if system_prompt_path == '':
        system_prompt = load_system_prompt()
    else:
        system_prompt = load_system_prompt(system_prompt_path)
    
    if system_prompt == '': system_prompt = None
    

    if prompt_path == '':
        prompts = load_prompts()
    else:
        prompts = load_prompts(prompt_path)
    
    if conversation_name == '':
        conversation_name = "files/output.txt"
    else:
        conversation_path = f'files/conversations/{conversation_name}.txt'
        file.create_file(conversation_path)


    for prompt in tqdm(prompts,'prompting:'):
        response = generate_response(model,'user',prompt,system_prompt)
        file.write_file(conversation_path,prompt,response.message.content)

    print(f'all file-prompts prompted')

    while True:
        prompt = input("prompt:")
        if prompt == 'exit': break

        response = generate_response(model,'user',prompt,system_prompt)
        file.write_file(conversation_path,prompt,response.message.content)




