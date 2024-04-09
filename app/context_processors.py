def get_dashbord_url(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            dashboard_url = 'super_dashboard'
        elif request.user.is_staff:
            dashboard_url = 'staff_dashboard'
        else:
            dashboard_url = 'dashboard'
    else:
        dashboard_url = None
    
    return {'dashboard_url': dashboard_url}