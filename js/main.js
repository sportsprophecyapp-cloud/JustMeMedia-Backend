// Navbar scroll effect
const nav = document.getElementById('navbar');
window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 60);
});

// Mobile menu
const toggle = document.getElementById('mobile-toggle');
const mobileMenu = document.getElementById('mobile-menu');
toggle.addEventListener('click', () => mobileMenu.classList.toggle('open'));
document.querySelectorAll('.mobile-link').forEach(link => {
    link.addEventListener('click', () => mobileMenu.classList.remove('open'));
});

// Scroll reveal
const reveals = document.querySelectorAll('.scroll-reveal');
const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
        if (entry.isIntersecting) {
            setTimeout(() => entry.target.classList.add('visible'), i * 80);
            observer.unobserve(entry.target);
        }
    });
}, { threshold: 0.1, rootMargin: '0px 0px -60px 0px' });
reveals.forEach(el => observer.observe(el));

// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
        const target = document.querySelector(a.getAttribute('href'));
        if (target) { e.preventDefault(); window.scrollTo({ top: target.offsetTop - 76, behavior: 'smooth' }); }
    });
});

// Contact form
const contactForm = document.getElementById('contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const btn = document.getElementById('submit-btn');
        const btnText = document.getElementById('btn-text');
        btn.disabled = true;
        btnText.textContent = 'Sending…';

        const formData = new FormData(contactForm);
        const jsonData = Object.fromEntries(formData.entries());
        
        fetch("/api/contact", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(jsonData),
        })
        .then(res => res.json())
        .then((data) => {
            if (data.status === 'ok') {
                contactForm.style.display = 'none';
                document.getElementById('form-success').classList.add('show');
            } else {
                throw new Error(data.message || 'Error sending message');
            }
        })
        .catch((error) => {
            console.error('Form submission error:', error);
            btn.disabled = false;
            btnText.textContent = 'Send Message';
            alert('There was an error sending your message. Please try again or email directly.');
        });
    });
}

// Partner form
const partnerForm = document.getElementById('partner-form');
if (partnerForm) {
    partnerForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const btn = partnerForm.querySelector('button[type="submit"]');
        const originalText = btn.textContent;
        btn.disabled = true;
        btn.textContent = 'Submitting...';

        const formData = new FormData(partnerForm);
        // Map message to strategy to match the backend expectation
        const jsonData = {
            name: formData.get('name'),
            email: formData.get('email'),
            role: formData.get('role'),
            strategy: formData.get('message')
        };
        
        fetch("/api/partners", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(jsonData),
        })
        .then(res => res.json())
        .then((data) => {
            if (data.status === 'ok') {
                partnerForm.style.display = 'none';
                const successDiv = document.getElementById('partner-success');
                if (successDiv) successDiv.style.display = 'block';
            } else {
                throw new Error(data.message || 'Error submitting application');
            }
        })
        .catch((error) => {
            console.error('Form submission error:', error);
            btn.disabled = false;
            btn.textContent = originalText;
            alert('There was an error submitting your application. Please try again or email directly.');
        });
    });
}
