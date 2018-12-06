#!/usr/bin/env python

import numpy as np
import io_mesh as io
import subprocess
import argparse
import os
import copy
import sys
import logging

fwhm=sys.argv[3]
software= 'freesurfer'
subjects_dir = '/usr/local/freesurfer/subjects'
subject_id=os.path.basename(os.path.normpath(sys.argv[2]))
n_surfs=int(sys.argv[1])

def beta(alpha, aw, ap):
    """Compute euclidean distance fraction, beta, that will yield the desired
    volume fraction, alpha, given vertex areas in the white matter surface, aw,
    and on the pial surface, ap.

    A surface with `alpha` fraction of the cortical volume below it and 
    `1 - alpha` fraction above it can then be constructed from pial, px, and 
    white matter, pw, surface coordinates as `beta * px + (1 - beta) * pw`.
    """
    if alpha == 0:
        return np.zeros_like(aw)
    elif alpha == 1:
        return np.ones_like(aw)
    else:
        return 1-(1 / (ap - aw) * (-aw + np.sqrt((1-alpha)*ap**2 + alpha*aw**2)))

os.mkdir('output_surfaces')
out_dir = os.path.join(os.getcwd(),'output_surfaces')

for hemisphere in ("rh", "lh"):

	wm = io.load_mesh_geometry(os.path.join('/tmp',str(sys.argv[4]),hemisphere+".white"))
	gm = io.load_mesh_geometry(os.path.join('/tmp',str(sys.argv[4]),hemisphere+".pial"))

	wm_vertexareas = io.load_mgh(os.path.join('/tmp',str(sys.argv[4]),'%s_white_area.mgh' %hemisphere))
	pia_vertexareas = io.load_mgh(os.path.join('/tmp',str(sys.argv[4]),'%s_pial_area.mgh' %hemisphere))

	vectors= wm['coords'] - gm['coords']
	tmpsurf= copy.deepcopy(gm)
	#create mask where vertex coordinates match
	mask = vectors.sum(axis=1)!=0

	#number of equally space intracortical surfaces (eg 5 is 0, 0.25, 0.5, 0.75, and 1)
	for depth in range(n_surfs):
    		print("creating surface " + str(depth +1))
    		betas = beta(float(depth)/(n_surfs-1), wm_vertexareas[mask], pia_vertexareas[mask])
    		betas = np.nan_to_num(betas)
    		tmpsurf['coords'][mask] = gm['coords'][mask] + vectors[mask]* np.array([betas]).T
    		tmpsurf['volume_info']=gm['volume_info']
    		io.save_mesh_geometry(os.path.join(out_dir,'equi_'+hemisphere+'_{N}'+'{}.pial'.format(str(float(depth)/(n_surfs-1)))),tmpsurf)

subprocess.call("rm -r " + os.path.join('/tmp',str(sys.argv[4])), shell=True)
