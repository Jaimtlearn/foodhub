/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./foodhub/templates/*"],
  theme: {
    extend: {
      backgroundImage: {
        'gradient-pattern' : "url('/static/images/others/gradient.webp')",
        'gradient': "url('/static/images/others/blue-gradient.webp')"
      }
    },
  },
  plugins: [],
}

