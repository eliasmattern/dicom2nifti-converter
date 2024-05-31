# DICOM to NIfTI Converter

This tool converts DICOM files to NIfTI format.

## Installation
To use PsyTestPro python must be installed:
[Download here](https://www.python.org/downloads/)

There are also some dependencies that must be installed using pip:
```shell
# For converter:
pip install SimpleITK

# For player:
pip install nibabel
pip install matplotlib
```

## How It Works

The converter takes an input directory containing subdirectories of DICOM files and converts each subdirectory into a corresponding NIfTI file in the specified output directory.

## Usage

1. **Input Directory**: Specify the path to the directory containing the subdirectories with DICOM files.
2. **Output Directory**: Specify the path where the converted NIfTI files will be saved.

### Details

- Each subdirectory in the input directory should contain DICOM files.
- For each subdirectory, a corresponding folder with the same name will be created in the output directory.
- Inside each output subdirectory, the converted NIfTI file will be stored.

### Example

If the input directory is structured as follows:

```
input_directory/
├── patient1/
│   ├── image1.dcm
│   ├── image2.dcm
│   └── ...
├── patient2/
│   ├── image1.dcm
│   ├── image2.dcm
│   └── ...
└── ...
```

After conversion, the output directory will be structured as follows:

```
output_directory/
├── patient1/
│   └── converted_image.nii
├── patient2/
│   └── converted_image.nii
└── ...
```


### Instructions

1. Run the converter and provide the paths to the input and output directories when prompted.
2. The converter will process each subdirectory and save the resulting NIfTI files in the specified output directory.

## NIfTI Player

The NIfTI player allows you to visualize NIfTI files by playing them as a sequence of images, making it look like a film. This helps you verify if the NIfTI files look correct.

### How It Works

1. The player prompts you for the path to a directory.
2. It processes each NIfTI file found in the directory, displaying the images in sequence.

### Instructions

1. Run the NIfTI player and provide the path to the directory containing the NIfTI files when prompted.
2. The player will display each NIfTI file found in the directory, showing the images in sequence.

This tool simplifies the process of converting DICOM files to the widely-used NIfTI format, making it easier to handle and analyze medical imaging data.

Feel free to contribute or report any issues you encounter!
