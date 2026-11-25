<h1 align="center">Generate Equivolumetric Surfaces</h1>

<p align="center">
  Generates n equivolumetric intracortical surfaces between the FreeSurfer white and pial surfaces of each hemisphere, using vertex-area ratios, for laminar sampling.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.126"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.126-blue.svg" alt="Run on brainlife.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-see_LICENSE-lightgrey.svg" alt="License"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Generates n equivolumetric intracortical surfaces between the FreeSurfer white and pial surfaces of each hemisphere, using vertex-area ratios, for laminar sampling.**

Smooths the white and pial vertex-area maps with FreeSurfer mris_fwhm, then builds n_surfs surfaces from white to pial whose depth follows the equivolumetric model of Waehnert et al. (2014), so the same cortical layers are sampled in gyri and sulci. Use it for laminar or depth-dependent analyses of cortical data. It needs a FreeSurfer subject directory with white and pial surfaces and area files.

| | |
|---|---|
| **Inputs** | `neuro/freesurfer` |
| **Outputs** | `raw` |
| **Container** | `brainlife/freesurfer:6.0.0` |
| **Resources** | 1 CPUs |
| **Requires** | `FREESURFER_LICENSE` |
| **Run it** | [doi.org/10.25663/brainlife.app.126](https://doi.org/10.25663/brainlife.app.126) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `freesurfer` | `neuro/freesurfer` | yes | FreeSurfer subject directory (recon-all output). Must contain surf/?h.white, ?h.pial, ?h.area and ?h.area.pial for both hemispheres. |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `output_surfaces` | `raw` | FreeSurfer-format surfaces for each hemisphere at evenly spaced equivolumetric depths from white (0) to pial (1), named equi_<hemi>_{N}<depth>.pial. |

<details>
<summary><b>Parameters</b> (2)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `smoothing` | number | `0` | fwhm value for smoothing |
| `n_surfs` | number | `5` | Number of surfaces to generate, including the white and pial boundaries (e.g. 5 gives depths 0, 0.25, 0.5, 0.75, 1). |

</details>

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.126](https://doi.org/10.25663/brainlife.app.126), choose `neuro/freesurfer` from your project, set the parameters and press **Execute**. The results are saved to your project as `raw`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `brainlife/freesurfer:6.0.0`), [`jq`](https://jqlang.github.io/jq/), `FREESURFER_LICENSE`.

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "output": "/path/to/freesurfer/output",
       "smoothing": 0,
       "n_surfs": 5
   }
   ```

3. Run `./main`.

## Troubleshooting

- **Please set FREESURFER_LICENSE in .bashrc**: Set FREESURFER_LICENSE in the execution environment.

## Release notes

This code has so far been tested on:
- python 2.7 and 3.6, freesurfer v.6 and on linux (Ubuntu 16.04) and macOS (10.12.6)

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- Generate Equivolumetric Surfaces. brainlife.io App. [doi:10.25663/brainlife.app.126](https://doi.org/10.25663/brainlife.app.126)
- Waehnert MD, et al. Anatomically motivated modeling of cortical laminae. NeuroImage (2014). [doi:10.1016/j.neuroimage.2013.03.078](https://doi.org/10.1016/j.neuroimage.2013.03.078)
- Fischl. FreeSurfer. *NeuroImage* 62:774-781 (2012). [doi:10.1016/j.neuroimage.2012.01.021](https://doi.org/10.1016/j.neuroimage.2012.01.021)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- Konrad Wagstyl
- David Hunt

**Project director**

- Franco Pestilli

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io, which runs this App, is publicly funded by Wellcome, the U.S. National Institutes of Health and the U.S. National Science Foundation; acknowledging that support helps keep it running.</sub>

## License

See [LICENSE](LICENSE).
