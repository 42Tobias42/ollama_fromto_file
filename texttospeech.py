from dia.model import Dia
import soundfile as sf



def text_to_speech(text:str , seed:int|None):
    '''
    generates speech from text input.

    seed: not implemented
    '''
    
    model = Dia.from_pretrained()

    output = model.generate(text)

    sf.write("output.mp3",output,44100)
