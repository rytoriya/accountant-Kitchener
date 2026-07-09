(function(){
  'use strict';

  /* Active nav link */
  var cp=window.location.pathname.split('/').pop()||'index.html';
  document.querySelectorAll('.main-nav a').forEach(function(a){
    if(a.getAttribute('href')===cp)a.classList.add('active');
  });

  /* Mobile nav */
  var ham=document.querySelector('.hamburger'),nav=document.querySelector('.nav-wrap');
  if(ham&&nav){
    ham.addEventListener('click',function(){nav.classList.toggle('open')});
    document.querySelectorAll('.main-nav .dt').forEach(function(dt){
      dt.addEventListener('click',function(){
        if(window.innerWidth<=1080)dt.parentElement.classList.toggle('open');
      });
    });
  }

  /* Compact header on scroll */
  var hdr=document.querySelector('.site-header');
  if(hdr&&'IntersectionObserver' in window){
    var sent=document.createElement('div');
    sent.style.cssText='position:absolute;top:0;height:90px;width:1px;pointer-events:none';
    document.body.prepend(sent);
    new IntersectionObserver(function(en){
      hdr.classList.toggle('compact',!en[0].isIntersecting);
    }).observe(sent);
  }

  /* Scroll reveals */
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(en){
      en.forEach(function(e){
        if(e.isIntersecting){e.target.classList.add('vis');io.unobserve(e.target)}
      });
    },{threshold:0,rootMargin:'0px 0px -8% 0px'});
    document.querySelectorAll('[data-reveal]').forEach(function(el){io.observe(el)});
  }else{
    document.querySelectorAll('[data-reveal]').forEach(function(el){el.classList.add('vis')});
  }

  /* Count-up stats */
  function countUp(el){
    var txt=el.textContent.trim();
    var m=txt.match(/^([\d.]+)(.*)$/);
    if(!m)return;
    var target=parseFloat(m[1]),suffix=m[2],dec=(m[1].split('.')[1]||'').length;
    var t0=null,dur=1400;
    function frame(t){
      if(!t0)t0=t;
      var p=Math.min((t-t0)/dur,1);
      p=1-Math.pow(1-p,3);
      el.textContent=(target*p).toFixed(dec)+suffix;
      if(p<1)requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }
  if('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches){
    var cio=new IntersectionObserver(function(en){
      en.forEach(function(e){
        if(e.isIntersecting){countUp(e.target);cio.unobserve(e.target)}
      });
    },{threshold:.4});
    document.querySelectorAll('[data-count]').forEach(function(el){cio.observe(el)});
  }

  /* FAQ accordion */
  document.querySelectorAll('.faq-q').forEach(function(q){
    q.addEventListener('click',function(){
      var it=q.parentElement,open=it.classList.contains('open');
      it.parentElement.querySelectorAll('.faq-it.open').forEach(function(o){o.classList.remove('open')});
      if(!open)it.classList.add('open');
    });
  });

  /* Mobile CTA bar — show after hero */
  var bar=document.querySelector('.mcta');
  var heroEl=document.querySelector('.hero, .page-hero, .art-hero');
  if(bar&&heroEl&&'IntersectionObserver' in window){
    new IntersectionObserver(function(en){
      bar.classList.toggle('show',!en[0].isIntersecting);
    }).observe(heroEl);
  }else if(bar){bar.classList.add('show')}

  /* Open-now status (Mon-Fri 9-6, Sat 10-2 ET) */
  var openEl=document.getElementById('open-now');
  if(openEl){
    try{
      var now=new Date(new Date().toLocaleString('en-US',{timeZone:'America/Toronto'}));
      var d=now.getDay(),h=now.getHours();
      var open=d!==0&&h>=10&&h<21;
      openEl.textContent=open?'Open now until 9pm':'Currently closed';
      openEl.className=open?'o-open':'o-closed';
    }catch(e){}
  }

  /* Contact form: client-side validation UX (Netlify handles submission) */
  var form=document.querySelector('form[name="contact"]');
  if(form){
    form.addEventListener('submit',function(){
      var b=form.querySelector('.fsub');
      if(b){b.textContent='Sending…';b.disabled=true}
    });
  }
})();
