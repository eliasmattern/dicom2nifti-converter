import os

import SimpleITK as sitk

input_folder = input("Enter the path to the input DICOM folder: ")
output_folder = input("Enter the path to the output folder: ")

files = os.listdir(input_folder)
num = 1
for file in files:
    input_path = os.path.join(input_folder, file)
    if os.path.isdir(input_path):
        output_path = os.path.join(output_folder, os.path.basename(file))
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        print('######################################')
        try:

            reader = sitk.ImageSeriesReader()
            dicom_names = reader.GetGDCMSeriesFileNames(input_path)
            reader.SetFileNames(dicom_names)
            image = reader.Execute()

            image = sitk.PermuteAxes(image, [1, 0, 2])

            sitk.WriteImage(image, output_path + '/output.nii')
            print('created: ' + str(num))
            num += 1

        except Exception as _:
            print('Failed to convert directory: ' + file)
        print('######################################')
