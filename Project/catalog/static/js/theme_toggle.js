document.addEventListener('DOMContentLoaded', () => {
    const themeToggleButton = document.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('theme');
    const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');

    function setTheme(theme) {
        if (theme === 'dark') {
            document.body.classList.add('dark-mode');
            localStorage.setItem('theme', 'dark');
            if (themeToggleButton) themeToggleButton.textContent = 'Light Mode';
        } else {
            document.body.classList.remove('dark-mode');
            localStorage.setItem('theme', 'light');
            if (themeToggleButton) themeToggleButton.textContent = 'Dark Mode';
        }
    }

    // Set initial theme
    if (currentTheme) {
        setTheme(currentTheme);
    } else if (prefersDarkScheme.matches) {
        setTheme('dark');
    } else {
        setTheme('light'); // Default to light theme
    }

    if (themeToggleButton) {
        themeToggleButton.addEventListener('click', () => {
            let newTheme = localStorage.getItem('theme') === 'dark' ? 'light' : 'dark';
            setTheme(newTheme);
        });
    }

    // Listen for changes in OS theme preference
    prefersDarkScheme.addEventListener('change', (e) => {
        if (!localStorage.getItem('theme')) { // Only switch if no user override
            setTheme(e.matches ? 'dark' : 'light');
        }
    });
});
