import os, re, glob

files = glob.glob('/home/user/accountant-Kitchener/*.html')

old_css1 = '[data-clip]{clip-path:inset(0 0 100% 0)}'
old_css2 = '[data-clip].vis{clip-path:inset(-60px -60px -60px -60px);transition:clip-path .9s var(--eo)}'
old_reduced = '  .mcta,[data-clip].vis{transition:none}\n  [data-clip]{clip-path:none}'

new_css1 = '[data-clip]{opacity:0;transform:translateY(22px)}'
new_css2 = '[data-clip].vis{opacity:1;transform:translateY(0);transition:opacity .75s var(--eo),transform .75s var(--eo)}'
new_reduced = '  .mcta,[data-clip].vis{transition:none}\n  [data-clip]{opacity:1;transform:none}'

old_threshold = 'threshold:.25'
new_threshold = 'threshold:0'

count = 0
for f in files:
    with open(f) as fh:
        txt = fh.read()
    orig = txt
    txt = txt.replace(old_css1, new_css1)
    txt = txt.replace(old_css2, new_css2)
    txt = txt.replace(old_reduced, new_reduced)
    txt = txt.replace(old_threshold, new_threshold)
    if txt != orig:
        with open(f, 'w') as fh:
            fh.write(txt)
        count += 1

print(f'Fixed {count} files')
