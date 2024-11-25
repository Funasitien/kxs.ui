/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  theme: {
    fontFamily: {
      sans: ["Poppins", "sans-serif"],
      serif: ["JetBrains Mono", "serif"],
    },
    extend: {},
  },
  plugins: [require("@tailwindcss/typography"), require("daisyui")],
  daisyui: {
    themes: ["light", "sunset", {
      kxs: {
        "primary": "#00b1ff",
        "secondary": "#bb5600",
        "accent": "#fa0000",
        "neutral": "#23232e",
        "base-100": "#322526",
        "info": "#0056ff",
        "success": "#00b690",
        "warning": "#e30f00",
        "error": "#ff0033",
        "font-family": "'Roboto Slab', 'Georgia', Arial, sans-serif",
      },
    },], // false: only light + dark | true: all themes | array: specific themes like this ["light", "dark", "cupcake"]
    darkTheme: "dark", // name of one of the included themes for dark mode
    base: true, // applies background color and foreground color for root element by default
    styled: true, // include daisyUI colors and design decisions for all components
    utils: true, // adds responsive and modifier utility classes
    prefix: "", // prefix for daisyUI classnames (components, modifiers and responsive class names. Not colors)
    logs: true, // Shows info about daisyUI version and used config in the console when building your CSS
    themeRoot: ":root", // The element that receives theme color CSS variables
  },
};
