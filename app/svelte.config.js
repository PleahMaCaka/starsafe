// noinspection JSUnusedGlobalSymbols

import adapter from "@sveltejs/adapter-static"
import { vitePreprocess } from "@sveltejs/kit/vite"

/** @type {{preprocess: *, kit: {adapter: Adapter}}} */
const config = {
    preprocess: vitePreprocess(),
    kit: {
        adapter: adapter()
    }
}

export default config
