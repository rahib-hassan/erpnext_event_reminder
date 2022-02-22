# Event Reminder Notification for ERPNEXT

This is a Frappe/ERPNext app that implements:
- Send desk notification reminders to users for calendar events.
- How many minutes before the reminder should be send can be configured per event.

## Steps to Install
1. Install this app to your Frappe/ERPNext instance. [(refer)](https://frappeframework.com/docs/v13/user/en/basics/apps#installing-an-app-into-a-site)
2. Run `bench migrate` command, so that the required custom fields are created. 
3. New field for reminder will be created in the "New Event" form. 

#### License

MIT
