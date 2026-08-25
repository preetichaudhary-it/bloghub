document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.getElementById('menuToggle');
    const navLinks = document.getElementById('navLinks');

     // --- Active Link Highlight Logic ---
    const currentPath = window.location.pathname;
    const allLinks = document.querySelectorAll('.nav-links a');

    allLinks.forEach(link => {
        // Get the path from the href attribute (e.g., "/" or "/about")
        const linkPath = link.getAttribute('href');
        
        // Match exact homepage path or check if sub-paths match
        if (currentPath === linkPath || (linkPath !== '/' && currentPath.startsWith(linkPath))) {
            link.classList.add('active-link');
        }
    });
    // ------------------------------------

    // Toggle the mobile drawer when clicking the hamburger icon
    menuToggle.addEventListener('click', (event) => {
        event.stopPropagation(); // Prevents immediate closing from the document listener below
        menuToggle.classList.toggle('active');
        navLinks.classList.toggle('active');
    });

    // Automatically close the menu if the user clicks anywhere outside of it
    document.addEventListener('click', (event) => {
        if (!navLinks.contains(event.target) && !menuToggle.contains(event.target)) {
            menuToggle.classList.remove('active');
            navLinks.classList.remove('active');
        }
    });
});