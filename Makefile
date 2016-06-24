SIM=ghdl
VHDL_SOURCES = $(PWD)/pwm.vhd
TOPLEVEL=pwm
MODULE=test_pwm
SIM_ARGS=--wave=test_pwm.ghw
include $(COCOTB)/makefiles/Makefile.inc
include $(COCOTB)/makefiles/Makefile.sim


mrproper:
	-rm -rf sim_build
	-rm -rf ${MODULE}.pyc
