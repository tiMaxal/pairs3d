<p align="center">
  <img src="imgs/logo3d_983940088pizapw1553754827_square_grey.png" width="200" alt="pairs3d logo">
</p>
  __pairs3d__
Stereo Image Pair Sorter
 [created by chatgpt vibe-code]
 separate stereo "cha-cha" pairs, and single images, from one folder
 
`pairs3d` is a basic python GUI tool that automatically identifies and separates stereo image pairs from folders containing both stereo pairs and single images. It uses perceptual hashing and timestamp proximity to detect stereo pairs and organizes them into separate pair/single folders for easy management.

 __Features__
Detects stereo image pairs based on:
- Timestamp proximity (within 2 seconds)
- Perceptual similarity (using pHash)
- Moves identified pairs to a pairs/ folder
- Moves remaining images to a singles/ folder
- Simple GUI for folder selection

__author note__
 usage *may* miss some pairs, so manual perusal of the 'singles' folder is still recommended, but it *should* place only pairs into the 'pairs' folder for subsequent processing [ie, with StereoPhotoMaker or similar]

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
