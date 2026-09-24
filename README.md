# DENTARA

DENTARA is a polished visual prototype for a fictional premium dental clinic. It combines editorial art direction, calm medical precision, and a deliberate motion system into a standalone browser experience.

## What it demonstrates

- Premium clinic landing-page design with responsive desktop and mobile layouts
- Cinematic hero treatment and scroll-based section reveals
- Interactive service selector with directional transitions
- Before/after comparison slider with eased pointer response
- Doctor selection with focus states and animated profile modal
- Smile simulator modes
- Animated FAQ accordion with realistic demo answers
- Multi-step booking flow with directional transitions and confirmation toast
- Responsive mobile navigation and touch-friendly interactions
- Accessibility-minded controls and `prefers-reduced-motion` support

## Motion system

Motion is used to communicate hierarchy and continuity rather than as decoration. The prototype uses transform/opacity-first transitions, directional state changes, staggered reveals, tactile button feedback, eased slider movement, animated modal entrances, and unfolding FAQ answers. Reduced-motion users receive simplified transitions and static reveal states.

## Technology

DENTARA is intentionally framework-free. It uses browser-native HTML, CSS, and vanilla JavaScript only—no npm, React, Next.js, build system, or server.

## Run locally

Open `index.html` directly in any modern browser. The project is designed to work from a `file://` URL.

## Project structure

```text
index.html   Semantic page structure and content
styles.css   Design system, responsive layout, and motion styling
script.js    Interactive behavior, state changes, and scroll reveals
README.md    Project documentation
```

All people, patients, statistics, addresses, testimonials, and treatment content are fictional or illustrative demo content. DENTARA is not a real clinic and the experience is not medical advice.

## Built with

- HTML
- CSS
- Vanilla JavaScript
