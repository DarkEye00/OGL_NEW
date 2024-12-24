/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./static/**/*.js"],
  theme: {
    extend: {
      keyframes: {
        "open-menu": {
          "0%": { transform: "scaleY(0)" },
          "80%": { transform: "scaleY(1.2)" },
          "100%": { transform: "scaleY(1)" },
        },
        "zoom-in":{
          "0%": {
            transform: "scale(1)"/* Start at original size */
          },
          "100%": {
            transform: "scale(1.2)" /* Zoom in 20% */
          }
        }
      },
      animation: {
        "open-menu": "open-menu 1s ease-in-out forwards",
        "zoom-in": "zoom-in 10s ease-in-out ",
      },
    },
  },
  plugins: [],
};
