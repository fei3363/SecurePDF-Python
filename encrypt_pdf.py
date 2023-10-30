import PyPDF2
import os

def encrypt_pdf(input_pdf, password):
    # 從輸入檔案路徑中提取路徑和檔案名稱
    path, filename = os.path.split(input_pdf)
    name, ext = os.path.splitext(filename)
    
    # 進行輸出檔案的名稱和路徑
    output_pdf = os.path.join(path, f"{name}_encrypted{ext}")

    # 進行 PDF 讀取物件
    with open(input_pdf, "rb") as file:
        pdf = PyPDF2.PdfReader(file)

        # 檢查PDF是否已加密
        if pdf.is_encrypted:
            print("PDF already encrypted.")
            return

        # 進行PDF寫入物件
        pdf_writer = PyPDF2.PdfWriter()

        # 複製每一頁到寫入物件
        for page in pdf.pages:
            pdf_writer.add_page(page)
        
        # 加密PDF
        pdf_writer.encrypt(password)

        # 寫入加密的PDF到新檔案
        with open(output_pdf, "wb") as output_file_handle:
            pdf_writer.write(output_file_handle)

    print(f"PDF encrypted! Saved as {output_pdf}")

# 使用者輸入
input_file = input("Enter the file path of the PDF: ")
password = input("Enter the password to encrypt the PDF: ")

# 執行加密功能
encrypt_pdf(input_file, password)

