// ================================
// GLOBAL NAVIGATION & UTILITIES
// ================================

/**
 * Navigate to a specific page using window.location.href
 * @param {string} page - The page filename to navigate to
 */
function navigate(page) {
    const baseUrl = window.location.pathname.substring(0, window.location.pathname.lastIndexOf('/') + 1);
    window.location.href = baseUrl + page;
}

/**
 * Initialize page on load
 */
document.addEventListener('DOMContentLoaded', function() {
    initializePage();
});

/**
 * Initialize page elements and functionality
 */
function initializePage() {
    // Add smooth scroll behavior
    document.documentElement.style.scrollBehavior = 'smooth';

    // Initialize tooltips (if needed)
    initializeTooltips();

    // Add keyboard shortcuts
    initializeKeyboardShortcuts();
}

/**
 * Initialize tooltips for hover elements
 */
function initializeTooltips() {
    // Add hover effects to cards
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transition = 'all 0.3s ease';
        });
    });
}

/**
 * Initialize keyboard shortcuts
 */
function initializeKeyboardShortcuts() {
    document.addEventListener('keydown', function(event) {
        // Ctrl/Cmd + H = Home
        if ((event.ctrlKey || event.metaKey) && event.key === 'h') {
            event.preventDefault();
            navigate('index.html');
        }

        // Escape = Dashboard
        if (event.key === 'Escape') {
            navigate('dashboard.html');
        }
    });
}

/**
 * Format file size in human-readable format
 * @param {number} bytes - File size in bytes
 * @returns {string} - Formatted file size
 */
function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return Math.round((bytes / Math.pow(k, i)) * 100) / 100 + ' ' + sizes[i];
}

/**
 * Get current timestamp formatted
 * @returns {string} - Formatted timestamp
 */
function getCurrentTimestamp() {
    return new Date().toLocaleString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
    });
}

/**
 * Show toast notification (optional add-on)
 * @param {string} message - Message to display
 * @param {string} type - Type of toast (success, error, info, warning)
 * @param {number} duration - Duration in milliseconds (default: 3000)
 */
function showToast(message, type = 'info', duration = 3000) {
    const toastContainer = document.getElementById('toast-container') || createToastContainer();
    
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.style.cssText = `
        background-color: ${getToastColor(type)};
        color: white;
        padding: 16px 20px;
        border-radius: 8px;
        margin-bottom: 12px;
        animation: slideUp 0.3s ease;
        font-weight: 500;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    `;
    toast.textContent = message;
    
    toastContainer.appendChild(toast);
    
    setTimeout(() => {
        toast.style.animation = 'fadeOut 0.3s ease';
        setTimeout(() => toast.remove(), 300);
    }, duration);
}

/**
 * Get toast color based on type
 * @param {string} type - Toast type
 * @returns {string} - Color hex code
 */
function getToastColor(type) {
    const colors = {
        success: '#22C55E',
        error: '#EF4444',
        info: '#3B82F6',
        warning: '#F59E0B'
    };
    return colors[type] || colors.info;
}

/**
 * Create toast container if it doesn't exist
 * @returns {HTMLElement} - Toast container element
 */
