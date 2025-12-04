// ============================================================================
// FILE: static/admin/js/seo_admin.js
// ============================================================================
/* SEO Admin JavaScript enhancements */
(function($) {
    $(document).ready(function() {
        
        // Character counter for page_title
        $('#id_page_title').on('input', function() {
            var length = $(this).val().length;
            var color = length <= 60 ? 'green' : length <= 70 ? 'orange' : 'red';
            $(this).css('border-color', color);
        });
        
        // Character counter for meta_description
        $('#id_meta_description').on('input', function() {
            var length = $(this).val().length;
            var color = length <= 160 ? 'green' : 'red';
            $(this).css('border-color', color);
        });
        
        // Auto-populate Twitter fields from OG fields
        $('#id_og_title').on('blur', function() {
            if (!$('#id_twitter_title').val()) {
                $('#id_twitter_title').val($(this).val());
            }
        });
        
        $('#id_og_description').on('blur', function() {
            if (!$('#id_twitter_description').val()) {
                $('#id_twitter_description').val($(this).val());
            }
        });
        
        $('#id_og_image_url').on('blur', function() {
            if (!$('#id_twitter_image_url').val()) {
                $('#id_twitter_image_url').val($(this).val());
            }
        });
        
    });
})(django.jQuery);