/**
 * Playwright Multi-Viewport Screenshot Capture & Visual QA Script
 * Captures full-page screenshots at standard Desktop, Tablet, and Mobile breakpoints.
 * 
 * Usage:
 *   node tests/visual-qa/capture-screenshots.js --url http://127.0.0.1:8000/classes --output tests/visual-qa/screenshots/classes
 *   node tests/visual-qa/capture-screenshots.js --file resources/views/... --output tests/visual-qa/screenshots/...
 */

import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Standard Viewports
const VIEWPORTS = [
    { name: 'desktop-1440', width: 1440, height: 900, isMobile: false, hasTouch: false },
    { name: 'tablet-768', width: 768, height: 1024, isMobile: true, hasTouch: true },
    { name: 'mobile-375', width: 375, height: 667, isMobile: true, hasTouch: true },
];

function parseArgs() {
    const args = process.argv.slice(2);
    const parsed = {
        url: '',
        file: '',
        output: path.join(__dirname, 'screenshots'),
        delay: 500,
        fullPage: true,
    };

    for (const arg of args) {
        if (arg.startsWith('--url=')) {
            parsed.url = arg.substring(6);
        } else if (arg.startsWith('--file=')) {
            parsed.file = arg.substring(7);
        } else if (arg.startsWith('--output=')) {
            parsed.output = path.resolve(process.cwd(), arg.substring(9));
        } else if (arg.startsWith('--delay=')) {
            parsed.delay = parseInt(arg.substring(8), 10) || 500;
        }
    }

    return parsed;
}

async function capture() {
    const config = parseArgs();
    const targetUrl = config.url || (config.file ? `file://${path.resolve(config.file)}` : '');

    if (!targetUrl) {
        console.error('[ERROR] Please specify --url=<URL> or --file=<FilePath>');
        console.log('Example: node tests/visual-qa/capture-screenshots.js --url=http://127.0.0.1:8000/classes');
        process.exit(1);
    }

    if (!fs.existsSync(config.output)) {
        fs.mkdirSync(config.output, { recursive: true });
    }

    console.log(`[VISUAL-QA] Starting browser capture for target: ${targetUrl}`);
    console.log(`[VISUAL-QA] Output directory: ${config.output}`);

    const browser = await chromium.launch({
        headless: true,
    });

    const results = [];

    for (const vp of VIEWPORTS) {
        console.log(`[VISUAL-QA] Capturing ${vp.name} (${vp.width}x${vp.height})...`);
        const context = await browser.newContext({
            viewport: { width: vp.width, height: vp.height },
            isMobile: vp.isMobile,
            hasTouch: vp.hasTouch,
            deviceScaleFactor: 2, // Retina quality
        });

        const page = await context.newPage();

        try {
            await page.goto(targetUrl, {
                waitUntil: 'networkidle',
                timeout: 30000,
            }).catch(async (e) => {
                console.warn(`[VISUAL-QA] Networkidle timed out, waiting for DOM content loaded...`);
                await page.waitForLoadState('domcontentloaded');
            });

            if (config.delay > 0) {
                await page.waitForTimeout(config.delay);
            }

            const filename = `${vp.name}.png`;
            const filepath = path.join(config.output, filename);

            await page.screenshot({
                path: filepath,
                fullPage: config.fullPage,
            });

            console.log(`  -> Saved: ${filepath}`);
            results.push({ viewport: vp.name, width: vp.width, height: vp.height, path: filepath, status: 'ok' });
        } catch (err) {
            console.error(`[ERROR] Failed to capture ${vp.name}:`, err.message);
            results.push({ viewport: vp.name, status: 'error', error: err.message });
        } finally {
            await context.close();
        }
    }

    await browser.close();
    console.log('[VISUAL-QA] Browser capture complete. Results:');
    console.log(JSON.stringify(results, null, 2));
}

capture().catch((err) => {
    console.error('[FATAL]', err);
    process.exit(1);
});

