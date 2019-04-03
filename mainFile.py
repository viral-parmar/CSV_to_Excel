import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import pandas as pd
from Append_Function import append_df_to_excel
import os.path
import sys


class Watcher:
    def __init__(self, args):
        self.watch_dir = os.getcwd()
        print(args[0])
        self.directory_to_watch = os.path.join(self.watch_dir, args[1])
        self.observer = Observer()
        self.event_handler = Handler(patterns=["*.CSV"], ignore_patterns=["*.temp"], ignore_directories=True)
        #self.event_handler = Handler()

    def run(self):
        self.observer.schedule(self.event_handler, self.directory_to_watch, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(PatternMatchingEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print("Received created event - %s." % event.src_path)
            df = pd.read_csv(event.src_path, header=0, index_col=0)
            append_df_to_excel(os.path.join(os.getcwd(), "myfile.xlsx"), df)
        elif event.event_type == 'modified':
            # Taken any actionc here when a file is modified.
            df = pd.read_csv(event.src_path, header=0, index_col=0)
            append_df_to_excel(os.path.join(os.getcwd(), "myfile.xlsx"), df)
            print("Received modified event - %s." % event.src_path)


if __name__ == '__main__':
    print(sys.argv)
    w = Watcher(sys.argv)
    w.run()
