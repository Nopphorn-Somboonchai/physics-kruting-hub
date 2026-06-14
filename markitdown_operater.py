from markitdown import MarkItDown

# 1. เปิดใช้งานระบบปลั๊กอินให้เป็น True เหมือนระบบใหญ่
md = MarkItDown(enable_plugins=True) 

# 2. แปลงไฟล์
result = md.convert("sample.pdf")

# 3. เวลาบันทึกไฟล์ ต้องระบุ encoding="utf-8" เพื่อป้องกันภาษาและสัญลักษณ์เพี้ยน
with open("exam.md", "w", encoding="utf-8") as f:
    f.write(result.text_content)

print("แปลงไฟล์เสร็จสมบูรณ์!")