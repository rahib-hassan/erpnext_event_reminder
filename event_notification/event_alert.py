import frappe
from frappe.utils import now
from datetime import datetime, timedelta
from frappe import enqueue

def notification_log(event):
    notification = frappe.get_doc({
        "doctype": "Notification Log", "subject": event.subject, "for_user": event.owner,\
        "type": "Alert", "email_content": event.description, "document_type": "Event",\
        "document_name": event.name})

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
                enqueue(notification_log, now=False, queue="default")
                notification_log(event)
                event.alert_sent = 1
                event.save()
