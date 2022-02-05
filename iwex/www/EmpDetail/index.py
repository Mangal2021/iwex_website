import frappe

def get_context(context):
    context.employee = frappe.get_doc("CompanyEmployeeDetail","868f86e75a")
    return context