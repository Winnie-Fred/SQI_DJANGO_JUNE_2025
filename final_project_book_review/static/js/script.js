
// Mobile Navigation
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');

    if (hamburger && navMenu) {
        hamburger.addEventListener('click', function() {
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
        });

        // Close menu when clicking on a link
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });
    }

    // Search functionality
    const searchInput = document.querySelector('.search-bar input');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            // Add search logic here
            console.log('Searching for:', searchTerm);
        });
    }

    // Filter functionality
    const filterSelects = document.querySelectorAll('.filter-select');
    filterSelects.forEach(select => {
        select.addEventListener('change', function() {
            const filterValue = this.value;
            const filterType = this.querySelector('option').textContent.includes('Genre') ? 'genre' : 'sort';
            console.log(`Filter ${filterType}:`, filterValue);
            // Add filter logic here
        });
    });

    // Modal functionality
    const modal = document.getElementById('writeReviewModal');
    const writeReviewBtn = document.querySelector('.write-review-btn');
    const closeModal = document.querySelector('.close-modal');

    if (writeReviewBtn && modal) {
        writeReviewBtn.addEventListener('click', function() {
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        });
    }

    if (closeModal && modal) {
        closeModal.addEventListener('click', function() {
            modal.classList.remove('active');
            document.body.style.overflow = 'auto';
        });
    }

    // Close modal when clicking outside
    if (modal) {
        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                modal.classList.remove('active');
                document.body.style.overflow = 'auto';
            }
        });
    }

    // Star rating functionality
    const starRating = document.querySelector('.star-rating');
    if (starRating) {
        const stars = starRating.querySelectorAll('i');
        let currentRating = 0;

        stars.forEach((star, index) => {
            star.addEventListener('mouseover', function() {
                highlightStars(index + 1);
            });

            star.addEventListener('click', function() {
                currentRating = index + 1;
                setRating(currentRating);
            });
        });

        starRating.addEventListener('mouseleave', function() {
            setRating(currentRating);
        });

        function highlightStars(rating) {
            stars.forEach((star, index) => {
                if (index < rating) {
                    star.classList.remove('far');
                    star.classList.add('fas');
                    star.classList.add('selected-rating');
                    
                } else {
                    star.classList.remove('fas');
                    star.classList.add('far');
                    star.classList.remove('selected-rating');

                }
            });
        }

        function setRating(rating) {
            const ratingInput = document.getElementById('ratingInput');
            highlightStars(rating);
            ratingInput.value = rating;
        }
    }

    // Password toggle functionality
    const passwordToggles = document.querySelectorAll('.password-toggle');
    passwordToggles.forEach(toggle => {
        toggle.addEventListener('click', function() {
            const passwordInput = this.parentNode.querySelector('input');
            const icon = this.querySelector('i');
            
            if (passwordInput.type === 'password') {
                passwordInput.type = 'text';
                icon.classList.remove('fa-eye');
                icon.classList.add('fa-eye-slash');
            } else {
                passwordInput.type = 'password';
                icon.classList.remove('fa-eye-slash');
                icon.classList.add('fa-eye');
            }
        });
    });

    // Password strength indicator
    const passwordInput = document.getElementById('password');
    if (passwordInput) {
        passwordInput.addEventListener('input', function() {
            const password = this.value;
            const strengthBar = document.querySelector('.strength-fill');
            const strengthText = document.querySelector('.strength-text span');

            if (strengthBar && strengthText) {
                const strength = calculatePasswordStrength(password);
                updatePasswordStrength(strength, strengthBar, strengthText);
            }
        });
    }

    function calculatePasswordStrength(password) {
        let strength = 0;
        
        if (password.length >= 8) strength += 1;
        if (/[a-z]/.test(password)) strength += 1;
        if (/[A-Z]/.test(password)) strength += 1;
        if (/[0-9]/.test(password)) strength += 1;
        if (/[^A-Za-z0-9]/.test(password)) strength += 1;

        return strength;
    }

    function updatePasswordStrength(strength, strengthBar, strengthText) {
        const colors = ['#ef4444', '#f97316', '#eab308', '#22c55e', '#10b981'];
        const labels = ['Very Weak', 'Weak', 'Fair', 'Good', 'Strong'];
        const widths = ['20%', '40%', '60%', '80%', '100%'];

        strengthBar.style.backgroundColor = colors[strength - 1] || '#ef4444';
        strengthBar.style.width = widths[strength - 1] || '0%';
        strengthText.textContent = labels[strength - 1] || 'Very Weak';
    }

    
    function showError(message) {
        // Create or update error message
        let errorDiv = document.querySelector('.error-message');
        if (!errorDiv) {
            errorDiv = document.createElement('div');
            errorDiv.className = 'error-message';
            errorDiv.style.cssText = `
                background: #fee2e2;
                color: #dc2626;
                padding: 1rem;
                border-radius: 0.5rem;
                margin-bottom: 1rem;
                border: 1px solid #fecaca;
            `;
            document.querySelector('.auth-form').prepend(errorDiv);
        }
        errorDiv.textContent = message;

        // Remove error after 5 seconds
        setTimeout(() => {
            if (errorDiv.parentNode) {
                errorDiv.remove();
            }
        }, 5000);
    }

    // // Review form functionality
    // const reviewForm = document.querySelector('.review-form');
    // if (reviewForm) {
    //     reviewForm.addEventListener('submit', function(e) {
    //         e.preventDefault();
            
    //         const formData = new FormData(this);
    //         const reviewData = {
    //             rating: document.querySelectorAll('.star-rating .fas').length,
    //             title: formData.get('title') || document.getElementById('reviewTitle')?.value,
    //             content: formData.get('content') || document.getElementById('reviewContent')?.value
    //         };

    //         if (reviewData.rating === 0) {
    //             alert('Please select a rating');
    //             return;
    //         }

    //         if (!reviewData.content) {
    //             alert('Please fill in all fields');
    //             return;
    //         }

    //         // Simulate review submission
    //         alert('Review submitted successfully! (This is a demo)');
            
    //         // Close modal
    //         const modal = document.getElementById('writeReviewModal');
    //         if (modal) {
    //             modal.classList.remove('active');
    //             document.body.style.overflow = 'auto';
    //         }

    //         // Reset form
    //         this.reset();
    //         document.querySelectorAll('.star-rating i').forEach(star => {
    //             star.classList.remove('fas');
    //             star.classList.add('far');
    //         });
    //     });
    // }

    // Pagination functionality
    const pageNumbers = document.querySelectorAll('.page-number');
    pageNumbers.forEach(pageNumber => {
        pageNumber.addEventListener('click', function() {
            if (!this.classList.contains('active')) {
                // Remove active class from all page numbers
                pageNumbers.forEach(pn => pn.classList.remove('active'));
                // Add active class to clicked page number
                this.classList.add('active');
                
                // Simulate page load
                console.log('Loading page:', this.textContent);
            }
        });
    });

    // Helpful review buttons
    const helpfulBtns = document.querySelectorAll('.action-btn');
    helpfulBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            if (this.innerHTML.includes('Helpful')) {
                // Simulate helpful vote
                const currentCount = parseInt(this.textContent.match(/\d+/)[0]);
                this.innerHTML = this.innerHTML.replace(/\(\d+\)/, `(${currentCount + 1})`);
                this.style.color = '#2563eb';
            }
        });
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add animation classes to elements when they come into view
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, observerOptions);

    // Observe elements for animation
    document.querySelectorAll('.feature-card, .book-card, .review-card').forEach(el => {
        observer.observe(el);
    });

    // Add loading states to buttons
    document.querySelectorAll('.btn').forEach(btn => {
        btn.addEventListener('click', function() {
            if (this.type === 'submit' && !this.dataset.originalText) {
                this.dataset.originalText = this.innerHTML;
            }
        });
    });

    // Image lazy loading fallback for older browsers
    if ('loading' in HTMLImageElement.prototype) {
        const images = document.querySelectorAll('img[data-src]');
        images.forEach(img => {
            img.src = img.dataset.src;
        });
    } else {
        // Fallback for browsers that don't support lazy loading
        const script = document.createElement('script');
        script.src = 'https://polyfill.io/v3/polyfill.min.js?features=IntersectionObserver';
        document.head.appendChild(script);
    }
});

