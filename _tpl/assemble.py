#!/usr/bin/env python3
"""Assemble a page: extracts <head> meta from the OLD page (title, description,
keywords, canonical, og, geo, JSON-LD), swaps in the new stylesheet link, and
wraps the new <main> content with the shared header/footer templates."""
import re, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL = os.path.join(ROOT, '_tpl')

def assemble(page, main_file):
    old = open(os.path.join(ROOT, page)).read()
    head = re.search(r'<head>(.*?)</head>', old, re.S).group(1)
    # strip old style/import blocks and font links
    head = re.sub(r'<style>.*?</style>', '', head, flags=re.S)
    head = re.sub(r'<link rel="stylesheet"[^>]*>', '', head)
    head = re.sub(r'\n{3,}', '\n', head).strip()

    main = open(os.path.join(TPL, main_file)).read()
    header = open(os.path.join(TPL, 'header.html')).read()
    footer = open(os.path.join(TPL, 'footer.html')).read()

    out = f'''<!DOCTYPE html>
<html lang="en">
<head>
{head}
<link rel="stylesheet" href="assets/css/main.css">
</head>
<body>
{header}<main>
{main}</main>
{footer}'''
    open(os.path.join(ROOT, page), 'w').write(out)
    print(f'assembled {page} ({len(out)} bytes)')

if __name__ == '__main__':
    assemble(sys.argv[1], sys.argv[2])
