import frappe

def get_lead_link(lead_name, document_name):
    """
    Fetches a personalized URL for a lead by document name from Link or Personal Link doctypes.
    """
    # Check in Papermark 'Link' doctype
    url = frappe.db.get_value(
        "Link",
        {"reference_doctype": "CRM Lead", "reference_name": lead_name, "document": document_name},
        "url",
    )

    if url:
        return url

    # Check in Formbricks 'Personal Link' doctype
    url = frappe.db.get_value(
        "Personal Link",
        {"reference_doctype": "CRM Lead", "reference_name": lead_name, "survey": document_name},
        "url",
    )

    return url or "#"
