import pytest
from Level1.SearchFile import FileFinder
from Level1.SystemDriveFinder import SystemDriveFinder
class Test_Drive:
    def test_DriveCase(self):
        obj=SystemDriveFinder()
        self.expected=obj.find_drives()
        self.actual=['C']
        assert self.expected==self.actual
    def test_searchfile(self):
        obj=FileFinder()
        d=obj.find_file('demo.txt','C:\\')
        act=['C:\\Hcl1\\demo.txt', 'C:\\Hcl2\\demo.txt']
        self.expected=act
        self.actual_res=d
        assert self.expected==self.actual_res


