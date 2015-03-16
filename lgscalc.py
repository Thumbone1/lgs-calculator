# File: lgscalc.py
# For calculating low gravity solids when using calcium carbonate
# Written by: Judge Gambill

def main():
	init_lgs_prcnt = float(raw_input("input initial lgs percent > "))
	init_lgs_wt = float(raw_input("input initial lgs by weight > "))
	caco3_wt = float(raw_input("input calcium carbonate lb/bbl > "))

	corrected_lgs_prcnt = init_lgs_prcnt - (caco3_wt * init_lgs_prcnt / init_lgs_wt)
	corrected_lgs_wt = init_lgs_wt - caco3_wt

	print "corrected lgs percent is %r" % corrected_lgs_prcnt
	print "corrected lgs lb/bbl is %r" % corrected_lgs_wt

main()
