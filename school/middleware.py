class SecurityHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Security Hardening Headers
        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'DENY'
        response['X-XSS-Protection'] = '1; mode=block'
        response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        response['Permissions-Policy'] = 'camera=(), microphone=(), geolocation=()'
        
        # Content Security Policy (Optimized for Modern PWA, CDNs, Fonts, Unfold CMS)
        csp_directives = [
            "default-src 'self'",
            "script-src 'self' 'unsafe-inline' 'unsafe-eval' https://cdn.jsdelivr.net https://cdnjs.cloudflare.com https://unpkg.com",
            "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdn.jsdelivr.net https://cdnjs.cloudflare.com https://unpkg.com",
            "font-src 'self' https://fonts.gstatic.com https://cdn.jsdelivr.net https://cdnjs.cloudflare.com",
            "img-src 'self' data: blob: https://images.unsplash.com https://plus.unsplash.com https://*.ngrok-free.app https://*.ngrok.io",
            "connect-src 'self' https://*.ngrok-free.app https://*.ngrok.io wss: https:",
            "manifest-src 'self'",
            "worker-src 'self' blob:",
        ]
        response['Content-Security-Policy'] = "; ".join(csp_directives)
        
        return response
