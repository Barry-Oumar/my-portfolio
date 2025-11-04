/**
 * CUSTOM CURSOR EFFECT
 * Crée un curseur personnalisé avec animation fluide
 * Grossit au survol d'éléments cliquables
 */

document.addEventListener('DOMContentLoaded', function() {
    const cursor = document.getElementById('custom-cursor');
    const cursorDot = document.getElementById('custom-cursor-dot');
    
    // Activer seulement sur desktop
    if (window.innerWidth > 768) {
        // Suivre les mouvements de la souris
        document.addEventListener('mousemove', function(e) {
            // Mettre à jour la position avec animation fluide
            requestAnimationFrame(() => {
                cursor.style.left = e.clientX + 'px';
                cursor.style.top = e.clientY + 'px';
                cursorDot.style.left = e.clientX + 'px';
                cursorDot.style.top = e.clientY + 'px';
            });
        });
        
        // Détecter les éléments survolables
        const hoverElements = document.querySelectorAll('a, button, .btn, .card, input, textarea, select');
        
        hoverElements.forEach(element => {
            element.addEventListener('mouseenter', function() {
                document.body.classList.add('cursor-hover');
            });
            
            element.addEventListener('mouseleave', function() {
                document.body.classList.remove('cursor-hover');
            });
        });
    }
});
