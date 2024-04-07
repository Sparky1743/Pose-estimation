# Pose-Estimation Using OpenPose Model
Implemented the human pose estimation using the OpenPose model. The folder "Open Pose" contains the codes to estimate the poses in images and videos. The videos processed by the model can be [found here](https://iitgnacin-my.sharepoint.com/:f:/g/personal/22110050_iitgn_ac_in/EsCh9PatjaBHjldrNO1yzo8BDKIGl4qDh5KZU5dvKPwADA?e=WeLBSl).

Required files for OpenPose models are downloaded from:
1) https://github.com/CMU-Perceptual-Computing-Lab/openpose
2) https://github.com/XeroLen23/OpenPose_dependencies

# MusclesInAction Model Installation Guide
Required files:
1) [vibe data](https://iitgnacin-my.sharepoint.com/:f:/g/personal/22110050_iitgn_ac_in/EtRhtOX9t3BJhX0EBC4f0N4BzSHOQ0HcJdJ21MfHfnhXXw?e=td8i7M)
2) [Dataset - 53gb](https://musclesinaction.cs.columbia.edu/MIADataset.tar)
   
To create a new conda environment:

```bash
conda create --name musclesinaction
```
To active the newly created environment:

```bash
conda activate musclesinaction
```
To ensure PyTorch works with CUDA, use the following command:

```bash
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
```
## System Specifications
1. **Operating System**: Windows 11
2. **GPU**: Nvidia GeForce RTX 3050
3. **IDE**: Visual Studio 2017, 2022
4. **CUDA Toolkit Version**:
   - nvcc: NVIDIA (R) Cuda compiler driver, version 12.4
5. **cuDNN Version**: 9.0.0
6. **GeForce Driver Version**: 551.86
7. **Cmake Version**: 3.27.0-rc2
   
## Conda Environment Description
- **Python**: 3.12.2
- **conda**: 23.7.2
- **pip**: 23.3.1
- [**Installed Libraries**](https://github.com/Sparky1743/Pose-estimation/blob/main/files/musclesinaction/pre_req.txt)

# References
### OpenPose Model:
1) https://github.com/CMU-Perceptual-Computing-Lab/openpose/issues/2227
2) https://www.youtube.com/watch?v=Fe3SJuQM7bs
3) https://github.com/raspberry-pi-maker/NVIDIA-Jetson
4) https://github.com/CMU-Perceptual-Computing-Lab/openpose/issues/1093

### MusclesInAction Model:
1) [model repo link](https://github.com/mchiquier/musclesinaction)
2) [No attribute 'getargspec' error](https://stackoverflow.com/questions/74585622/pyfirmata-gives-error-module-inspect-has-no-attribute-getargspec)
3) [PyTorch Using CUDA](https://github.com/krishnaik06/Pytorch-Tutorial/blob/master/Tutorial%206-%20Creating%20ANN%20with%20Pytorch%20On%20Pima%20Diabetes%20Dataset%20%26%20Training%20On%20GPU.ipynb)
4) [CUDA Toolkit 12.4](https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=11&target_type=exe_network)
5) [cuDNN 9.0.0](https://developer.nvidia.com/cudnn-downloads?target_os=Windows&target_arch=x86_64&target_version=Agnostic&cuda_version=12)
