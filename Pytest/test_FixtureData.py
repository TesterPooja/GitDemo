import pytest

from Pytest.BaseClass import BaseClass


# @pytest.mark.usefixtures("dataload")
class TestExample2(BaseClass):

    def test_editprofile(self, dataload):     # you have to pass fixture name in parameter though you are
        print(dataload)                       # globally using it, because you are returning the data
        print(dataload[1])                    # it's ok if you do not declare usefixture outside class

        log = self.test_getlogger()   # accessing getlogger method from base class and creating object
        log.info(dataload)      # logging means printing only however it will print or log in
        log.info(dataload[1])   # html report as well
