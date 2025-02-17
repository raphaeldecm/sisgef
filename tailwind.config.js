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
        primary: '#1E40AF', // Azul profundo, extraído do logo
        secondary: '#10B981', // Verde vibrante
        accent: '#34D399', // Um verde claro para detalhes e botões
        dark: '#1F2937', // Cinza escuro para contrastar
        light: '#E5E7EB', // Cinza claro para fundos
      },
    },
  },
  plugins: [],
}

