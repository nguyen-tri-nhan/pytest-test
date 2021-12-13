import pytest
import time
import _thread


def runTest():
    pytest.main(["2 Failed.py"])


for i in range(3):
    _thread.start_new_thread(runTest, ())
    time.sleep(10)
