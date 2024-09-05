import logging
from pathlib import Path

class EventStore:
    _instance = None

    def __new__(cls, log_file="event_store.log"):
        if cls._instance is None:
            cls._instance = super(EventStore, cls).__new__(cls)
            cls._instance.initialize(log_file)
        return cls._instance

    def initialize(self, log_file):
        # Initialize the logger
        self.logger = logging.getLogger("EventStoreLogger")
        self.logger.setLevel(logging.INFO)

        # Ensure log directory exists
        log_dir = Path(log_file).parent
        log_dir.mkdir(parents=True, exist_ok=True)

        # Create a file handler for logging to a file
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)

        # Create a logging format
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Add the handler to the logger
        self.logger.addHandler(file_handler)

        # Optionally keep events in memory (can be useful for quick access)
        self.events = []

    def save(self, event):
        self.events.append(event)
        self.logger.info(f"Event saved: {event}")

    def get_all_events(self):
        return self.events

    def get_events_by_function(self, function_name):
        return [event for event in self.events if event.get('function_name') == function_name]
