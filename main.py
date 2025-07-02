from ollama import chat
from ollama import ChatResponse

import file
import LLM_handler as LLM



def prompt_to_file(model:str, system_prompt_path: str = 'system_prompt.txt',prompt_path: str = 'prompt.txt'):
    '''
    This function inputs the prompts contained in system_prompt and prompt to the provided model
    
    '''
    #read system prompt
    with open(system_prompt_path) as f:
        system_prompt = f.read()
        print(f'system: {system_prompt}')
    
    #read prompt
    with open('prompt.txt') as f:
        prompt = f.read()
        print(f'prompt: {prompt}')

    #pass system prompt
    if system_prompt.strip() == "":    
        #chat(model=model, messages=[{'role':'system', 'content': system_prompt}])
        print('No system_prompt provided')
    
    #pass prompt
    if prompt.strip() != '':
        response:ChatResponse = chat(model=model, messages=[{'role':'system', 'content': system_prompt},{'role':'user', 'content': prompt}])
    else:
        raise ValueError('No prompt provided')
    
    #save output
    with open('output.txt','a') as f: 
        f.write(response.message.content)
    print(response.message.content)



#model = input('model name:')
#prompt_to_file(model)



LLM.run_LLM()

    

