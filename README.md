# ☂ Waddle Dee Advanced Pond

> A polished theme inspired by Parasol Waddle Dee, designed for Aliucord and desktop clients with a frosted glass interface, animated background, custom typography, and matching sound effects.

[![Supported Platforms](https://img.shields.io/badge/platforms-Android%20%7C%20Desktop-2e432c)](https://github.com/Tazendo64/Tazendo64-Themes-for-Aliucord-By-tazendouwu64)
[![Open Issues](https://img.shields.io/github/issues/Tazendo64/Tazendo64-Themes-for-Aliucord-By-tazendouwu64)](https://github.com/Tazendo64/Tazendo64-Themes-for-Aliucord-By-tazendouwu64/issues)

---

## ✨ Highlights

* **🌊 Animated background:** Uses the bundled WebP art asset (`waddledeebackground.webp`) for a soft, layered parallax-style backdrop.
* **🎵 Built-in sound pack:** Includes custom MP3s for message send/receive, call start, and ringtone events.
* **🎨 curated palette:** Matches the warm green, cream, and orange tones of the original Waddle Dee visual style.
* **✒️ custom typography:** Adds the included `waddle_font.ttf` for a handcrafted, playful aesthetic.
* **🪟 frosted glass:** Designed to preserve readability while keeping the interface airy and polished.

## 🎨 Official Color Palette

| Item | HEX | Representative Color |
| :--- | :---: | :--- |
| **Main Background** | `#2e432c` | Dark Lotus Leaf Green |
| **Panels & Interface** | `#1d2b1c` | Frosted Translucent Green |
| **Accent Color** | `#ff7a45` | Waddle Dee Warm Orange |
| **Interface Text** | `#fffef0` | Umbrella Cream |
| **Secondary Text** | `#9bb88d` | Soft Moss Green |

## 🚀 Installation Guide

### 📱 On Aliucord (Android)
1. Install the **Themer** plugin and the **CustomSounds** plugin from the official Aliucord server.
2. Download [`theme-waddledee.json`](./themes/android/theme-waddledee.json) and place it under `Aliucord/themes/` on your device.
3. Open Aliucord Settings > Plugins > Themer, activate the theme, and restart the app.
4. In **CustomSounds**, assign the audio files from [`assets/`](./assets/):
   * **Send message:** [`waddle_send.mp3`](./assets/waddle_send.mp3)
   * **Receive message:** [`waddle_receive.mp3`](./assets/waddle_receive.mp3)
   * **Call start:** [`waddle_call_start.mp3`](./assets/waddle_call_start.mp3)
   * **Ringtone:** [`waddle_ringtone.mp3`](./assets/waddle_ringtone.mp3)

### 💻 On PC and Linux (Vencord / BetterDiscord)
1. Open your custom Discord client.
2. Go to **Custom Themes** or **Custom CSS**.
3. Copy the content from [`waddledee-pc.theme.css`](./themes/pc-linux/waddledee-pc.theme.css) or import it directly.
4. Enjoy the animated background and frosted glass aesthetic.

## 📂 Repository Structure

```text
Tazendo64-Themes-for-Aliucord-By-tazendouwu64/
├── .gitattributes # Prevents corruption of audio and fonts
├── assets/ # Background art, typography, and sound effects
│ ├── waddle_background.png   # Legacy static fallback for previews
│ ├── waddle_font.ttf
│ ├── waddledeebackground.webp # Active animated background asset
│ ├── waddle_send.mp3
│ ├── waddle_receive.mp3
│ ├── waddle_call_start.mp3
│ └── waddle_ringtone.mp3
├── index.html # Live preview page with color and sound interactions
├── LICENSE # GPL-3.0 license
├── README.md # Project documentation
└── themes/ # Theme variants
    ├── android/
    │ └── theme-waddledee.json
    └── pc-linux/
        └── waddledee-pc.theme.css
```

---

_Created with 🧡 by [Tazendo64](https://github.com/Tazendo64). Report problems in the [issue tracker](https://github.com/Tazendo64/Tazendo64-Themes-for-Aliucord-By-tazendouwu64/issues)._

## 🔌 Recommended Community Plugins

For the full experience, these plugins are recommended on Aliucord:

* **Themer:** Required to load and apply the `theme-waddledee.json` colors.
* **CustomSounds:** Essential for binding the `.mp3` files to message and call events.
* **FontAndFont:** Lets you apply `waddle_font.ttf` throughout the app UI.
* **BiggerUserPopouts:** Improves the glassmorphism effect in profile popouts and cards.

## 🌐 Live Preview

Open the [Waddle Dee preview page](https://tazendo64.github.io/Tazendo64-Themes-for-Aliucord-By-tazendouwu64/).
