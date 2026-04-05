# 🎮 Cellular Automata Explorer

Interactive playground for learning Cellular Automata (CA) - part of **GameWorld** mini-game collection.

## Features

### Interactive Web Version
- **Elementary CA** (1D) - Rule 0-255
- **Conway's Game of Life** (2D)
- Click to draw cells
- Presets: Glider, Blinker, LWSS, Gosper Glider Gun, Acorn, Diamond
- Adjustable speed
- Download Python code to learn locally

### Learning Resources
- **Elementary CA**: 1D grid, each cell checks neighbors (left, self, right) using rule number
- **Game of Life**: 2D grid, B3/S23 rules - born with 3, survive with 2-3 neighbors
- **Famous Rules**:
  - Rule 30: Chaos, used for random number generation
  - Rule 110: Turing complete!
  - Rule 184: Models traffic flow

## Files

```
cellular-automata/
├── index.html    ← Interactive web version (just open in browser!)
└── README.md
```

## Quick Start

1. Open `index.html` in any modern browser
2. Click cells to draw patterns
3. Press ▶ Start to run the simulation
4. Try presets or experiment with rules!

## For Learning

Download the Python code directly from the web app to:
- See the actual algorithms
- Modify parameters
- Run locally with Matplotlib
- Learn by experimentation

## Related

- Inspired by Stephen Wolfram's "A New Kind of Science"
- Related to: Physics, Computer Science, Emergence, Complex Systems
- Try Golly (external) for more advanced Life simulations
