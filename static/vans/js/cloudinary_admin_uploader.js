// Global function to open Cloudinary upload widget
function openCloudinaryWidget(inputId) {
    // Ensure the input exists
    const input = document.getElementById(inputId);
    if (!input) {
        console.error(`Input with ID "${inputId}" not found.`);
        return;
    }

    const cloudName = input.dataset.cloudName;
    const uploadPreset = input.dataset.uploadPreset;

    // Initialize currentImages safely
    let currentImages = [];
    try {
        currentImages = JSON.parse(input.value || '[]');
        if (!Array.isArray(currentImages)) currentImages = [];
    } catch (e) {
        currentImages = [];
    }

    // Open Cloudinary widget
    cloudinary.openUploadWidget({
        cloudName: cloudName,
        uploadPreset: uploadPreset,
        sources: ['local', 'url', 'camera'],
        multiple: true,
        maxFiles: 10,
        folder: 'vans',
        clientAllowedFormats: ['jpg', 'jpeg', 'png', 'gif', 'webp'],
        maxFileSize: 5000000, // 5MB
        resourceType: 'image',
    }, function(error, result) {
        if (!error && result && result.event === 'success') {
            const filename = `${result.info.public_id}.${result.info.format}`; // e.g. 'vans/red-auto.webp'
        
            if (!Array.isArray(currentImages)) currentImages = [];
            currentImages.push(filename);
        
            // Update hidden input
            input.value = JSON.stringify(currentImages);
        
            // Update previews
            renderPreviews(inputId, currentImages);
        }
    });
}

// Render image previews
function renderPreviews(inputId, images) {
    const previewContainer = document.getElementById('preview_' + inputId);
    
    if (!images || images.length === 0) {
        previewContainer.innerHTML = '<p class="help">No images uploaded yet.</p>';
        return;
    }
    
    previewContainer.innerHTML = images.map((url, index) => `
        <div class="cloudinary-preview-item">
            <img src="${url}" alt="Van image ${index + 1}">
            <button type="button" 
                    class="remove-image-btn" 
                    onclick="removeImage('${inputId}', ${index})"
                    title="Remove image">
                ✕
            </button>
        </div>
    `).join('');
}

// Remove image from array
function removeImage(inputId, index) {
    const input = document.getElementById(inputId);
    let images = JSON.parse(input.value || '[]');
    
    // Remove image at index
    images.splice(index, 1);
    
    // Update hidden input
    input.value = JSON.stringify(images);
    
    // Update preview
    renderPreviews(inputId, images);
}

// Initialize previews on page load
document.addEventListener('DOMContentLoaded', function() {
    // Find all Cloudinary upload widgets
    document.querySelectorAll('.cloudinary-upload-widget input[type="hidden"]').forEach(function(input) {
        const images = JSON.parse(input.value || '[]');
        renderPreviews(input.id, images);
    });
});