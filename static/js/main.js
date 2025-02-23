$(document).ready(function() {
    // Navigation Toggle
    $('.nav-toggle').click(function() {
        $('.nav-links').toggleClass('active');
    });

    // Smooth Scrolling
    $('.nav-link').click(function(e) {
        if (this.hash !== '') {
            e.preventDefault();
            const hash = this.hash;
            $('html, body').animate({
                scrollTop: $(hash).offset().top - 70
            }, 800);
        }
    });

    // Project Filtering
    $('.filter-btn').click(function() {
        const category = $(this).data('filter');
        
        $('.filter-btn').removeClass('active');
        $(this).addClass('active');

        if (category === 'all') {
            $('.project-card').show();
        } else {
            $('.project-card').hide();
            $(`.project-card[data-category="${category}"]`).show();
        }
    });

    // Contact Form Submission
    $('#contact-form').submit(function(e) {
        e.preventDefault();
        
        $.ajax({
            url: $(this).attr('action'),
            type: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                if (response.status === 'success') {
                    alert('Message sent successfully!');
                    $('#contact-form')[0].reset();
                }
            },
            error: function() {
                alert('An error occurred. Please try again.');
            }
        });
    });

    // Animations on Scroll
    $(window).scroll(function() {
        $('.animate-on-scroll').each(function() {
            const elementTop = $(this).offset().top;
            const windowBottom = $(window).scrollTop() + $(window).height();

            if (windowBottom > elementTop) {
                $(this).addClass('animate__animated animate__fadeInUp');
            }
        });
    });
});

// Add this to your main.js or in a script tag
document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });

    // Image preview zoom
    const certImages = document.querySelectorAll('.certificate-image img');
    certImages.forEach(img => {
        img.addEventListener('mousemove', function(e) {
            const x = e.clientX - e.target.offsetLeft;
            const y = e.clientY - e.target.offsetTop;
            
            e.target.style.transformOrigin = `${x}px ${y}px`;
            e.target.style.transform = 'scale(1.5)';
        });

        img.addEventListener('mouseleave', function(e) {
            e.target.style.transform = 'scale(1)';
        });
    });

    // Filter certificates
    const filterButtons = document.querySelectorAll('.filter-btn');
    filterButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            const category = this.dataset.filter;
            const cards = document.querySelectorAll('.certificate-card');

            cards.forEach(card => {
                if (category === 'all' || card.dataset.category === category) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });

            // Update active filter
            filterButtons.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
        });
    });
});