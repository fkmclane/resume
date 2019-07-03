#!/usr/bin/env python3
import asyncio
import os.path
import sys

import pyppeteer

if (len(sys.argv) != 1 and len(sys.argv) != 2) or '-h' in sys.argv:
    sys.stderr.write(f'Usage: {sys.argv[0]} [resume.html]\n')
    sys.exit(1)

if len(sys.argv) == 2:
    resume = sys.argv[1]
else:
    resume = 'resume.html'

async def take_screen():
    browser = await pyppeteer.launch({'headless': True, 'args': ['--window-size=1920,1080']})
    page = await browser.newPage()
    await page.goto('file://' + os.path.abspath(resume))
    await page.emulateMedia('screen');
    await page.pdf({'path': os.path.splitext(resume)[0] + '.pdf', 'scale': 0.6, 'printBackground': True});
    await browser.close()

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
asyncio.get_event_loop().run_until_complete(take_screen())
