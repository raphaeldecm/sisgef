/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./sisgef/**/*.{html,js}"],
  theme: {
    screens: {
      'mini': '50px',
      'sm': '640px',
      'md': '768px',
      'lg': '1024px',
      'lc': '1222px',
      'xl': '1280px',
      '2xl': '1536px',
    },
    fontFamily: {
      sans: ['Poppins', 'sans-serif'],
    },
    extend: {
      animation: {
        fade: 'fadeOut 5s ease-in-out',
      },
      keyframes: theme => ({
        fadeOut: {
          '0%': { opacity: '1' },
          '90%': {opacity: '0.1'},
          '100%': { opacity: '0'},
        },
      }),
      fontFamily: {
        poppins: ["Poppins", "sans-serif"]
      }
    },
  },
  plugins: [],
}

