to do:
- [done] `start` button
- [done] progress bar
- [done] show no. of files being processed
- [done] `pause` button
- [done] also cause 'pause' to pause timer
- [done] `exit` button
- [done] process subfolders
- [done] allow setting values for TIME_DIFF_THRESHOLD + HASH_DIFF_THRESHOLD
- action 'alt' for keyboard control
- [show folder contents in 'chooser', ie whether images exist there]
- [done] move progress bar between timer\filecount lines
   [instead of showing info at ends of bar]
- Cross-platform support: Windows and Linux [+ mac?]
- cli functionality 


Package as:
- Windows .exe (standalone)
- Debian .deb package
build exe: 
C:\Users\timax\AppData\Roaming\Python\Python313\Scripts\pyinstaller --onefile --windowed --hidden-import=PIL --hidden-import=imagehash --version-file=version.txt pairs3d.v1-3.py --name pairs3d

[
    update readme
 - "`pairs3d` is a cross-platform GUI tool .. "
 ]
 __Installation__
Windows:
- Download the latest pairs3d.exe from the Releases section.
- Run the executable. No installation required.

Linux (Debian/Ubuntu):
- Download the latest pairs3d.deb from the Releases section.
- Install the package:
`bash`
`Copy`
`Edit`
`sudo dpkg -i pairs3d.deb`
  Launch pairs3d from your applications menu or by running pairs3d in the terminal.

 __Usage__
- Launch pairs3d.
- Click on the "Browse" button to select the folder containing your images.
- The tool will process the images and display the number of pairs and singles found.
- Check the pairs/ and singles/ folders created inside your selected directory.

[Screenshots]

  *Main interface of pairs3d*

  *Results after processing images.*



- pipe folder of pairs to `StereoPhotoMaker` for processing to stereogram images
   [anaglyph \ sbs \ uni]



__✅ Usage Instructions (when icons are in imgs/ folder)__


*🔧 PyInstaller .exe (Windows)*
- Makefile entry:

make
exe:
	pyinstaller --onefile --windowed --icon=imgs/pairs3d.ico pairs3d.py

*🐧 .desktop launcher (Linux)*
- Create pairs3d.desktop and reference the PNG:

ini:
[Desktop Entry]
Type=Application
Name=pairs3d
Exec=pairs3d
Icon=imgs/pairs3d.png
Terminal=false
Categories=Graphics;

- Then install with -
bash:
cp pairs3d.desktop ~/.local/share/applications/

*🍎 macOS app bundling (Py2app or manual)*
- Use the .icns icon -
bash:
--iconfile imgs/pairs3d.icns
