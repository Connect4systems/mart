from . import __version__ as app_version

app_name = "mart"
app_title = "Mart"
app_publisher = "Mart Team"
app_description = "Custom app template for Frappe v16 and ERPNext v16"
app_email = "dev@example.com"
app_license = "MIT"

required_apps = ["erpnext"]

# Includes in <head>
# ------------------
# app_include_css = "/assets/mart/css/mart.css"
# app_include_js = "/assets/mart/js/mart.js"

# Home Pages
# ----------
# role_home_page = {
#     "Role": "home_page"
# }

# Website user home page (by Role)
# role_home_page = {
#     "Role": "home_page"
# }

# Generators
# ----------
# website_generators = ["Web Page"]

# Installation
# ------------
# before_install = "mart.install.before_install"
# after_install = "mart.install.after_install"

# Desk Notifications
# ------------------
# notification_config = "mart.notifications.get_notification_config"

# Permissions
# -----------
# permission_query_conditions = {
#     "Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#     "Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# doc_events = {
#     "*": {
#         "on_update": "method",
#         "on_cancel": "method",
#         "on_trash": "method"
#     }
# }

# Scheduled Tasks
# ---------------
# scheduler_events = {
#     "all": [
#         "mart.tasks.all"
#     ],
#     "daily": [
#         "mart.tasks.daily"
#     ],
# }

# Testing
# -------
# before_tests = "mart.install.before_tests"
