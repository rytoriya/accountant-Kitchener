import os, re, glob

files = glob.glob('/home/user/accountant-Kitchener/*.html')

changes = 0
for path in files:
    with open(path) as f:
        txt = f.read()
    orig = txt

    # (a) Add loading="lazy" to non-hero Unsplash images missing it
    # Hero images already have loading="eager", skip those
    # Pattern: <img ... src="https://images.unsplash..." without loading= attribute
    def add_lazy(m):
        tag = m.group(0)
        if 'loading=' in tag:
            return tag
        return tag.replace('<img', '<img loading="lazy"', 1)
    # Only apply to img tags in non-hero contexts (those with loading="eager" are already set)
    txt = re.sub(r'<img(?![^>]*loading=)[^>]*unsplash\.com[^>]*>', add_lazy, txt)

    # (b) Color discipline: stat numbers black instead of green
    # .sn color:var(--g) → color:var(--blk)
    txt = txt.replace(
        '.sn{font-family:var(--fh);font-size:32px;font-weight:800;color:var(--g);display:block;line-height:1}',
        '.sn{font-family:var(--fh);font-size:32px;font-weight:800;color:var(--blk);display:block;line-height:1}'
    )

    # (b) Nav CTA: solid green → outline style (less aggressive, still prominent)
    txt = txt.replace(
        '.nav-cta-btn{\n  display:inline-block;\n  background:var(--g);color:var(--wht)!important;\n  padding:0 17px;height:38px;line-height:38px;\n  border-radius:var(--r);margin-left:8px;\n  font-family:var(--fb);font-size:11px;font-weight:700;\n  letter-spacing:.05em;text-transform:uppercase;\n  text-decoration:none!important;\n  transition:background .2s,box-shadow .2s;\n  white-space:nowrap;flex-shrink:0;\n}',
        '.nav-cta-btn{\n  display:inline-block;\n  background:transparent;color:var(--g)!important;\n  padding:0 17px;height:38px;line-height:38px;\n  border-radius:var(--r);margin-left:8px;border:1.5px solid var(--g);\n  font-family:var(--fb);font-size:11px;font-weight:700;\n  letter-spacing:.05em;text-transform:uppercase;\n  text-decoration:none!important;\n  transition:background .2s,color .2s,box-shadow .2s;\n  white-space:nowrap;flex-shrink:0;\n}'
    )
    txt = txt.replace(
        '.nav-cta-btn:hover{background:var(--gd);box-shadow:0 4px 16px rgba(58,158,73,.3)}',
        '.nav-cta-btn:hover{background:var(--g);color:var(--wht)!important;box-shadow:0 4px 16px rgba(58,158,73,.3)}'
    )

    # (a) Netlify form wiring in contact.html
    if 'contact.html' in path:
        txt = txt.replace(
            '<form class="lf">',
            '<form class="lf" name="contact" method="POST" data-netlify="true"><input type="hidden" name="form-name" value="contact">'
        )
        # Remove the fake JS form handler (it conflicts with netlify)
        txt = txt.replace(
            """  var f=document.querySelector('.lf');
  if(f)f.addEventListener('submit',function(e){
    e.preventDefault();
    var b=f.querySelector('.fsub');
    b.textContent='Message sent. We will be in touch soon.';
    b.style.background='#2C7A38';b.disabled=true;
  });""",
            ""
        )

    if txt != orig:
        with open(path, 'w') as f:
            f.write(txt)
        changes += 1
        print(f'Updated: {os.path.basename(path)}')

print(f'\nTotal files changed: {changes}')
