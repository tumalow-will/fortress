import pandas as pd
import time
import os

import hoglundi.path
import hoglundi.drivers.modbus.codecs as codecs
import hoglundi.drivers.modbus.device as device

class Driver(object):
    name = 'solark'
    def __init__(self, power, modbus_args, register_map=None):
        register_map = self.default_register_map() if \
                            register_map is None else register_map

        #example modbus_args
        #{'type': 'TCP', 'host': 192.169.1.10, 'port':5205}
        self.device = device.Device(modbus_args=modbus_args,
                                register_map=register_map,
                                unit=1)
        self.power = power

    def default_register_map(self):
        here = hoglundi.path.here(__file__)
        default_location = os.path.join(here, 'solark.map.csv')
        df = pd.DataFrame.from_csv(default_location, index_col=None)
        #returns a list of dictionaries
        register_map = df.to_dict('records')
        return register_map

    def tearDown(self):
        return self.device.tearDown()

    def status(self):
        #include faults here too
        return {}

    def read(self, name):
        return self.device.read_holding_registers(name)

    def write(self, name, value):
        return self.device.write_registers(name, value)

    def ensure(self, name, value):
        curr_val = self.read(name)
        if curr_val != value:
            self.write(name, value)

    def read_operating_state(self):
        state_val = self.read('Operating State')
        states = {}
        return states[state_val]

if __name__ == '__main__': 
    import coosbay
    coosbay.start(__file__)
    #import sys
    #host = sys.argv[1]
    #port = int(sys.argv[2])


    modbus_args = {'type': 'RTU',
                    'port': '/dev/ttyUSB0',
                    'baudrate': 9600
                    }
    dr = Driver(power=5, modbus_args=modbus_args)
    dev = dr.device
    sclient = dev.client
    client = sclient.client
    import pdb; pdb.set_trace()
