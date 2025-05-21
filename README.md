# NovaFlow Interface

This repository contains HTML mock-ups and an optional React starter application for the NovaFlow product, a platform designed to streamline creative collaboration for design teams and solo creators.

## HTML Mock-ups

These are standalone HTML files that use Tailwind CSS via a CDN link for styling. They provide a quick way to view the visual design of the Landing Page and Project Dashboard.

**Instructions:**

1.  Download or clone the directory containing the HTML files (e.g., if they are in the root, or in a specific `html-mockups/` directory).
2.  Open `index.html` (for Landing Page) or `dashboard.html` (for Project Dashboard) directly in your web browser.

The `tailwind.config.js` content is included as a comment within each HTML file for reference. If you wish to set up a local Tailwind CSS build process for these mock-ups:
    *   Save the configuration from the comments into a `tailwind.config.js` file in the same directory as the HTML files.
    *   Ensure you have Node.js and npm/yarn installed.
    *   Install Tailwind CSS: `npm install -D tailwindcss`
    *   Create a basic `input.css` file with `@tailwind base; @tailwind components; @tailwind utilities;`
    *   Run the Tailwind CLI to process your CSS: `npx tailwindcss -i ./input.css -o ./output.css --watch`
    *   Link to `./output.css` in your HTML files instead of the CDN.

## React Starter (Vite + Tailwind CSS)

This is an optional, more interactive starter project built with React (using Vite) and Tailwind CSS, demonstrating the NovaFlow components.

**Instructions:**

1.  **Initial Setup (if not already done):**
    *   Ensure you have Node.js and npm (Node Package Manager) or yarn installed on your system.
    *   Create a new Vite React project (replace `novaflow-react` with your preferred project name if desired):
        ```bash
        # Using npm
        npm create vite@latest novaflow-react -- --template react
        ```
        ```bash
        # OR using yarn
        yarn create vite novaflow-react --template react
        ```
    *   Navigate into your newly created project directory:
        ```bash
        cd novaflow-react
        ```
    *   Install Tailwind CSS, PostCSS, and Autoprefixer, then generate Tailwind and PostCSS configuration files:
        ```bash
        # Using npm
        npm install -D tailwindcss postcss autoprefixer
        npx tailwindcss init -p
        ```
        ```bash
        # OR using yarn
        yarn add -D tailwindcss postcss autoprefixer
        yarn tailwindcss init -p
        ```

2.  **Configure Project:**
    *   Replace the contents of the generated `tailwind.config.js`, `postcss.config.js`, `src/index.css`, `src/main.jsx`, `src/App.jsx`, and `index.html` files with the corresponding files provided in this repository (e.g., from a `react-starter/` directory if you've organized them that way, or from the root if they are there).
    *   Create the following directory structure and add the provided component files:
        *   `src/components/Button/Button.jsx`
        *   `src/components/Card/Card.jsx`
        *   `src/components/Navbar/Navbar.jsx`
    *   If you copied the `package.json` from this repository into your `novaflow-react` directory, it already includes the necessary dependencies.

3.  **Install Dependencies & Run:**
    *   **Command 1: Install project dependencies** (if you haven't already or if you replaced `package.json`):
        ```bash
        # Using npm
        npm install
        ```
        ```bash
        # OR using yarn
        yarn install
        ```
    *   **Command 2: Start the development server:**
        ```bash
        # Using npm
        npm run dev
        ```
        ```bash
        # OR using yarn
        yarn dev
        ```
    *   **Command 3: View in browser:**
        Open your web browser and navigate to the local development server URL displayed in your terminal (this is usually `http://localhost:5173` or a similar port).

## Design System

The core visual guidelines, including color palette, typography scale, and spacing tokens, are detailed in the `design_system.md` file. These principles are applied in both the HTML mock-ups and the React starter.
