[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.1-blue.svg)](https://doi.org/10.25663/bl.app.1)

# Surface tools

Generate equivolumetric surfaces: creates equivolumetric surfaces based on the ratio of areas of the mesh surfaces, without the trouble of dealing with volumetric operations.

Takes WMC datatype as input and generates n equally spaced equivolumetric surfaces, that can then be viewed in Freesurfer. (i.e. n_surfs = 5 will generate the pial and white matter surfaces as well as 3 equally spaced intermediate surfaces)

The smoothing or "diffusion smoothing" value (fwhm, Full Width at Half Maximum of the Gaussian, in mm, default 0) determines the extent to which the surfaces are smoothed (e.g. sharp jumps in neighboring data points on the surfaces will be smoothed out, generally increasing the signal-to-noise ratio)

![equivolumetric](https://raw.githubusercontent.com/kwagstyl/surface_tools/master/equivolumetric_surfaces/images/equi_euclid_surfaces.png)
Equivolumetric surfaces (red) at 0.25, 0.5 and 0.75 cortical depth on the BigBrain. Euclidean surface (yellow) at mid depth. The euclidean surface samples different layers in gyri and sulci, while equivolumetric surfaces sample the gyri and sulci more consistently.

![graph](https://raw.githubusercontent.com/davhunt/pictures/master/euclidean%20vs%20equivolumetric.PNG)
Euclidean vs equivolumetric intensity sampling. The laminar peaks are better aligned using equivolumetric sampling than euclidean sampling.

The code requires FreeSurfer to be installed.

### Release notes
This code has so far been tested on:
- python 2.7 and 3.6, freesurfer v.6 and on linux (Ubuntu 16.04) and macOS (10.12.6)

### Authors
- Konrad Wagstyl (kw350@cam.ac.uk)
- David Hunt (davhunt@indiana.edu)

### Project director
- Franco Pestilli (franpest@indiana.edu)

### Acknowledgements:
Written by Konrad Wagstyl and Alexander Huth at a Brain Hack, a version is also available in Pyrocortex.
Casey Paquola and Richard Bethlehem were involved in piloting these scripts on CIVET and FreeSurfer respectively.

The io_mesh code was copied and adapted from https://github.com/juhuntenburg/laminar_python, another great tool for doing volume-based equivolumetric laminar processing.

The equations for generating equivolumetric surfaces come from Waehnert et al 2014: "Anatomically motivated modeling of cortical laminae" https://doi.org/10.1016/j.neuroimage.2013.03.078

Code is demo-ed here on the BigBrain (Amunts et al., 2013), freely available histological atlas of the human brain https://bigbrain.loris.ca/

### Funding 
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)

## Running the App 

### On Brainlife.io

You can submit this App online at [https://doi.org/10.25663/brainlife.app.126](https://doi.org/10.25663/brainlife.app.126) via the "Execute" tab.

### Running Locally (on your machine)

1. git clone this repo.
2. Inside the cloned directory, create `config.json` with something like the following content with paths to your input files.

```json
{
        "n_surfs": 5,
        "output": "./input/freesurfer/output",
        "smoothing": 5
}

3. Launch the App by executing `main`

```bash
./main
```

### Sample Datasets

If you don't have your own input file, you can download sample datasets from Brainlife.io, or you can use [Brainlife CLI](https://github.com/brain-life/cli).

```
npm install -g brainlife
bl login
mkdir input
bl dataset download 5a0662225ab38300be518f53 && mv 5a0662225ab38300be518f53 input/freesurfer
```

## Output

All output files will be generated under the current working directory (pwd). The main output of this App is a directory called `output_surfaces`. This file contains the 2n (rh and lh) generated equivolumetric surfaces (*.pial).

### Dependencies

This App only requires [singularity](https://www.sylabs.io/singularity/) to run. If you don't have singularity, you will need to install following dependencies.  

  - Freesurfer: https://surfer.nmr.mgh.harvard.edu/
  - jsonlab: https://www.mathworks.com/matlabcentral/fileexchange/33381-jsonlab-a-toolbox-to-encode-decode-json-files
  - NIBABEL: https://github.com/nipy/nibabel
  - NUMPY: https://github.com/numpy/numpy
