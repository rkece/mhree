# 🌌 The Living Birthday Universe (Oryzo.ai Edition)

An immersive, highly animated 3D birthday experience inspired by **ORYZO.AI** (cosmic luxury aesthetic, liquid glowing gradients, 3D spring physics) and **FOLLOW.ART** (kinetic auto-advancing imagery).

Built entirely as **one single standalone vanilla file (`index.html`)** with **zero build dependencies required**.

---

## 🎨 Unified Design System & Typography

- **Single Universal Font**: **Plus Jakarta Sans** across all headings, body text, buttons, and captions for a razor-sharp, cohesive, modern aesthetic.
- **Atmosphere**: Deep cosmic obsidian (`#07050C`) and midnight amethyst (`#0E0919`) illuminated with glowing champagne gold (`#F3D293`), starlight rose, and liquid glass borders.
- **No Cluttered Navbar**: Full-bleed immersion with minimal floating corner controls.
- **Cursor Starlight Aura**: An interactive stardust halo gently follows your pointer.

---

## ✨ Signature Features & Interactive Mechanics

1. **2-Second Kinetic Auto-Parallax Carousel (Chapter I)**:
   - Images automatically advance every 2 seconds with smooth cubic-bezier spring physics.
   - 3D perspective tilt reacting to cursor coordinates (`perspective(800px) rotateY(...) rotateX(...)`).
   - Drag / touch-swipe gesture support, progress dot indicators, and click to inspect full memory stories in a modal lightbox.
   - Automatically pauses on hover so the user can comfortably view any image.

2. **Signature 3D Memory Planet (Chapter II)**:
   - A celestial solar system where your friend is the central glowing star.
   - Memory photographs revolve in concentric 3D rings (`preserve-3d`, `translate3d`).
   - **Click & drag to rotate** the 3D orbital plane along both X and Y axes.

3. **Signature Quantum Time-Rewind Machine (Chapter III)**:
   - A 3D dimensional hourglass with flowing golden quantum sand particles.
   - Clicking `"⏳ Rewind Time"` flips the hourglass in 3D (`rotateY(180deg) rotateZ(180deg)`), reverses the gravity flow of glowing sand particles, and triggers a time-warp rewind revealing the "Day 01" origin memory.

4. **Signature 3D Holographic Music Box (Chapter IV)**:
   - A 3D mechanical music box sitting on the canvas.
   - Clicking releases the latch, hinges open the lid in 3D (`rotateX(-120deg)`), raises a blooming crystal flower, and awakens the synthesized music box melody.

5. **Signature Tear-Through-The-Screen Reveal (Chapter V)**:
   - A gold-woven paper veil blocks a secret birthday sanctuary with `"There's something hidden underneath... [Drag to Tear]"`.
   - Dragging your mouse or finger tears through paper fibers with ragged edges and floating confetti shreds to uncover the hidden blessing underneath (includes an accessible "Reveal All" option).

6. **Signature Scratch-to-Reveal Gold Foil Cards (Chapter VI)**:
   - Metallic gold foil scratchcards rendered with HTML5 Canvas.
   - Drag to scratch away the metallic gold foil and reveal hidden personal messages with a live status badge.

7. **Interactive Birthday Cake & Blowable Candle (Chapter VII)**:
   - 3D cake tier with a flickering candle flame.
   - Click the candle or click `"Blow Out Candle 🎂"` to extinguish the flame with a wind whoosh, watch animated smoke curl into the sky, and trigger a golden confetti shower.

8. **Living Flower Garden (Active Everywhere on Background)**:
   - Click or tap anywhere in empty areas across the website to plant procedural botanical flowers.
   - A seed drops, a stem sways with the wind, leaves emerge, petals bloom, and glowing pollen particles burst into the air.

9. **Web Audio API Celestial Music Box**:
   - Synthesizes warm bell chimes, candle-blow whoosh, and star chimes—no external audio files required.
   - Subtle corner floating widget with animated equalizer bars.

10. **Live In-App Personalizer (Floating Action Button)**:
    - Click the floating **"✏️ Personalize"** button anytime to update your friend's name, your name, headline, or upload custom friend portraits with instant preview and `localStorage` persistence.

---

## 🚀 How to Run

Because everything is contained in `index.html`, you can:
- Double-click `index.html` to open it in any modern browser (Chrome, Edge, Safari, Firefox).
- Or run a local HTTP server:
  ```bash
  python -m http.server 5173
  ```
  And visit: **http://localhost:5173**
