#!/usr/bin/env node

/**
 * Agentix (agx) CLI Node.js Runner
 * Spawns the underlying agx.py engine.
 */

import { spawn } from 'child_process';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const scriptPath = path.resolve(__dirname, '../scripts/agx.py');
const args = process.argv.slice(2);

const isWindows = process.platform === 'win32';
const pythonCmd = isWindows ? 'python' : 'python3';

const child = spawn(pythonCmd, [scriptPath, ...args], {
    stdio: 'inherit',
    cwd: process.cwd(),
});

child.on('error', (err) => {
    if (err.code === 'ENOENT') {
        console.error(`[AGENTIX] Error: '${pythonCmd}' not found in PATH. Please ensure Python 3.10+ is installed.`);
    } else {
        console.error(`[AGENTIX] Execution error:`, err.message);
    }
    process.exit(1);
});

child.on('close', (code) => {
    process.exit(code ?? 0);
});
