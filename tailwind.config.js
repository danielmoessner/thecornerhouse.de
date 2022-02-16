const colors = require('tailwindcss/colors')

module.exports = {
  content: ['./templates/**/*.html'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Montserrat', 'sans-serif']
      },
      colors: {
        gold: '#bd8951',
        gray: colors.stone
      }
    },
  },
  plugins: [
//    require('@tailwindcss/forms'),
  ],
}
