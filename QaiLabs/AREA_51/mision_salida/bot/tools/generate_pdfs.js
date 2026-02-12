// --- DEPRECATED / LEGACY TOOL (JS VERSION) ---
// DO NOT USE for QAI Executive Horizon proposals.
// This is a backup script. The official motor is QaiCore/tools/generate_all_pdfs.py (Python).
// ------------------------------------------------

const playwright = require('playwright');
const path = require('path');
const fs = require('fs');

async function generatePDF({ inputUrl, outputPath, width, height, isA4 = false }) {
    console.log(`Generating PDF from ${inputUrl} to ${outputPath}...`);
    const browser = await playwright.chromium.launch();
    const context = await browser.newContext();
    const page = await context.newPage();

    // Set viewport to match the slide size
    await page.setViewportSize({ width: parseInt(width) || 1280, height: parseInt(height) || 720 });

    await page.goto(inputUrl, { waitUntil: 'networkidle' });

    const pdfOptions = {
        path: outputPath,
        printBackground: true,
    };

    if (isA4) {
        pdfOptions.format = 'A4';
        pdfOptions.margin = { top: '15mm', right: '15mm', bottom: '15mm', left: '15mm' };
    } else {
        pdfOptions.width = width || '1280px';
        pdfOptions.height = height || '720px';
        pdfOptions.margin = { top: 0, right: 0, bottom: 0, left: 0 };
    }

    await page.pdf(pdfOptions);
    await browser.close();
    console.log(`PDF successfully generated at ${outputPath}`);
}

const args = process.argv.slice(2);
if (args.length < 2) {
    console.log('Usage: node generate_pdfs.js <inputUrl> <outputPath> [width] [height] [isA4]');
    process.exit(1);
}

const [inputUrl, outputPath, width, height, isA4Str] = args;
generatePDF({
    inputUrl,
    outputPath,
    width,
    height,
    isA4: isA4Str === 'true'
}).catch(err => {
    console.error(err);
    process.exit(1);
});
