#!/usr/bin/env python

import numpy as np
import io_mesh as io
import subprocess
import argparse
import os
import copy
import sys
import logging


def calculate_area(surfname,fwhm, software="CIVET", subject="fsid",surf="pial",hemi="lh"):
    """calculate and smooth surface area using CIVET or freesurfer"""
    tmpdir='/tmp/' + str(np.random.randint(1000))
    os.mkdir(tmpdir)
    if software == "CIVET" :
        try:
            subprocess.call("depth_potential -area_voronoi " + surfname + " " +os.path.join(tmpdir,"tmp_area.txt"),shell=True)
            if fwhm ==0:
                area=np.loadtxt(os.path.join(tmpdir,"tmp_area.txt"))
            else:
                subprocess.call("depth_potential -smooth " + str(fwhm) + " " + os.path.join(tmpdir,"tmp_area.txt ") + surfname + " "+os.path.join(tmpdir,"sm_area.txt"),shell=True)
                area=np.loadtxt(os.path.join(tmpdir,"sm_area.txt"))
            subprocess.call("rm -r "+tmpdir,shell=True)
        except OSError:
            print("depth_potential not found, please install CIVET tools or replace with alternative area calculation/data smoothing")
            return 0;
    if software == "freesurfer":
        if surf == "white":
            areafile=".area"
        elif surf == "pial":
            areafile=".area.pial"
        if 'lh' in surfname:
            hemi="lh"
        else:
            hemi="rh"
        if subject=="fsid":
            print("subject id not included")
            return 0;
        try:
            subprocess.call("mris_fwhm --s " + subject + " --hemi " + hemi + " --cortex --smooth-only --fwhm " + str(fwhm) + " --i "
                            + os.path.join(subjects_dir,subject,"surf", hemi+areafile) + " --o " + os.path.join(tmpdir,"sm_area.mgh"), shell=True)
            area=io.load_mgh(os.path.join(tmpdir,"sm_area.mgh"))
            subprocess.call("rm -r " + tmpdir, shell =True)
        except OSError:
            print("freesurfer tool failure, check mris_fwhm works and SUBJECTS_DIR is set")
            return 0;
    return area;
   

#parser = argparse.ArgumentParser(description='generate equivolumetric surfaces between input surfaces')
#parser.add_argument('gray', type=str, help='input gray surface')
#parser.add_argument('white', type=str, help='input white surface')
#parser.add_argument('n_surfs', type=int, help='number of output surfaces, also returns gray and white surfaces at 0 and 1')
#parser.add_argument('output', type=str, help='output surface prefix eg equi_left_{N}')
#parser.add_argument('--smoothing',type=int, help='fwhm of surface area smoothing. optional, default = 0mm')
#parser.add_argument('--software', type=str, help='surface software package CIVET or freesurfer, default is CIVET')
#parser.add_argument('--subject_id', type=str, help='subject name if freesurfer')
#args=parser.parse_args()


subjects_dir=os.getcwd()
fwhm=sys.argv[3]
software= 'freesurfer'
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


for hemisphere in ("rh", "lh"):
	wm = io.load_mesh_geometry(os.path.join(subjects_dir,subject_id,"surf",hemisphere+".white"))
	gm = io.load_mesh_geometry(os.path.join(subjects_dir,subject_id,"surf",hemisphere+".pial"))

	wm_vertexareas = calculate_area(os.path.join(subject_id,"surf",hemisphere+".white"),fwhm,software=software,surf="white", subject=subject_id,hemi=hemisphere)
	pia_vertexareas = calculate_area(os.path.join(subjects_dir,subject_id,"surf",hemisphere+".pial"), fwhm,software=software,surf="pial", subject=subject_id,hemi=hemisphere)



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
		#    if software == "CIVET":
		#        io.save_mesh_geometry(args.output+'{}.obj'.format(str(float(depth)/(n_surfs-1))),tmpsurf)
		#    elif software == "freesurfer":
    		subjects_dir=os.environ['SUBJECTS_DIR']
    		tmpsurf['volume_info']=gm['volume_info']
    		io.save_mesh_geometry(os.path.join(subjects_dir,subject_id,'surf','equi_'+hemisphere+'_{N}'+'{}.pial'.format(str(float(depth)/(n_surfs-1)))),tmpsurf)
