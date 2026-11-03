# ☂ Tazendo64-Themes-for-Aliucord-By-tazendouwu64

> A cross-platform theme inspired by Parasol Waddle Dee, with a custom background, sound effects, and calligraphic typography.

---

## ✨Special Features

* **🌊 Custom Backgrounds:** A lightweight static preview background and an optional animated WebP for the themes.
* **🎵 Interactive Audio:** Sound effects for sending messages, calls, and ringtone previews.
* **🎨 Curated Color Palette:** A harmonious combination faithfully based on the tones of the original illustration.
* **♿ Accessible Preview:** Keyboard-operable color swatches, visible focus states, and support for reduced-motion preferences.

The animated background is about 21 MB. The website preview loads a smaller static image first and only loads the animation when you enable it.

## 🧰 Build and ZIP package

Run `python3 build.py` to validate the Android theme JSON and local web assets, then create:

* `build/site/` — the ready-to-publish website.
* `build/waddledee-theme-suite.zip` — the website, themes, assets, license, and README.

Download the package directly: [waddledee-theme-suite.zip](https://github.com/Tazendo64/Tazendo64-Themes-for-Aliucord-By-tazendouwu64/releases/download/v1.2.0/waddledee-theme-suite.zip).

## 🎨 Official Color Palette

| Item | HEXCode | Representative Color |
| :--- | :---: | :--- |
| **Main Background** | `#2e432c` | Dark Lotus Leaf Green |
| **Panels & Interface** | `#1d2b1c` | Frosted Translucent Green |
| **Accent Color** | `#ff7a45` | Waddle Dee Warm Orange |
| **Interface Text** | `#fffef0` | Umbrella Cream |
| **Secondary Text** | `#9bb88d` | Soft Moss Green |

## 🚀 Installation Guide

### 📱 On Aliucord (Android)
1. Install the **Themer** plugin and the **CustomSounds** plugin from the official Aliucord server.
2. Download the file [`theme-waddledee.json`](./themes/android/theme-waddledee.json) from this repository and move it to the `Aliucord/themes/` folder on your device's storage.
3. Go to Aliucord Settings > Plugins > Themer, activate the theme, and restart the application.
4. Open the CustomSounds settings and add the URLs of the audio files located in the `/assets` folder:
   * **Send message:** `waddle_send.wav`
   * **Receive message:** `waddle_receive.mp3`
   * **Call start:** `waddle_call_start.mp3`

## 📑 Note: also you can use the plugin Themes if you want.

### 💻 On PC and Linux (Vencord / BetterDiscord)
1. Open your custom Discord client on your computer.
2. Go to the **Custom Themes (Custom CSS)** section in your settings.
3. Import [`waddledee-pc.theme.css`](./themes/pc-linux/waddledee-pc.theme.css) as a theme file. Do not paste its contents into a standalone CSS editor: its font and background use relative paths to the repository's `assets/` folder. If installing it locally, keep the file at `themes/pc-linux/waddledee-pc.theme.css` and preserve the `assets/` folder at the repository root.
4. Enjoy the animated background and frosted transparency!

## 📂 Repository Structure

```text
Tazendo64-Themes-for-Aliucord-By-tazendouwu64/
├── .gitattributes # Prevents corruption of audio and fonts
├── assets/ # WebP background, .ttf font, and audio tracks
│ ├── 167568d5ab41d1eca3daa416c9e7df6d.jpg
│ ├── waddle_background.png
│ ├── waddle_font.ttf
│ ├── waddledeebackground.webp
│ ├── waddle_send.wav
│ ├── waddle_receive.mp3
│ ├── waddle_ringtone.mp3
│ ├── waddle_call_start.mp3
│ └── waddle_ringtone.mp3
├── index.html # Preview webpage with interactive sound
├── LICENSE # GPL-3.0 license for your project
├── README.md # Your cover page (This file)
└── themes/ # Folder containing the themes
    ├── android/
    │ └── theme-waddledee.json
    └── pc-linux/
        └── waddledee-pc.theme.css
```

---

_Created with 🧡 by [Tazendo64](https://github.com/Tazendo64). For suggestions, [open an issue](https://github.com/Tazendo64/Tazendo64-Themes-for-Aliucord-By-tazendouwu64/issues)._
 
## 🔌 Recommended Community Plugins

To experience the full potential of this theme suite, we highly recommend installing the following plugins from the official Aliucord server:

* **Themer:** Required to inject and parse your custom `theme-waddledee.json` color mapping.
* **CustomSounds:** Essential for binding your audio assets to system alerts (messages, calls, startup).
* **FontAndFont:** Used to apply the custom calligraphic typography `waddle_font.ttf` across the entire application interface.
* **BiggerUserPopouts:** Enhances the frosted glass effect preview on user profiles and cards.
