/**
 * PROJECT FILTERING SYSTEM
 * Filtre les projets basé sur les tags de technologie
 * Transitions fade in/out fluides
 */

document.addEventListener('DOMContentLoaded', function() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectItems = document.querySelectorAll('.project-item');
    
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const filterValue = this.getAttribute('data-filter');
            
            // Mettre à jour le bouton actif
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            
            // Filtrer les projets
            filterProjects(filterValue);
        });
    });
    
    function filterProjects(filter) {
        projectItems.forEach(item => {
            const technologies = item.getAttribute('data-technologies');
            
            if (filter === 'all') {
                // Afficher tous les projets
                item.classList.remove('hidden');
                setTimeout(() => {
                    item.style.opacity = '1';
                    item.style.transform = 'scale(1)';
                }, 10);
            } else {
                // Vérifier si le projet contient la technologie filtrée
                if (technologies.includes(filter)) {
                    item.classList.remove('hidden');
                    setTimeout(() => {
                        item.style.opacity = '1';
                        item.style.transform = 'scale(1)';
                    }, 10);
                } else {
                    item.style.opacity = '0';
                    item.style.transform = 'scale(0.8)';
                    setTimeout(() => {
                        item.classList.add('hidden');
                    }, 400);
                }
            }
        });
    }
});
