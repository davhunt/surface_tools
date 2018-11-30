#!/bin/bash

tmpdir=$(( $RANDOM % 1000 ))
mkdir $tmpdir

mris_fwhm --s $SUBJECT --hemi $HEMI --cortex --smooth-only --fwhm $FWHM --i $SDFSDF --o $tmpdir/sm_area.mgh
