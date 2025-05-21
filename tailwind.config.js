/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#A0AECF', // Pastel Blue-ish
        'primary-light': '#D6E2F6', // Lighter primary
        secondary: '#BAD6FB', // Soft Pastel Blue
        accent: '#D8BFD8',   // Pastel Purple
        neutral: '#E5E7EB', // Light Gray (Tailwind gray-200)
        background: '#F9FAFB', // Very Light Gray (Tailwind gray-50)
        surface: '#FFFFFF',    // White
        text: '#374151',      // Dark Gray (Tailwind gray-700)
        'text-light': '#6B7280', // Medium Gray (Tailwind gray-500)
        'pastel-blue': '#BFDBFE',
        'pastel-grey': '#D1D5DB',
        'pastel-purple': '#DDD6FE',
      },
      borderRadius: {
        '2xl': '1rem', // 16px
      },
      boxShadow: {
        'primary-soft': '0 4px 14px 0 rgba(160, 174, 207, 0.5)',
        'neutral-soft': '0 4px 12px 0 rgba(229, 231, 235, 0.6)',
      },
      fontFamily: {
        sans: ['ui-sans-serif', 'system-ui', '-apple-system', 'BlinkMacSystemFont', '"Segoe UI"', 'Roboto', '"Helvetica Neue"', 'Arial', '"Noto Sans"', 'sans-serif', '"Apple Color Emoji"', '"Segoe UI Emoji"', '"Segoe UI Symbol"', '"Noto Color Emoji"'],
      },
    },
  },
  plugins: [],
}
