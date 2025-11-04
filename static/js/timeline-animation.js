/**
 * TIMELINE ANIMATION
 * Anime le dessin de la ligne de timeline au scroll
 * Slide-in des éléments depuis la gauche
 */

document.addEventListener('DOMContentLoaded', function() {
    const timelineItems = document.querySelectorAll('.timeline-item');
    
    // IntersectionObserver pour les éléments de timeline
    const timelineObserver = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                
                // Animer la ligne de timeline
                updateTimelineLine(entry.target);
            }
        });
    }, { 
        threshold: 0.2,
        rootMargin: '0px 0px -100px 0px'
    });
    
    // Observer tous les éléments de timeline
    timelineItems.forEach(item => {
        timelineObserver.observe(item);
    });
    
    // Fonction pour mettre à jour la hauteur de la ligne
    function updateTimelineLine(item) {
        const timeline = item.closest('.timeline');
        const timelineLine = timeline.querySelector('.timeline-line');
        
        if (timelineLine) {
            const items = timeline.querySelectorAll('.timeline-item.is-visible');
            if (items.length > 0) {
                const lastItem = items[items.length - 1];
                const timelineTop = timeline.offsetTop;
                const itemBottom = lastItem.offsetTop + lastItem.offsetHeight;
                const lineHeight = itemBottom - timelineTop;
                
                timelineLine.style.height = lineHeight + 'px';
            }
        }
    }
    
    // Mettre à jour au scroll pour animation fluide
    let ticking = false;
    window.addEventListener('scroll', function() {
        if (!ticking) {
            window.requestAnimationFrame(function() {
                timelineItems.forEach(item => {
                    if (item.classList.contains('is-visible')) {
                        updateTimelineLine(item);
                    }
                });
                ticking = false;
            });
            ticking = true;
        }
    });
});
