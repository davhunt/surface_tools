#!/usr/bin/env python

import os
import subprocess
import sys

tmpdir='/tmp/' + str(sys.argv[1])
fwhm=sys.argv[4]
#subjects_dir = os.path.dirname(os.path.realpath(sys.argv[3]))
subjects_dir = os.environ['SUBJECTS_DIR']
subject_id=os.path.basename(os.path.normpath(sys.argv[3]))
n_surfs=int(sys.argv[2])

for hemisphere in ("rh", "lh"):
	for areafile in (".area", ".area.pial"):
		if areafile == ".area":
			areaf = "white"
		elif areafile == ".area.pial":
			areaf = "pial"
		subprocess.call("mris_fwhm --s " + subject_id + " --hemi " + hemisphere + " --cortex --smooth-only --fwhm " + str(fwhm) + " --i " + os.path.join(subjects_dir,subject_id,"surf", hemisphere+areafile) + " --o " + os.path.join(tmpdir,"%s_%s_area.mgh" %(hemisphere,areaf)), shell=True)
		subprocess.call("cp " + os.path.join(subjects_dir,subject_id,"surf",hemisphere+"."+areaf) + " " + tmpdir, shell=True)
