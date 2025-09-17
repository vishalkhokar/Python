from pypdf import PdfReader
import os

def readPddf():
    base_dir = os.path.dirname(__file__)  
    pdf_path=os.path.join(base_dir,"train_info.pdf")
    reader=PdfReader(pdf_path)
    print(type(reader))
    print(len(reader.pages))

    texts=[]
    for i in reader.pages:
      content =  i.extract_text()
      if content:
          texts.append(content)
             
    return texts