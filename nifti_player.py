import os

import matplotlib.pyplot as plt
import nibabel as nib

path = input('path to nifti file: ')

for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith('.nii'):
            my_img = nib.load(dirpath + '/' + filename)
            print(my_img.shape)
            nii_data = my_img.get_fdata()
            nii_aff = my_img.affine
            nii_hdr = my_img.header
            print(nii_aff, '\n', nii_hdr)
            print(nii_data.shape)
            print(nii_data.shape[2])
            if len(nii_data.shape) == 3:
                for slice_Number in range(nii_data.shape[2]):
                    plt.imshow(nii_data[:, :, slice_Number])
                    plt.show(block=False)
                    plt.pause(0.04)
                    plt.clf()

            if len(nii_data.shape) == 4:
                for frame in range(nii_data.shape[3]):
                    for slice_Number in range(nii_data.shape[2]):
                        plt.imshow(nii_data[:, :, slice_Number, frame])
                        plt.show(block=False)
                        plt.pause(0.04)
                        plt.clf()
