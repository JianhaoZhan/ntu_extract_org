# ntu_extract_org

This repository is used to extract the RGB with skeleton files in NTU-RGB-D dataset:

1.To the environment, you only need to : 

```
conda install python=3.7.1
pip install opencv-python
```

2.You should download NTU-RGB-D dataset in https://rose1.ntu.edu.sg/dataset/actionRecognition/, including RGB_video and .skeleton files.

how to extract RGB frames from video, you can follows : https://github.com/JianhaoZhan/RGB-Flow_extrating

3.Make your file structure as follows:
  SKELETON_PATH/\*.skeleton
  RGB_PATH/nturgbd_rgb_s00\*/SxxxCxxxPxxxRxxxAxxx/xxxxx.jpg
  
4.run: (where: SKELETON_PATH is the path of xx.skeleton files, TARGET_PATH is the path where you save processed files, and RGB_PATH is the RGB frame path you extract from video)
  ```python
  python generate.py SKELETON_PATH TARGET_PATH RGB_PATH
  ```
  as example:
  ```python
  python generate.py /New-8T/mars/ntu60  /New-8T/mars/NTU-Skeleton  /New-8T/mars/NTU_RGB
  ```
  
  and the result as follows:
  ![result](https://github.com/JianhaoZhan/ntu_extract_org/blob/main/others.jpg)
