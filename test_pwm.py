import logging
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge
from cocotb.triggers import FallingEdge

PS = 1
NS = 1000*PS
US = 1000*NS
MS = 1000*US

# 62.5Mhz
HALF_CLK = 8*NS

@cocotb.coroutine
def reset_dut(reset, duration):
    reset <= 0
    yield Timer(duration)
    reset <= 1
    yield Timer(duration)
    reset.log.info("Reset complete")


class PwmTest(object):
    """ Test class """
    def __init__(self, dut):
        self.dut = dut

    @cocotb.coroutine
    def init_sig(self):
        """ initialize signals """
        self.clock_thread = cocotb.fork(Clock(self.dut.clk, 2*HALF_CLK).start())
        yield reset_dut(self.dut.reset_n, 12*NS)
        yield Timer(1*NS)

###################
# Tests
@cocotb.test()
def test_simple(dut):
    """
        Testing  simple
    """
    testobj = PwmTest(dut)
    dut.ena <= 0
    dut.reset_n <= 1
    dut.duty <= 200
    yield testobj.init_sig()
    dut.ena <= 1
    yield Timer(1*MS)
