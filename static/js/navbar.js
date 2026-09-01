document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.getElementById('menuToggle');
    const navLinks = document.getElementById('navLinks');

    // Safe Guard Check: Ensure element exist in DOM before binding logic
    if (!menuToggle || !navLinks) return;

    // --- Active Link Highlight Logic ---
    const currentPath = window.location.pathname;
    const allLinks = document.querySelectorAll('.nav-links a');

    allLinks.forEach(link => {
        const linkPath = link.getAttribute('href');
        
        // Fixed Match Logic: Stop the homepage link "/" from accidentally matching sub-routes like "/blog"
        if (linkPath === '/' && currentPath === '/') {
            link.classList.add('active-link');
        } else if (linkPath !== '/' && linkPath !== '#' && currentPath.startsWith(linkPath)) {
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

    // Close the menu is a user clicks an internal link inside menu
    navLinks.addEventListener('click', (event) => {
        if (event.target.tagName === 'A'){
            menuToggle.classList.remove('active');
            navLinks.classList.remove('active');
        }
    })

    // Automatically close the menu if the user clicks anywhere outside of it
    document.addEventListener('click', (event) => {
        if (!navLinks.contains(event.target) && !menuToggle.contains(event.target)) {
            menuToggle.classList.remove('active');
            navLinks.classList.remove('active');
        }
    });
});