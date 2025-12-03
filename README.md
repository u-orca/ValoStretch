# ValoStretch

[![Python](https://img.shields.io/badge/python-3.9+-blue)](https://www.python.org/)

**ValoStretch** is a simple tool I built with **PySide6** that allows users to set **true stretched** resolutions in VALORANT by editing their `GameUserSettings.ini` files safely.

> ⚠️ **Disclaimer:** This tool modifies game configuration files. Use it at your own risk.

---

 ## 🚀 Features
- Automatically detects all `GameUserSettings.ini` files in VALORANT’s config folders.  
- Lets the user enter a **custom width and height**.  
- Updates resolution-related fields in all INI files while preserving user-specific settings (monitor IDs, GUIDs, etc.).
- - **Creates a backup** of the original `GameUserSettings.ini` files before applying changes, so users can revert if needed.  
- **Prebuilt executable available** in the [Releases](https://github.com/u-orca/ValoStretch/releases) section for Windows.
  
---

## 🛠️ If you want to run it with Python instead

1. Install Python 3.9+  
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the Python script:
```bash
py main.py
```

## 🎮 How to Use

1. **Launch ValoStretch**.  
2. Enter your preferred **Width** and **Height** in the text fields.  
3. Click the **Set Resolution** button.  
4. The app will automatically search all `GameUserSettings.ini` files in VALORANT’s config folders.  
5. Resolution-related fields in all INI files will be updated.  
6. **Before launching VALORANT**, change your **Windows display settings** resolution to match the one you set in ValoStretch.  
   - For non‑native aspect ratios, make sure your display scaling or GPU scaling is set to “Stretched / Full‑screen” so the game output fills the entire monitor and has no black bars.
7. A popup will confirm **success** or report if no INI files were found.
   
> **Troubleshooting Tip:** If the resolution changes do not apply correctly, try the following:  
> 1. Launch VALORANT first and set the **Fullscreen Mode** to **Windowed**, not Borderless Windowed.  
> 2. Close VALORANT completely.  
> 3. Run ValoStretch again and repeat the steps to set your desired resolution.  
> This can help ensure that the changes are correctly applied to the INI files.

> **Tip:** For true stretch to work correctly in-game, make sure your chosen resolution is supported by your monitor and matches your desired aspect ratio. Using unsupported resolutions may not achieve the desired effect.

---

## 🗒️ What ValoStretch Edits in Config

- **ResolutionSizeX/Y** → Sets the main game resolution.  
- **LastUserConfirmedResolutionSizeX/Y** → Confirms the resolution to the game.  
- **DesiredScreenWidth/Height** → Sets the desired screen resolution for rendering.  
- **LastUserConfirmedDesiredScreenWidth/Height** → Confirms desired rendering resolution.  
- **bShouldLetterbox / bLastConfirmedShouldLetterbox** → Ensures no black bars if using stretched resolutions.  
- **bUseDynamicResolution** → Disables automatic dynamic resolution scaling.  
- **WindowPosX/Y** → Resets the window position to default (0,0).  
- **LastConfirmedFullscreenMode / PreferredFullscreenMode** → Ensures proper fullscreen/window mode.

---

## ⚠️ Important Notes

- **Safe Editing Only:** ValoStretch modifies only resolution-related fields. User-specific data such as monitor IDs and device GUIDs remain unchanged.  
- **Display Scaling Matters:**  
  - For non-native aspect ratios, configure display scaling or GPU scaling to **stretched/full-screen** to avoid black bars.  
