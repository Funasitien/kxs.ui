import { defineConfig } from 'astro/config';
import tailwind from "@astrojs/tailwind";

import icon from "astro-icon";

import mdx from "@astrojs/mdx";

// https://astro.build/config
export default defineConfig({
  markdown: {
    extendMarkdownConfig: (config) => {
      config.linkify = true;
      return config;
    }
  },
  public: {
    input: './public',
    output: './dist/public'
  },
  integrations: [tailwind(), icon(), mdx()]
});