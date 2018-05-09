import pytest

import serial

from canlib import canlib
import uuid
import datetime

@pytest.fixture(scope="session")
def test_uuid():
    return uuid.uuid4()
    
@pytest.fixture(scope="session")
def test_time():
    return datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()

@pytest.fixture(scope="session")
def ser():
    ser = serial.Serial(port="COM5", baudrate=115200)
    yield ser
    if not ser.closed:
        ser.close()
            