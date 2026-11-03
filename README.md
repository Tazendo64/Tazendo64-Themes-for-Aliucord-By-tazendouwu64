# ☂ Tazendo64-Themes-for-Aliucord-By-tazendouwu64

> An advanced cross-platform theme inspired by Parasol Waddle Dee with an animated background, custom sound effects, calligraphic typography, and a high-performance anti-crash system.

[![Supported Platforms](https://shields.io)](https://github.com)
[![Open Issues](https://shields.io)](https://github.com/issues)


---

## ✨Special Features

* **🌊 Fluid Motion Background:** Ultra-lightweight WebP file (`waddledeebackground.webp`) that simulates water movement and Kirby's reflection without overloading your device's RAM.
* **🎵 Integrated Interactive Audio:** Sound effects from the Kirby universe assigned to key actions (sending/receiving messages, calls, and startup sounds).
* **🎨 Curated Color Palette:** A harmonious combination faithfully based on the tones of the original illustration.
* **🛡️ Anti-Crash System:** Styles optimized using hardware acceleration (GPU) and asynchronous audio buffers to prevent freezes on any platform.

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
2. Download the file [`tema-waddledee.json`](./themes/android/tema-waddledee.json) from this repository and move it to the `Aliucord/themes/` folder on your device's storage.
3. Go to Aliucord Settings > Plugins > Themer, activate the theme, and restart the application.
4. Open the CustomSounds settings and add the URLs of the audio files located in the `/assets` folder:
   * **Send message:** `waddle_send.mp3`
   * **Receive message:** `waddle_receive.mp3`
   * **Call start:** `waddle_call_start.mp3`

### 💻 On PC and Linux (Vencord / BetterDiscord)
1. Open your custom Discord client on your computer.
2. Go to the **Custom Themes (Custom CSS)** section in your settings.
3. Copy the code from [`waddledee-pc.theme.css`](./themes/pc-linux/waddledee-pc.theme.css) or directly link to the file and import it.
4. Enjoy the animated background and frosted transparency!

## 📂 Repository Structure

```text
Tazendo64-Themes-for-Aliucord-By-tazendouwu64/
├── .gitattributes # Prevents corruption of audio and fonts
├── assets/ # WebP animation, .ttf font, and audio tracks
│ ├── waddle_font.ttf
│ ├── waddledeebackground.webp
│ ├── waddle_send.mp3
│ ├── waddle_receive.mp3
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

_Created with 🧡 by [Tazendo64](https://github.com). If you have optimization ideas for the anti-crash system, feel free to open an Issue or Pull Request!_
 
## 🔌 Recommended Community Plugins

To experience the full potential of this theme suite, we highly recommend installing the following plugins from the official Aliucord server:

* **Themer:** Required to inject and parse your custom `tema-waddledee.json` color mapping.
* **CustomSounds:** Essential for binding your `.mp3` assets to system alerts (messages, calls, startup).
* **FontAndFont:** Used to apply the custom calligraphic typography `waddle_font.ttf` across the entire application interface.
* **BiggerUserPopouts:** Enhances the frosted glass effect preview on user profiles and cards.
