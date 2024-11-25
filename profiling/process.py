from threading import Timer
from typing import NamedTuple, Iterable, Callable, Dict
from datetime import datetime
from typing import Dict, Any
from psutil import Process,cpu_count, process_iter



ProcClass = Process



class ProcInfo():
    Timestamp: datetime;
    Tag: str
    
    @staticmethod
    def GetCpuCount() -> int:
        return cpu_count()
    
    @staticmethod
    def GetProcesses() ->Iterable[ProcClass]:
        return process_iter(['pid', 'name', 'username', 'cpu_percent'])


    def __init__(self, name: str) -> None:
        self._name = name
        self._reset()
        
    def _reset(self):
        self._instances: int = 0
        self._cpu: float = 0.0
    
    @property
    def name(self) -> str:
        return self._name
    @property
    def instances(self) -> int:
        return self._instances
    @property    
    def cpu(self) -> float:
        return self._cpu
    
    def Update(self, info: dict[str,Any] , cpus = 1 ) -> None:
        if info['name'] != self._name :
            raise(Exception)
        self._instances += 1
        self._cpu += info['cpu_percent'] / cpus
    
    def Reset(self) -> None:
        self._reset()

class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

ProcInfoDict =  Dict[str, ProcInfo] 

ProcCallback = Callable[[ProcInfoDict,Any], None]




def theloop( procs: Dict[str, ProcInfo] = {}):
        print(f"Interval: {ProcessCheck._Interval}  Names:{ list(procs.keys())}")
        pass 
    
class ProcessCheck():
    _Interval:float = 2.2

    @staticmethod
    def _SetTrackedList( trackedNames: Iterable[str] ) -> Dict[str,ProcInfo]:
        rval = {}
        for tn in trackedNames:  
            rval[tn] = ProcInfo(tn)
        return rval
    


    # @staticmethod
    # def SetUpTracking( intv: float, trackedNames: Iterable[str],  cback: Callable[ [Dict[str,ProcInfo]],Any]  = theloop )-> RepeatTimer:

    #     ProcessCheck._Interval = intv
    #     # def theloop(i: float, d:Dict[str, ProcInfo]):
    #     #     print(f"Interval: {i}  Names:{d.keys()}")
    #     #     pass 

    #     rval = RepeatTimer( ProcessCheck._Interval, cback, None, {'procs': ProcessCheck._SetTrackedList(trackedNames)}  ) 
    #     return rval
    
    @staticmethod
    def SetUpTracking( intv: float, trackedNames: Iterable[str],  cback: ProcCallback , extra: Any = None )-> RepeatTimer:

         ProcessCheck._Interval = intv
         # def theloop(i: float, d:Dict[str, ProcInfo]):
         #     print(f"Interval: {i}  Names:{d.keys()}")
         #     pass 

         rval = RepeatTimer( ProcessCheck._Interval, cback, [ProcessCheck._SetTrackedList(trackedNames),extra]  ) 
         return rval

    @staticmethod
    def GenHeader( DPI: ProcInfoDict )  -> str:
        retval: str = 'Timestamp,Tag,'.join(DPI.keys())
        return retval
    @staticmethod
    def GenRecord( DPI: ProcInfoDict) ->str:
        
        retval:  str = "{0},{1}".format(ProcInfo.Timestamp,ProcInfo.Timestamp)
        #for PI in DPI:


        return ""



                           
                           

