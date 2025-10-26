function tes(){
    console.log("hai");   
}

/* Scroll-direction based reveal for .slideup elements
   - when scrolling down and element enters viewport -> add .in-view
   - when scrolling up -> remove .in-view so element moves back to the right
   Throttled for performance.
*/
(function(){
    const els = Array.from(document.querySelectorAll('.slideup'));
    if(!els.length) return;

    let lastY = window.pageYOffset || document.documentElement.scrollTop;

    function throttle(fn, wait){
        let last = 0;
        return function(...args){
            const now = Date.now();
            if(now - last >= wait){
                last = now;
                fn.apply(this, args);
            }
        };
    }

    function onScroll(){
        const currentY = window.pageYOffset || document.documentElement.scrollTop;
        const scrollingDown = currentY > lastY;
        lastY = currentY;

        els.forEach(el => {
            const r = el.getBoundingClientRect();
            const entersViewport = r.top < window.innerHeight * 0.9 && r.bottom > 0;

            if(scrollingDown && entersViewport){
                el.classList.add('in-view');
            } else if(!scrollingDown){
                // On any upward scroll, hide it (move back to right)
                el.classList.remove('in-view');
            }
        });
    }

    // run once to set initial state
    onScroll();
    window.addEventListener('scroll', throttle(onScroll, 100), { passive: true });
})();