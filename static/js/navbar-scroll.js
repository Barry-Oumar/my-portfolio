/**
 * NAVBAR SCROLL EFFECT & SCROLL PROGRESS BAR
 * Réduit la hauteur du navbar et ajoute une ombre au scroll
 * Met à jour la barre de progression basée sur la position de défilement
 */

document.addEventListener('DOMContentLoaded', function() {
    const navbar = document.getElementById('main-navbar');
    const progressBar = document.getElementById('scroll-progress-bar');
    
    // Effet de scroll sur le navbar
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        // Mettre à jour la barre de progression
        updateScrollProgress();
    });
    
    // Fonction pour mettre à jour la barre de progression
    function updateScrollProgress() {
        const windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (window.scrollY / windowHeight) * 100;
        progressBar.style.width = scrolled + '%';
    }
    
    // Appel initial
    updateScrollProgress();
});
