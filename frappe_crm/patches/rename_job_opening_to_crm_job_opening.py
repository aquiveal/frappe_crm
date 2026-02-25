import frappe

def execute():
	if frappe.db.exists("DocType", "Job Opening"):
		frappe.rename_doc("DocType", "Job Opening", "CRM Job Opening", force=True)