function createToastContainer() {
    const container = document.createElement('div');
    container.id = 'toast-container';
    container.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 1000;
        pointer-events: none;
    `;
    document.body.appendChild(container);
    return container;
}

/**
 * Validate email format
 * @param {string} email - Email address to validate
 * @returns {boolean} - True if valid, false otherwise
 */
function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

/**
 * Debounce function for optimizing event handlers
 * @param {Function} func - Function to debounce
 * @param {number} wait - Wait time in milliseconds
 * @returns {Function} - Debounced function
 */
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

/**
 * Get URL parameters
 * @param {string} param - Parameter name to retrieve
 * @returns {string|null} - Parameter value or null
 */
function getUrlParam(param) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(param);
}

/**
 * Store data in localStorage with timestamp
 * @param {string} key - Storage key
 * @param {*} value - Value to store
 */
function storeData(key, value) {
    const data = {
        value: value,
        timestamp: new Date().getTime()
    };
    localStorage.setItem(key, JSON.stringify(data));
}

/**
 * Retrieve data from localStorage
 * @param {string} key - Storage key
 * @returns {*|null} - Stored value or null
 */
function retrieveData(key) {
    const data = localStorage.getItem(key);
    if (data) {
        const parsed = JSON.parse(data);
        return parsed.value;
    }
    return null;
}

/**
 * Clear specific data from localStorage
 * @param {string} key - Storage key
 */
function clearData(key) {
    localStorage.removeItem(key);
}

/**
 * Clear all data from localStorage
 */
function clearAllData() {
    localStorage.clear();
}

/**
 * Add loading state to button
 * @param {HTMLElement} button - Button element
 * @param {string} loadingText - Text to show while loading
 */
function setButtonLoading(button, loadingText = 'Loading...') {
    button.disabled = true;
    button.dataset.originalText = button.textContent;
    button.textContent = loadingText;
}

/**
 * Remove loading state from button
 * @param {HTMLElement} button - Button element
 */
function removeButtonLoading(button) {
    button.disabled = false;
    button.textContent = button.dataset.originalText || button.textContent;
}

/**
 * Initialize analytics tracking (optional)
 */
function initializeAnalytics() {
    // Track page view
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    console.log('User visited:', currentPage);
    
    // Optional: Send to analytics service
    if (window.gtag) {
        gtag('pageview', {
            'page_path': currentPage,
            'page_title': document.title
        });
    }
}

/**
 * Check device type
 * @returns {string} - Device type (mobile, tablet, desktop)
 */
function getDeviceType() {
    const userAgent = navigator.userAgent;
    if (/mobile|android|iphone|ipad|phone/i.test(userAgent)) {
        if (/ipad|tablet|android(?!.*mobile)/i.test(userAgent)) {
            return 'tablet';
        }
        return 'mobile';
    }
    return 'desktop';
}

/**
 * Enable dark mode toggle (optional add-on)
 */
function toggleDarkMode() {
    const isDarkMode = document.documentElement.getAttribute('data-theme') === 'dark';
    
    if (isDarkMode) {
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('theme', 'light');
    } else {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
    }
}

/**
 * Initialize dark mode preference
 */
function initializeDarkModePreference() {
    const savedTheme = localStorage.getItem('theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    if (savedTheme) {
        document.documentElement.setAttribute('data-theme', savedTheme);
    } else if (prefersDark) {
        document.documentElement.setAttribute('data-theme', 'dark');
    }
}

/**
 * Create a simple modal dialog
 * @param {string} title - Modal title
 * @param {string} message - Modal message
 * @param {Function} onConfirm - Callback for confirm button
 * @param {Function} onCancel - Callback for cancel button
 */
function showModal(title, message, onConfirm = null, onCancel = null) {
    const modal = document.createElement('div');
    modal.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.5);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 2000;
        animation: fadeIn 0.3s ease;
    `;

    const modalContent = document.createElement('div');
    modalContent.style.cssText = `
        background: white;
        border-radius: 16px;
        padding: 32px;
        max-width: 500px;
        width: 90%;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.2);
        animation: slideUp 0.3s ease;
    `;

    modalContent.innerHTML = `
        <h2 style="margin-top: 0; margin-bottom: 12px; color: #1F2937;">${title}</h2>
        <p style="color: #6B7280; margin-bottom: 24px;">${message}</p>
        <div style="display: flex; gap: 12px;">
            <button class="tertiary" style="flex: 1;" id="cancelBtn">Cancel</button>
            <button class="primary" style="flex: 1;" id="confirmBtn">Confirm</button>
        </div>
    `;

    modal.appendChild(modalContent);
    document.body.appendChild(modal);

    document.getElementById('confirmBtn').addEventListener('click', () => {
        modal.remove();
        if (onConfirm) onConfirm();
    });

    document.getElementById('cancelBtn').addEventListener('click', () => {
        modal.remove();
        if (onCancel) onCancel();
    });

    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.remove();
            if (onCancel) onCancel();
        }
    });
}

/**
 * Export utilities for external use
 */
window.VehicleClassifier = {
    navigate,
    showToast,
    formatFileSize,
    getCurrentTimestamp,
    validateEmail,
    debounce,
    getUrlParam,
    storeData,
    retrieveData,
    clearData,
    clearAllData,
    setButtonLoading,
    removeButtonLoading,
    toggleDarkMode,
    showModal,
    getDeviceType
};

// Initialize on page load
window.addEventListener('load', function() {
    initializePage();
    initializeAnalytics();
    initializeDarkModePreference();
});
