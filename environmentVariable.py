import os
def run(**args):
	print "[*] In environment module."
	for i in os.environ:
		print(i)

run()
