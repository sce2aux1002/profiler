from threading import Timer
from time import time
from profiling.process import ProcessCheck,ProcInfo,theloop, ProcInfoDict
from typing import Dict,cast,Any
from datetime import datetime
from profiling.useinput import *
import psutil
import os





def list_running_processes_with_cpu( DProcInfo: ProcInfoDict, XTRA: Tuple[str,Any]  ):


    for key in DProcInfo.keys(): DProcInfo[key].Reset() #cr

    """Lists all running processes on the system, including CPU utilization."""
    
    for i in range(2):
  
        if i== 1:        
            ProcInfo.Tag = XTRA[0]
            ProcInfo.Timestamp = datetime.now()

        for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent']):

            if i == 0 or proc.info['name'] not in DProcInfo.keys():   
                continue
            DProcInfo[proc.info['name']].Update(proc.info)                         
            #cpu_usage = proc.info['cpu_percent'] 
            #print(f" PID: {proc.info['pid']}, Name: {proc.info['name']}, User: {proc.info['username']}, CPU Usage: {cpu_usage}% Tag: {ProcInfo.Tag} TS: {ProcInfo.Timestamp}")
            
       
    for key in DProcInfo.keys():
        PI=DProcInfo[key]
        M: str = f"{PI.name},{PI.instances},{PI.cpu},{PI.Tag},{PI.Timestamp}\n"
        XTRA[1].write(M)
        #print(f"**Name: {PI.name} Instances: {PI.instances} CPU: {PI.cpu} Tag: {PI.Tag} TS:{PI.Timestamp} X:{XTRA[0]}" )


class PARAMS:
    Tag: str = "Tagging"
    intv: float = 2.5
    tracked: Tuple[str,...] = ("POWERPNT.EXE", )


if __name__ == "__main__":
#timer = ProcessCheck.SetUpTracking(2, ("chrome.exe", ) )
    ff = open("myfile.xtx","w")
    ff.write("Name,Instances,CPU,Timestamp,Tag\n")
    extras = (PARAMS.Tag,ff)
    timer = ProcessCheck.SetUpTracking(PARAMS.intv, PARAMS.tracked, list_running_processes_with_cpu,extras )

    while(True):
        sel = DoInput("Start Menu",("\t1. Start", "\t2. Cancel"))
        match sel:
            case "1":
                print("starting")
                print("Press return in window to quit")
                timer.start()
                input()                
                timer.cancel()
                timer.join()
                break
            case "2":
                print("cancelled")
                break
            case _:
                print("Invalid Option")
    



    ff.close()
    print("done")