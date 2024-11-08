from typing import Tuple
import json
from pynput.keyboard import Key, KeyCode, Listener

def DoInput(msg: str, options: Tuple[str,...] = ("dd",)) -> str:
    print(msg)
    for opt in options:
        print(opt)
    ind=input("Selection: ")
    return ind


class Config:

    def __init__(self, jsonstr: str) -> None:
    
        jobject = json.loads(jsonstr)
        self._tag = jobject['tag']
        self._interval:float =  float(jobject['interval'])
        self._tracked = tuple(jobject['tracked'])
        self._outfile = jobject['outfile']
    
    @property
    def interval(self) ->float:
        return self._interval
    
    @property
    def tracked(self) -> Tuple[str,...]:
        return self._tracked
    
    @property
    def tag(self):
        return self._tag
    @property
    def outfile(self):
        return self._outfile
    

class KeyCheck:
    @staticmethod    
    def on_press(key: Key |KeyCode|None ):
        if key == Key.esc :
            # Stop listener
            print("Exiting")
            exit()  
    
    @staticmethod    
    def WaitForStop()-> None:
        # Collect events until released
        with Listener( on_press=KeyCheck.on_press) as listener:
            listener.join()
  