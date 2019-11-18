.PHONY: all noStatic noEnforcement run

all:
	../sdstool compile Printer.abs Printer.st

noStatic:
	../sdstool compile --noStaticChecks Printer.abs Printer.st

noEnforcement:
	../sdstool compile --noStaticChecks --noEnforcement Printer.abs Printer.st

run:
	gen/erl/run
