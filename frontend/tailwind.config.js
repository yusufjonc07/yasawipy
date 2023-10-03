/** @type {import('tailwindcss').Config} */

import colors from "tailwindcss/colors"


export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        danger: colors.rose,
        primary: colors.blue,
        secondary: colors.gray,
        success: colors.green,
        warning: colors.yellow,
      },
    },
  },
  darkMode: 'class',
  plugins: [
    'flowbite/plugin'
  ],
}