#!/usr/bin/env python3
"""Generate the 7 remaining service pages from content data + shared template."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from assemble import assemble, TPL

REVIEWS = [
    ("MS","Muhammad Saad","Filing my personal taxes has always felt overwhelming, but the professionals here completely changed that. They were knowledgeable and made the whole process incredibly easy. Highly recommend."),
    ("JC","Janet Campitelli-Montgomery","Ibtehaj was professional, efficient, and very knowledgeable. He took the time to explain everything clearly and made the whole process smooth and stress-free. Highly recommend for anyone looking for reliable accounting services."),
    ("CI","Chinaar Inc.","Extremely professional, knowledgeable, and reliable. They helped navigate both personal and business finances with great attention to detail. Their advice saved me time and money during tax season and beyond."),
    ("SR","Syed Rizvi","Top-notch services without charging an arm and a leg. As a small business owner and Realtor, I appreciate their affordability and the fact that they never compromise on quality. Hashmi became a trusted advisor for my business."),
    ("HI","Haris Iqbal","As a student, filing taxes felt confusing and overwhelming, but the team made the entire process simple and stress-free. Incredibly patient and took the time to explain everything clearly. Highly recommend."),
]

def review_cards(idxs):
    out=[]
    for n,i in enumerate(idxs):
        av,name,text=REVIEWS[i]
        d=f' data-delay="{n}"' if n else ''
        out.append(f'''      <div class="rc" data-reveal{d}>
        <div class="rc-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="rc-text">"{text}"</p>
        <div class="rc-foot"><div class="rc-av">{av}</div><div><div class="rc-name">{name}</div><div class="rc-src">Google Review</div></div></div>
      </div>''')
    return '\n'.join(out)

def checks(items):
    return '\n'.join(f'          <div class="check"><span><b>{b}</b> {t}</span></div>' for b,t in items)

def sidebar_list(items):
    return '\n'.join(f'            <li>{i}</li>' for i in items)

def stats(items):
    out=[]
    for n,l in items:
        dc=' data-count' if n[0].isdigit() else ''
        out.append(f'      <div class="st"><span class="n"{dc}>{n}</span><span class="l">{l}</span></div>')
    return '\n'.join(out)

def faq_items(items):
    return '\n'.join(f'        <div class="faq-it"><div class="faq-q">{q}</div><div class="faq-a">{a}</div></div>' for q,a in items)

def build(p):
    faq_sec = ''
    if p.get('faq'):
        faq_sec = f'''
<section data-reveal>
  <div class="container">
    <div class="sec-head center">
      <h2 class="h-sec">Common questions answered</h2>
    </div>
    <div class="faq-narrow">
      <div class="faq-wrap">
{faq_items(p['faq'])}
      </div>
    </div>
  </div>
</section>
'''
    return f'''<section class="page-hero">
  <div class="container">
    <span class="crumb"><a href="index.html">Home</a> / {p['crumb']}</span>
    <h1>{p['h1']}</h1>
    <p class="lead">{p['lead']}</p>
    <div class="ph-btns">
      <a href="contact.html" class="btn btn-primary">Book a Free Consultation <span class="arr">&rarr;</span></a>
      <a href="tel:6475649666" class="btn btn-ghost">Call (647) 564-9666</a>
    </div>
  </div>
</section>

<section data-reveal>
  <div class="container">
    <div class="split">
      <div>
        <h2 class="h-sec">{p['checks_h']}</h2>
        <div class="checks">
{checks(p['checks'])}
        </div>
      </div>
      <div class="split-img" data-reveal>
        <img src="{p['img']}" alt="{p['img_alt']}" loading="lazy">
      </div>
    </div>
  </div>
</section>

<section class="bg-stone" data-reveal>
  <div class="container">
    <div class="split" style="align-items:start">
      <div class="prose">
{p['prose']}
      </div>
      <div>
        <div class="info-p">
          <h3>{p['sidebar_h']}</h3>
          <ul>
{sidebar_list(p['sidebar'])}
          </ul>
        </div>
        <div class="info-p" style="margin-top:20px;background:var(--paper)">
          <h3>Why work with a CPA</h3>
          <ul>
            <li>CPA Canada member firm</li>
            <li>18+ years of experience</li>
            <li>Upfront quote before we start</li>
            <li>In-person or fully virtual</li>
          </ul>
          <div style="margin-top:22px"><a href="contact.html" class="btn btn-forest btn-sm" style="width:100%">Get an Upfront Quote</a></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section data-reveal>
  <div class="container">
    <div class="sec-head">
      <h2 class="h-sec">{p['band_h']}</h2>
      <p class="lead">{p['band_p']}</p>
    </div>
    <div class="stat-row">
{stats(p['stats'])}
    </div>
  </div>
</section>

<section class="bg-stone" data-reveal>
  <div class="container">
    <div class="rev-head">
      <h2 class="h-sec" style="margin-bottom:0">What our clients say</h2>
      <div class="gbadge"><span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span><span>5.0 / 5 on Google</span></div>
    </div>
    <div class="reviews-grid">
{review_cards(p['reviews'])}
    </div>
  </div>
</section>
{faq_sec}
<section class="cta-band" data-reveal>
  <div class="container">
    <h2>{p['cta_h']}</h2>
    <p>{p['cta_p']}</p>
    <div class="cta-btns">
      <a href="contact.html" class="btn btn-white">Book a Free Consultation <span class="arr">&rarr;</span></a>
      <a href="tel:6475649666" class="btn btn-ghost-w">Call (647) 564-9666</a>
    </div>
    <p class="cta-note">We respond within 1 business day &middot; Open Mon&ndash;Sat, 10am&ndash;9pm</p>
  </div>
</section>
'''

PAGES = {
'personal-tax-accountant-kitchener.html': dict(
  crumb='Personal Tax',
  h1='A personal tax accountant who puts more back in your pocket.',
  lead='T1 returns, rental and investment income, RRSP planning, and CRA support for individuals and families across Kitchener-Waterloo.',
  checks_h='Personal tax that works for you',
  checks=[
    ('Full review of your situation.','We ask questions, find credits you may not know exist, and build the most advantageous return for your circumstances.'),
    ('RRSP and TFSA planning.','Maximize registered account contributions to reduce your taxable income now and build long-term wealth.'),
    ('Rental and investment income.','Rental properties, capital gains, and foreign income handled correctly with every deduction claimed.'),
    ('Newcomers and students.','First time filing in Canada? We walk you through every step and ensure you receive all credits you are entitled to.'),
  ],
  img='https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=1000&q=75',
  img_alt='Personal tax accountant consultation in Kitchener',
  prose='''        <h2>Personal tax returns in Kitchener</h2>
        <p>Filing your personal income tax return should not be stressful. Our Kitchener professional team takes care of everything, from gathering the right slips to identifying every deduction you are entitled to.</p>
        <h3>Deductions we maximize</h3>
        <p>Our Kitchener personal tax accountants review every line of your return to ensure you are claiming all eligible deductions: childcare expenses, moving expenses, home office costs for remote workers, medical expenses, charitable donations, professional dues, and education credits for students at Conestoga College, University of Waterloo, and Wilfrid Laurier.</p>
        <p>We also provide year-round tax planning advice. Read our <a href="blog-rrsp-vs-tfsa.html">RRSP vs TFSA guide</a> to understand which account works best for your situation.</p>''',
  sidebar_h='What we prepare',
  sidebar=[
    'T1 personal income tax returns for all income types',
    'Employment income from one or multiple employers',
    'Self-employment and freelance income',
    'Rental property income and expenses',
    'Investment income including dividends and capital gains',
    'RRSP and TFSA planning and contribution reporting',
    'Pension and retirement income (CPP, OAS, RRIF)',
    'Foreign income and international tax obligations',
  ],
  band_h='A personal tax accountant who works for you, not just the CRA',
  band_p='Our Kitchener clients consistently receive larger refunds and fewer CRA surprises. That is what a proactive personal tax accountant looks like.',
  stats=[('500+','Returns filed'),('5.0','Google rating'),('2wk','Typical refund via NETFILE'),('48hr','Turnaround')],
  reviews=[0,4,1],
  faq=[
    ('Can I claim home office expenses?','Yes. If you work from home, you may be eligible to claim a portion of your rent, utilities, internet, and supplies as home office expenses on your T1.'),
    ('What if I worked in another province?','We handle multi-province returns and ensure your income is allocated correctly between provinces for proper tax treatment.'),
    ('How long does it take to get my refund?','Electronic filings through NETFILE typically result in refunds within 2 weeks. We file electronically for all eligible returns.'),
    ('Do you offer tax planning as well as filing?','Absolutely. We provide year-round tax planning including RRSP contribution timing, income splitting, and deduction strategies, not just annual filing.'),
  ],
  cta_h='Ready for a bigger refund and fewer surprises?',
  cta_p='Book a free consultation with a Kitchener personal tax accountant. No obligation, no jargon.',
),
'small-business-tax-accountant-kitchener.html': dict(
  crumb='Small Business Tax',
  h1='Accounting that grows with your business.',
  lead='T2 corporate returns, incorporation advice, and salary-vs-dividend planning for owner-operated businesses across Kitchener-Waterloo.',
  checks_h='A real accounting partner, not a once-a-year filer',
  checks=[
    ('Corporate T2 returns.','CRA-compliant T2 filing for incorporated Ontario businesses with every eligible deduction applied.'),
    ('Year-round bookkeeping.','Monthly or quarterly bookkeeping so your books are always clean and year-end costs nothing extra.'),
    ('Incorporation advisory.','We run the numbers and show you the real tax savings of incorporating before you decide.'),
    ('Salary vs dividends planning.','Optimize how you pay yourself to minimize total tax across both personal and corporate returns.'),
  ],
  img='https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=1000&q=75',
  img_alt='Small business accounting team in Kitchener',
  prose='''        <h2>Accounting for Kitchener small businesses</h2>
        <p>Running a small business in Kitchener is demanding. Managing your accounting and taxes should not make it harder. Our professional accountants handle everything so you can focus on growing your business.</p>
        <h3>Corporate Tax Returns (T2)</h3>
        <p>We prepare and file T2 corporate income tax returns for incorporated small businesses in Kitchener. We maximize the small business deduction, apply all eligible credits, and ensure your return is filed accurately and on time.</p>
        <h3>Business Tax Planning</h3>
        <p>Strategic tax planning is where accountants add the most value. We help you structure your business, time income and expenses, and minimize your annual tax bill legally. See our guide on <a href="blog-salary-vs-dividend.html">salary vs dividend planning</a> for incorporated owners.</p>''',
  sidebar_h='Industries we serve',
  sidebar=[
    'Real estate and Realtors in Kitchener',
    'Construction and trades businesses',
    'Tech startups and IT consultants',
    'Restaurants and retail businesses',
    'Healthcare and professional services',
    'Trucking and logistics companies',
    'E-commerce and online businesses',
  ],
  band_h='Kitchener small businesses deserve more than a once-a-year accountant',
  band_p='We work with trades, retailers, consultants, and tech companies across Kitchener-Waterloo as their dedicated accounting partner, not just their tax filer.',
  stats=[('T2','Corporate returns'),('5.0','Google rating'),('6+','Years local'),('QB Elite','Certified ProAdvisor')],
  reviews=[3,2,1],
  faq=None,
  cta_h='Ready for an accountant who calls you back?',
  cta_p='Book a free consultation about your business. No obligation, and a clear quote before we start.',
),
'cpa-kitchener.html': dict(
  crumb='CPA Services',
  h1='Work directly with a Chartered Professional Accountant.',
  lead='Rigorous professional standards, CPA Canada membership, and 18+ years of experience behind every engagement in Kitchener, Ontario.',
  checks_h='The difference a CPA makes',
  checks=[
    ('Regulated and accountable.','CPA Canada membership means strict professional standards, ethics requirements, and continuing education.'),
    ('Strategic, not just compliance.','A CPA identifies tax-saving structures, flags risks early, and advises before you make decisions.'),
    ('Full scope of services.','Tax, accounting, bookkeeping, payroll, incorporation, and CRA representation from one regulated professional.'),
    ('CRA representation.','If you receive a CRA letter or audit, we handle it. You do not need to speak to the CRA yourself.'),
  ],
  img='https://images.unsplash.com/photo-1521791136064-7986c2920216?auto=format&fit=crop&w=1000&q=75',
  img_alt='CPA shaking hands with a client in Kitchener',
  prose='''        <h2>What a Kitchener CPA does for you</h2>
        <p>A Chartered Professional Accountant (CPA) is Canada's highest accounting designation, requiring rigorous training, regulated standards, and a legal obligation to act in your best interest. When you work with our CPA office in Kitchener, you are getting a qualified financial professional who takes full accountability for every recommendation.</p>
        <h3>Why the CPA designation matters</h3>
        <p>In Ontario, only designated CPAs may provide certain accounting and assurance services. When your business needs reviewed financials, tax opinions, or regulated advisory, you need a CPA. Our Kitchener CPA office gives you full professional accountability.</p>
        <h3>Our credentials</h3>
        <p>CPA Canada member firm in good standing. CPA, CGA designation and FCCA (UK) Fellow Chartered Certified Accountant (Ibtahaj Hashmi). 18+ years of experience in public accounting, serving Kitchener since 2019, with 100% professional liability coverage.</p>''',
  sidebar_h='CPA services we provide',
  sidebar=[
    'Personal and corporate tax planning and filing',
    'Financial statement preparation (NTR / compilation)',
    'Business advisory and strategic planning',
    'Governance, risk, and compliance services',
    'CRA audit representation and correspondence',
    'Business valuation and acquisition support',
    'Cash flow analysis and financial projections',
    'Year-round CPA advisory on demand',
  ],
  band_h='CPA Canada certified. Kitchener focused.',
  band_p='Ibtahaj Hashmi, CPA, FCCA leads every client engagement. With 18+ years of experience and dual credentials, you get real professional expertise, not a junior preparer.',
  stats=[('18+','Years of experience'),('5.0','Google rating'),('CPA','Canada member firm'),('FCCA','UK dual credential')],
  reviews=[1,2,3],
  faq=None,
  cta_h='Get a CPA in your corner.',
  cta_p='Book a free consultation with a Kitchener Chartered Professional Accountant. No obligation, no jargon.',
),
'bookkeeping-services-kitchener.html': dict(
  crumb='Bookkeeping',
  h1='Clean books mean better business decisions.',
  lead='Professional monthly bookkeeping for small businesses in Kitchener. Clean books, timely reporting, and a stress-free year-end at affordable rates.',
  checks_h='Bookkeeping you never have to think about',
  checks=[
    ('Monthly reconciliation.','Every transaction categorized, every bank account reconciled on time, every month, without you thinking about it.'),
    ('Cloud accounting setup.','QuickBooks, Xero, and Wave. We set you up, train your team if needed, and keep everything accurate.'),
    ('Financial reporting.','Clear profit and loss statements, balance sheets, and cash flow reports so you always know your position.'),
    ('HST tracking built in.','We track HST as we go so your quarterly or annual filing is ready with no scramble at deadline.'),
  ],
  img='https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=1000&q=75',
  img_alt='Bookkeeping and cloud accounting dashboard for a Kitchener business',
  prose='''        <h2>Bookkeeping in Kitchener you can rely on</h2>
        <p>Accurate bookkeeping is the foundation of every financially healthy business. Our Kitchener bookkeeping services keep your accounts organized, your reporting current, and your <a href="tax-filing-kitchener.html">year-end tax filing</a> straightforward, so you always know exactly where your business stands.</p>
        <h3>Monthly Bookkeeping</h3>
        <p>We handle all your monthly transaction recording, bank reconciliations, accounts payable and receivable tracking, and financial close, so you receive clean, accurate books every month without lifting a finger.</p>
        <h3>Cloud-Based Accounting</h3>
        <p>We work with QuickBooks Online, Xero, Wave, and other cloud accounting platforms, giving you real-time financial visibility from anywhere. We set up, train, and maintain your cloud accounting system for maximum efficiency.</p>
        <h3>Catch-Up Bookkeeping</h3>
        <p>If your books are behind by months or even years, we provide catch-up bookkeeping services to bring your records up to date.</p>''',
  sidebar_h='What is included',
  sidebar=[
    'Monthly transaction categorization',
    'Bank and credit card reconciliation',
    'Accounts payable and receivable management',
    'Monthly profit and loss and balance sheet',
    'HST tracking and remittance support',
    'Year-end working paper preparation',
    'Bookkeeper to accountant handoff for tax season',
  ],
  band_h='Stop losing hours to bookkeeping. Focus on your business.',
  band_p='Kitchener business owners who work with us spend less time on administration and more time serving customers. Your books are always current, HST-ready, and audit-proof.',
  stats=[('QB Elite','ProAdvisor certified'),('Monthly','Reporting cadence'),('5.0','Google rating'),('6+','Years local')],
  reviews=[3,2,0],
  faq=None,
  cta_h='Ready to hand off your bookkeeping?',
  cta_p='Book a free consultation and get a clear monthly quote. No obligation, no jargon.',
),
'payroll-services-kitchener.html': dict(
  crumb='Payroll Services',
  h1='Payroll that runs without you running it.',
  lead='Reliable, accurate payroll processing for Kitchener businesses. We handle every aspect of payroll from processing runs to CRA remittances.',
  checks_h='Every pay period, handled',
  checks=[
    ('Full payroll processing.','Salaries, wages, hourly staff, and contractors processed on schedule every pay period without errors.'),
    ('Source deductions and remittances.','CPP, EI, and income tax withheld correctly and remitted to the CRA on time, every time.'),
    ('T4 slips and year-end.','T4 preparation and filing handled for all employees before the February deadline.'),
    ('ROE and compliance.','Records of Employment, payroll registers, and all required CRA documentation maintained and filed.'),
  ],
  img='https://images.unsplash.com/photo-1521791136064-7986c2920216?auto=format&fit=crop&w=1000&q=75',
  img_alt='Payroll processing for a Kitchener business',
  prose='''        <h2>Payroll for Kitchener businesses</h2>
        <p>Our Kitchener payroll service takes the entire process off your plate, ensuring your employees are paid on time, every time, and all CRA obligations are met without fail. For growing businesses, we pair payroll with <a href="bookkeeping-services-kitchener.html">bookkeeping services</a> for a fully integrated financial back office.</p>
        <h3>Payroll Processing</h3>
        <p>We process regular payroll runs, weekly, bi-weekly, or semi-monthly, calculating gross pay, deductions (CPP, EI, income tax), and net pay for each employee accurately and on schedule.</p>
        <h3>Source Deductions and CRA Remittances</h3>
        <p>We calculate and remit all source deductions to CRA on time. Late remittances trigger immediate CRA penalties. We ensure you never miss a deadline.</p>
        <h3>T4 Preparation and Filing</h3>
        <p>At year-end, we prepare and file all T4 slips and the T4 summary with CRA and provide employee copies for their <a href="personal-tax-accountant-kitchener.html">personal tax returns</a>. The February deadline is never missed.</p>''',
  sidebar_h='What we handle',
  sidebar=[
    'Weekly, bi-weekly, or monthly payroll runs',
    'CPP and EI calculations and remittances',
    'Federal and Ontario income tax withholding',
    'CRA payroll account setup and management',
    'ROE (Record of Employment) preparation',
    'T4 and T4 summary filing',
    'Vacation pay and statutory holiday calculations',
  ],
  band_h='A payroll error can cost more than you think',
  band_p='CRA payroll penalties are strict. Our Kitchener team ensures every remittance is on time, every deduction is correct, and your employees are paid accurately.',
  stats=[('Zero','Late remittances'),('T4','Ready every February'),('5.0','Google rating'),('6+','Years local')],
  reviews=[2,3,1],
  faq=None,
  cta_h='Take payroll off your plate.',
  cta_p='Book a free consultation and get a clear per-run quote. No obligation, no jargon.',
),
'hst-filing-kitchener.html': dict(
  crumb='HST Filing',
  h1='HST filing without the headache.',
  lead='Accurate HST/GST registration, return filing, and compliance for Ontario businesses. Avoid penalties, recover ITCs, and stay on the right side of the CRA.',
  checks_h='HST handled end to end',
  checks=[
    ('Registration at the right time.','We register you for HST correctly, set up your reporting period, and ensure you never miss the $30,000 threshold.'),
    ('Input tax credit recovery.','We claim every eligible ITC so you only remit the net HST you owe, not a dollar more.'),
    ('Quarterly and annual filing.','Accurate HST/GST returns filed before every deadline with supporting records maintained properly.'),
    ('CRA HST audit support.','If the CRA questions your HST, we handle the review and respond to requests professionally.'),
  ],
  img='https://images.unsplash.com/photo-1450101499163-c8848c66ca85?auto=format&fit=crop&w=1000&q=75',
  img_alt='HST return preparation for an Ontario business',
  prose='''        <h2>HST filing in Kitchener</h2>
        <p>HST is one of the most complex and commonly mismanaged areas of <a href="small-business-tax-accountant-kitchener.html">small business compliance</a> in Ontario. Our Kitchener accountants handle every aspect of your HST obligations. Read our complete <a href="blog-hst-guide.html">HST guide for Ontario business owners</a>.</p>
        <h3>HST Registration</h3>
        <p>If your business revenue exceeds $30,000 in a rolling 12-month period, you are required to register for HST in Ontario. We guide you through the registration process with CRA, determine your optimal filing frequency, and set up your systems for clean HST tracking from day one.</p>
        <h3>HST Return Filing</h3>
        <p>We prepare and file your HST returns, monthly, quarterly, or annually, with full reconciliation of sales, ITC claims, and net remittances. All calculations are reviewed by a <a href="cpa-kitchener.html">professional accountant</a> before submission.</p>
        <h3>Input Tax Credit (ITC) Recovery</h3>
        <p>Many businesses underreport their Input Tax Credits and overpay HST unnecessarily. Our team ensures every eligible ITC is identified and claimed, reducing your net HST payable legally and compliantly.</p>''',
  sidebar_h='Common HST issues we resolve',
  sidebar=[
    'Late registration penalties',
    'CRA HST audit support and correspondence',
    'Missed or late filing catch-up',
    'Incorrect ITC claims, correction and amendment',
    'HST on real estate transactions',
    'Export and zero-rated supply classification',
  ],
  band_h='Most Kitchener business owners overpay HST without knowing it',
  band_p='Missed input tax credits, wrong reporting periods, and late filings cost Ontario businesses thousands each year. Our team makes sure your HST is filed right and every eligible credit is recovered.',
  stats=[('ITC','Recovery focus'),('On time','Every filing'),('5.0','Google rating'),('Ontario','Registered')],
  reviews=[2,3,0],
  faq=None,
  cta_h='Stop overpaying HST.',
  cta_p='Book a free consultation and find out what your HST position should look like. No obligation.',
),
'tax-consulting-kitchener.html': dict(
  crumb='Tax Consulting',
  h1='Strategic tax advice that moves the needle.',
  lead='Go beyond filing. Get strategic tax advice from a Kitchener professional. We help individuals and businesses make better decisions that reduce tax.',
  checks_h='Planning, not just filing',
  checks=[
    ('Tax structure optimization.','Salary, dividends, holdcos, family trusts: we model the right structure for your income and goals.'),
    ('Incorporation and reorganization.','Section 85 rollovers, corporate restructuring, and share reorganizations handled by experienced CPAs.'),
    ('CRA dispute resolution.','Objections, appeals, and audit responses prepared and presented professionally to protect your position.'),
    ('Estate and succession planning.','Minimize probate and capital gains on your estate transfer. Plan early, pay less.'),
  ],
  img='https://images.unsplash.com/photo-1554224155-6726b3ff858f?auto=format&fit=crop&w=1000&q=75',
  img_alt='Strategic tax planning session in Kitchener',
  prose='''        <h2>Tax strategy for Kitchener clients</h2>
        <p>Most people file taxes reactively, once a year, after the year is done. Our tax consulting services in Kitchener help you plan proactively, making decisions throughout the year that legally minimize your tax burden and support your long-term financial goals.</p>
        <h3>Personal Tax Consulting</h3>
        <p>We advise Kitchener residents on RRSP vs TFSA strategy, income splitting, family tax planning, estate planning, rental property structuring, and timing of capital gains and losses. See our <a href="blog-rrsp-vs-tfsa.html">RRSP vs TFSA guide</a> and <a href="blog-rental-income-tax.html">rental income tax guide</a>.</p>
        <h3>Business Tax Consulting</h3>
        <p>For <a href="small-business-tax-accountant-kitchener.html">small business owners</a> and corporations in Kitchener, we provide advice on incorporation timing, salary vs dividend optimization, holding company structures, tax deferral strategies, and succession planning. Read our <a href="blog-salary-vs-dividend.html">salary vs dividend guide</a>.</p>
        <h3>CRA Dispute and Audit Support</h3>
        <p>If you have received a CRA audit notice, reassessment, or compliance letter, our Kitchener professionals handle your response and representation. Read our guide on <a href="blog-cra-letter.html">how to respond to a CRA letter</a> before you take any action.</p>''',
  sidebar_h='Areas of tax consulting',
  sidebar=[
    'Income splitting and family tax planning',
    'Salary vs dividend optimization for business owners',
    'Incorporation and corporate restructuring',
    'Real estate and rental property tax strategy',
    'Capital gains planning and timing',
    'RRSP, TFSA, and retirement tax planning',
    'Estate and succession planning',
    'CRA audit defence and objection filing',
  ],
  band_h='Proactive planning saves far more than reactive filing',
  band_p='The best tax advice comes before the transaction, not after. Our consultants work alongside you throughout the year to identify savings, reduce risk, and build a compliant, efficient structure.',
  stats=[('18+','Years advisory'),('CPA','Canada certified'),('5.0','Google rating'),('Multi-year','Planning horizon')],
  reviews=[2,1,3],
  faq=None,
  cta_h='Plan ahead. Pay less.',
  cta_p='Book a free consultation with a Kitchener tax consultant. The best time to plan is before the transaction.',
),
}

for page, data in PAGES.items():
    main_name = 'main-'+page
    open(os.path.join(TPL, main_name),'w').write(build(data))
    assemble(page, main_name)
