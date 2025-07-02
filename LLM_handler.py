import file

import ollama
from ollama import chat
from ollama import ChatResponse

from tqdm import tqdm



def load_system_prompt(path:str = 'system_prompt.txt'):
    system_prompt = file.read_file(path,'',None)
    return system_prompt

def load_prompts(path:str = 'prompt.txt',seperator:str = '_'):
    prompts = file.read_file(path,seperator,None)
    return prompts

def generate_prompt(role:str,content:str):
    return {'role':role, 'content': content}

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
    

    if prompt_path == '':
        prompts = load_prompts()
    else:
        prompts = load_prompts(prompt_path)
    
    if conversation_name == '':
        conversation_name = "files/output.txt"
    else:
        conversation_path = f'files/conversations/{conversation_name}.txt'
        file.create_file(conversation_path)
    
    #pass system prompt
    chat(model,messages=[generate_prompt('system',system_prompt)])

    for prompt in tqdm(prompts,'prompting:'):
        response:ChatResponse = chat(model,messages=[generate_prompt('user',prompt)])


