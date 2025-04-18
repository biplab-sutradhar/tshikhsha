import { defineConfig } from "vitest/config";
import react from "@vitejs/plugin-react-swc";

export default defineConfig({
  plugins: [react()],
  test: {
    globals: true,
    coverage: {
      reporter: ["text", "html"],
      include: ["src/**/*.{jsx,js}"],
      exclude: ["src/App.jsx", "src/main.jsx"],
    },
    setupFiles: "./setupTest.js",
  },
});
