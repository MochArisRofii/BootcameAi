from crewai import Task
from Llms import GPTLlm
from Agents import *

class Tasks:
    def __init__(self, topik):
        self.topik = topik
        
        
        def cari_informasi(self):
            return Task(
                deskription="Mencari informasi tentang topik tertentu",
                expected_output="Informasi yang diinginkan",
                agent=Agents().tren_searcher(), 
            )
        def buat_blog(self):
            return Task(
                deskription="Membuat blog tentang topik tertentu",
                expected_output="Blog yang diinginkan",
                agent=Agents().penulis(),
            )
            
