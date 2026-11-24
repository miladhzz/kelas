import threading
from datetime import datetime


class Logger:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        # قفل برای جلوگیری از ساخت همزمان دو نمونه
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._initialized = False
        return cls._instance

    def __init__(self, filename="app.log"):
        # جلوگیری از مقداردهی دوباره هنگام ساخت نمونه‌های بعدی
        if self._initialized:
            return
        self.filename = filename
        self._file = open(filename, "a", encoding="utf-8")
        self._initialized = True

    def log(self, level, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{timestamp}] [{level}] {message}\n"
        self._file.write(line)
        self._file.flush()
        print(line.strip())  # نمایش در کنسول

    def info(self, msg):
        self.log("INFO", msg)

    def error(self, msg):
        self.log("ERROR", msg)

    def close(self):
        if self._file and not self._file.closed:
            self._file.close()


a = Logger()
print(a)

b = Logger()
print(b)