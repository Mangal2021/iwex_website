import frappe

def get_context(context):
    x = frappe.form_dict.docname;
    
    context.employee = frappe.get_doc("CompanyEmployeeDetail",x)
    return context

