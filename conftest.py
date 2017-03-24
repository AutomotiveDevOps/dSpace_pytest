import pytest
import os
import time

import rtplib2

@pytest.fixture(scope="module", params=["car", "van", "truck"])
def appl(request):
    # Setup
    print("Setup dSpace Appl")
    platformIdentifier = "SCALEXIO"
    applicationPath = r"C:\Vehicle\BuildResult\{}.sdf".format(request.param)
    app = rtplib2.Appl(applicationPath, request.param)
    app.battery = "on"
    yield app
    # Teardown
    print("Teardown dSpace Appl")
    app.battery = "off"
    del app