from typing import Tuple
import json

def DoInput(msg: str, options: Tuple[str,...] = ("dd",)) -> str:
    print(msg)
    for opt in options:
        print(opt)
    ind=input("Selection: ")
    return ind


class Config:

    def __init__(self, jsonstr: str) -> None:
    
        jobject = json.loads(jsonstr)
        self._interval:float =  float(jobject['interval'])
        self._tracked = tuple(jobject['tracked'])
    
    @property
    def interval(self) ->float:
        return self._interval
    
    @property
    def tracked(self) -> Tuple[str,...]:
        return self._tracked

    