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
    fontSize: {
      'xs': '.75rem',
      'sm': '.875rem',
      'base': '1rem',
      'lg': '1.125rem',
      'xl': '1.25rem',
      '2xl': '1.5rem',
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
      },
      colors: {
        green: '#2E7D32',
        green_light: '#4CAF50',
        green_bg: '#E8F5E9',
        grey: '#424242',
        grey_light: '#F5F5F5',
        grey_border: '#E0E0E0',
      },
    },
  },
  plugins: [],
}

