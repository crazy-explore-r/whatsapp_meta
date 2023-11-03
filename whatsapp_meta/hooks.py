from . import __version__ as app_version

app_name = "whatsapp_meta"
app_title = "Whatsapp Meta"
app_publisher = "Ragul KM"
app_description = "Whatsapp Buisiness integration for Frappe"
app_email = "developer.ragul@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/whatsapp_meta/css/whatsapp_meta.css"
# app_include_js = "/assets/whatsapp_meta/js/whatsapp_meta.js"

# include js, css files in header of web template
# web_include_css = "/assets/whatsapp_meta/css/whatsapp_meta.css"
# web_include_js = "/assets/whatsapp_meta/js/whatsapp_meta.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "whatsapp_meta/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "whatsapp_meta.utils.jinja_methods",
#	"filters": "whatsapp_meta.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "whatsapp_meta.install.before_install"
# after_install = "whatsapp_meta.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "whatsapp_meta.uninstall.before_uninstall"
# after_uninstall = "whatsapp_meta.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "whatsapp_meta.utils.before_app_install"
# after_app_install = "whatsapp_meta.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "whatsapp_meta.utils.before_app_uninstall"
# after_app_uninstall = "whatsapp_meta.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "whatsapp_meta.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Notification": "whatsapp_meta.whatsapp_meta.overrides.notification.SendNotification"
}

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Contact": {
		"validate": "whatsapp_meta.whatsapp_meta.docevents.contact_validate",
	},
	"User": {
		"after_insert" : "whatsapp_meta.whatsapp_meta.docevents.user_after_insert"
	}
}

fixtures = ["Property Setter"]

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"whatsapp_meta.tasks.all"
#	],
#	"daily": [
#		"whatsapp_meta.tasks.daily"
#	],
#	"hourly": [
#		"whatsapp_meta.tasks.hourly"
#	],
#	"weekly": [
#		"whatsapp_meta.tasks.weekly"
#	],
#	"monthly": [
#		"whatsapp_meta.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "whatsapp_meta.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "whatsapp_meta.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "whatsapp_meta.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["whatsapp_meta.utils.before_request"]
# after_request = ["whatsapp_meta.utils.after_request"]

# Job Events
# ----------
# before_job = ["whatsapp_meta.utils.before_job"]
# after_job = ["whatsapp_meta.utils.after_job"]

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"whatsapp_meta.auth.validate"
# ]
