import time
import os 
import shutil	
from whatchdog.observers import Observer		
from watchdog.events import FileSystemEventHandler 

from_dir = "C:\Users\Maria Eduarda"
to_dir = 

## GERENCIA O EVENTO DE CRIAÇÃO DE UM NOVO ARQUIVO

class FileMovementHandler(FileSystemEventHandler):

	def on_created(self, event):
    
    	print(event)
      
event_handler = FileMovementHandler() ## INICIALIZA A CLASSE GERENCIADORA DE EVENTOS
    
observer = Observer()
    
observer.schedule(event_handler, from_dir, recursive=True)
    
observer.start()

while True:
	time.sleep(2)
    print("executando...")
