import asyncio
from playwright.async_api import async_playwright
import os

async def generate_pdf():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Use the local server URL
        url = "http://localhost:8585/Empresa/02_COMERCIAL/clientes/CIAL/entrega/Deck_CIAL.html"
        output_path = r"C:\Users\abustamante\TheQaiCo\Empresa\02_COMERCIAL\clientes\CIAL\entrega\Deck_CIAL.pdf"
        
        print(f"Navigating to {url}...")
        await page.goto(url, wait_until="networkidle")
        
        # Force exact dimensions 1280x720 with zero margins
        # scale=1.0 ensures it doesn't try to fit to a different paper size
        await page.pdf(
            path=output_path,
            width="1280px",
            height="720px",
            print_background=True,
            margin={"top": "0px", "right": "0px", "bottom": "0px", "left": "0px"},
            scale=1.0,
            prefer_css_page_size=True
        )
        
        await browser.close()
        print(f"PDF successfully generated at {output_path} (1280x720, no margins)")

if __name__ == "__main__":
    asyncio.run(generate_pdf())