// Utility functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Export functions for potential use by Django templates
window.BookReview = {
    showError: function(message) {
        // This can be called from Django templates to show errors
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message fade-in';
        errorDiv.style.cssText = `
            position: fixed;
            top: 100px;
            right: 20px;
            background: #fee2e2;
            color: #dc2626;
            padding: 1rem 1.5rem;
            border-radius: 0.5rem;
            border: 1px solid #fecaca;
            z-index: 9999;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        `;
        errorDiv.textContent = message;
        document.body.appendChild(errorDiv);

        setTimeout(() => {
            if (errorDiv.parentNode) {
                errorDiv.remove();
            }
        }, 5000);
    },
    
    showSuccess: function(message) {
        // This can be called from Django templates to show success messages
        const successDiv = document.createElement('div');
        successDiv.className = 'success-message fade-in';
        successDiv.style.cssText = `
            position: fixed;
            top: 100px;
            right: 20px;
            background: #dcfce7;
            color: #166534;
            padding: 1rem 1.5rem;
            border-radius: 0.5rem;
            border: 1px solid #bbf7d0;
            z-index: 9999;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        `;
        successDiv.textContent = message;
        document.body.appendChild(successDiv);

        setTimeout(() => {
            if (successDiv.parentNode) {
                successDiv.remove();
            }
        }, 5000);
    }
};
