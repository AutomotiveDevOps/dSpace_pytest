import pytest
import os

import rtplib2

@pytest.fixture(scope="module", params=["car", "van", "truck"])
def appl(request):
    print("setup appl")
    platformIdentifier = "SCALEXIO"
    applicationPath = r"C:\TurnSignal_SCALEXIO\BuildResult\turnlamp.sdf"
    yield rtplib2.Appl(applicationPath, request.param)
    # Teardown
    print("teardown appl")

# Enhancing pytest-html reports 
# https://pypi.python.org/pypi/pytest-html#enhancing-reports
def pytest_configure(config):
    # Add the computer, user and domain to the header.
    for field in ["COMPUTERNAME", "USERNAME", "USERDOMAIN"]:
        config._metadata[field] = os.getenv(field, None)

    # This adds Jenkins environmental variables to the report header.
    for field in ["BUILD_URL", "BUILD_TAG", "WORKSPACE", "GIT_COMMIT", "GIT_BRANCH"]:
        config._metadata[field] = os.getenv(field, None)