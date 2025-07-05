<p align="center">
  <img src="imgs/logo3d_983940088pizapw1553754827_square_grey.png" width="200" alt="pairs3d logo">
</p>
<p align="center"><u><b>
  pairs3d  
</b></u></p>
  Stereo Image Pair Sorter

 
 move stereo "cha-cha" pairs, and single images, from one folder into separate folders
 
 
`pairs3d` is a basic python GUI tool that automatically identifies and separates stereo image pairs from folders containing both stereo pairs and single images. It uses perceptual hashing and timestamp proximity to detect stereo pairs and organizes them into separate pair/single folders for easy management.
  
 [created by chatgpt vibe-code]
 
 
 **Features**
 
Detects stereo image pairs based on:
- Timestamp proximity (within 2 seconds)
- Perceptual similarity (using pHash)
- Moves identified pairs to a pairs/ folder
- Moves remaining images to a singles/ folder
- Simple GUI for folder selection
- can process subfolders [by checkbox]
- Time-diff and Hash values can be adjusted [for reprocessing 'singles']
- uses settings.txt file to remember most recent folder chosen

**author note**

 usage *may* miss some pairs, so manual perusal of the 'singles' folder is still recommended, but it *should* place only pairs into the 'pairs' folder for subsequent processing [ie, with StereoPhotoMaker or similar] if Hash value is not set high.

License

- This project is licensed under the MIT License. See the LICENSE file for details.


## 🖼️ Assets

Icon set provided in `imgs/` for packaging:

| Format | Use |
|--------|-----|
| `pairs3d.ico` | Windows `.exe` builds |
| `pairs3d.png` | Linux `.desktop` shortcut |
| `pairs3d.icns` | macOS `.app` icon |
| `pairs3d.svg` | Optional vector-style reference |
