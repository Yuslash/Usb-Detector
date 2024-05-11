from plyer import notification
import wmi


def send(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,
        timeout=10,
    )


def monitor_usb_events():
    c = wmi.WMI()
    watcher = c.Win32_USBControllerDevice.watch_for("creation")
    print("Monitoring USB device connections...")

    for usb_event in iter(watcher, None):
        print("USB Connected!", usb_event)
        send("Hi keerthivasan", "Hi keerthi vasan some one is intrude")
        break


if __name__ == "__main__":
    monitor_usb_events()
