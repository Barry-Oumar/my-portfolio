/**
 * DARK MODE TOGGLE
 * Bascule entre thèmes clair et sombre
 * Persiste la préférence utilisateur dans localStorage
 */

document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');
    const body = document.body;
    
    // Vérifier la préférence sauvegardée ou utiliser le mode clair par défaut
    const currentTheme = localStorage.getItem('theme') || 'light';
    
    // Appliquer le thème sauvegardé au chargement
    if (currentTheme === 'dark') {
        body.classList.add('dark-mode');
        updateIcon(true);
    }
    
    // Basculer le thème au clic
    themeToggle.addEventListener('click', function() {
        body.classList.toggle('dark-mode');
        
        // Sauvegarder la préférence
        const isDarkMode = body.classList.contains('dark-mode');
        localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
        
        // Mettre à jour l'icône
        updateIcon(isDarkMode);
        
        // Animation de rotation
        this.style.transform = 'rotate(360deg)';
        setTimeout(() => {
            this.style.transform = 'rotate(0deg)';
        }, 300);
    });
    
    // Fonction pour mettre à jour l'icône
    function updateIcon(isDark) {
        if (isDark) {
            themeIcon.classList.remove('bi-moon-stars');
            themeIcon.classList.add('bi-sun-fill');
        } else {
            themeIcon.classList.remove('bi-sun-fill');
            themeIcon.classList.add('bi-moon-stars');
        }
    }
});
