from unittest import TestCase
from typing import cast
from profiling.process import *
from profiling.useinput import *
import json
import sys

class ProcessInfoTests(TestCase):
    proc: ProcInfo| None = None


    def test_create(self):
        tproc: ProcInfo =ProcInfo("foo.bar")
        self.assertEquals("foo.bar", tproc.name)
        self.assertEquals(0.0,tproc.cpu)      
        


    def test_Update(self):
        tproc: ProcInfo =ProcInfo("foo.bar")
        infobadname: Dict[str,Any] = {"name": "foox.bar","cpu_percent": 0.24}
        infogood1: Dict[str,Any] = {"name": "foo.bar","cpu_percent": 0.2}
        infogood2: Dict[str,Any] = {"name": "foo.bar","cpu_percent": 0.3}
        infogood3: Dict[str,Any] = {"name": "foo.bar","cpu_percent": 10.4}
        
        with self.assertRaises(Exception):
            tproc.Update(infobadname)
        tproc.Update(infogood1)

        self.assertEquals(1, tproc.instances)
        self.assertEquals(.2, tproc.cpu)
   
        tproc.Update(infogood2)
        self.assertEquals(2, tproc.instances)
        self.assertEquals(.5, tproc.cpu)

        tproc.Reset()
        self.assertEquals(0, tproc.instances)
        tproc.Update(infogood3, cpus=2)
        self.assertEquals(1, tproc.instances)
        self.assertEquals(5.2, tproc.cpu)



   


class ProcessChecktests(TestCase):

    def test_SetTrackedList(self):
        testset = ProcessCheck._SetTrackedList(("aaa","BBB","ccc"))
        self.assertListEqual(["aaa","BBB","ccc"], list(testset.keys())  )

    def test_getdata(self):
        x = [1,3,4]
        x.pop()
        x.insert(0,2)
        print(set(x).difference([1,3,4]))
        print(set(x).difference([2,1,3]))
        

class IntializationTest(TestCase):

    def test_config(self):
        jsondata = ""


        with open('test/files/testSetup.cfg', 'r') as file:
            jsondata = file.read()
            



        cfg = Config(jsondata)
        self.assertEquals(1.1,cfg.interval)
        self.assertEquals("aaa", cfg.tracked[0]  )
        self.assertEquals("bbb", cfg.tracked[1]  )
        self.assertEquals("TAG",cfg.tag)
        self.assertEquals("outfile.csv",cfg.outfile)
    
 
