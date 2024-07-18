# codellama-70b

> You are an expert developer experienced in TypeScript, Next.js, and Tailwind CSS. I need you to create a random spinning wheel web page

Here is an example of how you can use Next.js, Tailwind CSS, and TypeScript to create a simple 
webpage with a randomly spinning wheel.

**File structure:**
```
my-app/
├── pages/
│   ├── index.tsx
├── public/
│   └── wheel.png (image of the spinning wheel)
└── styles/
    ├── global.css
```
**index.tsx (`pages` folder):**
```TSX
import React, { useState } from "react";
import Head from 'next/head'

// Define your colors and their corresponding weights (probabilities) here:
const COLORS = [
  { name: "red", weight: 10 },
  { name: "green", weight: 20 },
  { name: "blue", weight: 30 },
];

export default function Home() {
  const [spinning, setSpinning] = useState(false);
  const [resultColor, setResultColor] = useState("");

  const spinWheel = () => {
    // Reset the result color and start spinning:
    setResultColor("");
    setSpinning(true);

    // Calculate the probability of each color based on their weight:
    let probabilities = COLORS.map((color) => color.weight / 100).reduce((a, b) => a + b);

    // Generate a random number between 0 and 1 (probability):
    const randomNumber = Math.random();

    // Calculate the position of the wheel based on the probability:
    let currentPosition = 0;
    COLORS.forEach((color) => {
      if (randomNumber >= currentPosition && randomNumber <= color.weight + currentPosition) {
        setResultColor(color.name);
      }
      currentPosition += color.weight;
    });

    // Stop spinning after 4 seconds:
    setTimeout(() => setSpinning(false), 4000);
  };

  return (
    <div className="container">
      <Head>
        <title>Random Spinning Wheel</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      
      <main>
        {/* Your spinning wheel goes here */}
        
        {resultColor && (
          // Display the result color if it's not empty:
          <p className="text-center text-2xl font-semibold mt-8">
            The result is: {resultColor.toUpperCase()}
          </p>
        )}
        
        <button onClick={spinWheel}>Spin!</button>
      </main>
    </div>
  );
}
```
**global.css (`styles` folder):**
```CSS
@tailwind base;
@tailwind components;
@tailwind utilities;
```
This is a simple example, but it should get you started with creating your own spinning wheel webpage 
using Next.js, Tailwind CSS, and TypeScript. You can customize the colors, weights, and probabilities 
according to your needs.