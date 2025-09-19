"""
Static-site mode: all admin/control backend views were removed.
Routes are now served directly via TemplateView in `handle/urls.py`.
"""

# Intentionally left minimal to avoid import errors elsewhere.