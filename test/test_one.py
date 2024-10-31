from unittest import TestCase
from typing import cast
from profiling.process import *
from profiling.useinput import *
import json

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
        
        with self.assertRaises(Exception):
            tproc.Update(infobadname)
        tproc.Update(infogood1)

        self.assertEquals(1, tproc.instances)
        self.assertEquals(.2, tproc.cpu)
   
        tproc.Update(infogood2)
        self.assertEquals(2, tproc.instances)
        self.assertEquals(.5, tproc.cpu)
   


class ProcessChecktests(TestCase):

    def test_SetTrackedList(self):
        testset = ProcessCheck._SetTrackedList(("aaa","BBB","ccc"))
        self.assertListEqual(["aaa","BBB","ccc"], list(testset.keys())  )


class IntializationTest(TestCase):

    def test_config(self):
        jsondata = '{ "interval": 1.1, "tracked": ["aaa","bbb"]}'

        cfg = Config(jsondata)
        self.assertEquals(1.1,cfg.interval)
        self.assertEquals("aaa", cfg.tracked[0]  )
        self.assertEquals("bbb", cfg.tracked[1]  )

        