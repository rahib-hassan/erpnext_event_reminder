import frappe
from frappe.utils import now
from datetime import datetime, timedelta
from frappe import enqueue

def get_participants(doc):
    users = []
    participants = doc.event_participants
    for participant in participants:
        if participant.reference_doctype == "Employee":
            user_id = frappe.db.get_value('Employee', {'full_name': participant.reference_docname}, ['user_id'])
            users.append(user_id)
    return users

def notification_log(doc):
    subject = (f'"{doc.subject}" starts in {doc.alert_time} minutes')
    
    users = get_participants(doc)
    users.append(doc.owner)
    for user in users:
        notification = frappe.get_doc({
            "doctype": "Notification Log", "subject": subject, "for_user": doc.owner,\
            "type": "Alert", "email_content": doc.description, "document_type": "Event",\
            "document_name": doc.name})

        notification.insert()


def send_notification():
    # frappe.logger().debug("Logged send notification method")
    events = frappe.db.get_all("Event", fields=["*"])
    for event in events:
        event = frappe.get_doc("Event", event.name)
        if event.alert_sent == 0 and event.alert_time:
            alert_time = event.starts_on - timedelta(minutes=event.alert_time)
            cur_time = datetime.strptime(now(), '%Y-%m-%d %H:%M:%S.%f')
            if cur_time >= alert_time and cur_time <= event.starts_on:
                enqueue(notification_log, now=False, queue="default", doc=event)
                event.alert_sent = 1
                event.save()


