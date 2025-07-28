/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    ".templates/**/*.html", //templates projects level
    "./**/templates/**/*.html", //templates inside app
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
