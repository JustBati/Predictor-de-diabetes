import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from Analisis_Server import Step1, Step2

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == "./Data/Sample.csv":
            print("\n\tDetectado cambio en Sample.csv. Ejecutando análisis...")
            Step2(lr)
            print("Análisis terminado. Resultados en Answer.csv\n")

if __name__ == "__main__":
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path='./Data/', recursive=False)
    observer.start()
    print("Iniciando servidor de análisis...\n")
    lr = Step1()

    print("\tMonitoreando cambios en Sample.csv...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
