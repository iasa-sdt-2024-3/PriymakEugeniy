class App:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def run(self):
        return 100

    def close(self):
        return 100

class DesktopApp(App):
    def __init__(self, name, version, platform):
        super().__init__(name, version)
        self.platform = platform

    def minimize(self):
        return 100

    def maximize(self):
        return 100

class WebApp(App):
    def __init__(self, name, version, url):
        super().__init__(name, version)
        self.url = url

    def navigate(self, url):
        return 100

    def refresh(self):
        return 100

desktop_app = DesktopApp("TEST1", "1.0", "Windows 11")
web_app = WebApp("TEST2", "1.0", "https://test.com")

print("Desktop App:")
print(f"Name: {desktop_app.name}")
print(f"Version: {desktop_app.version}")
print(f"Platform: {desktop_app.platform}")

print("\nWeb App:")
print(f"Name: {web_app.name}")
print(f"Version: {web_app.version}")
print(f"URL: {web_app.url}")