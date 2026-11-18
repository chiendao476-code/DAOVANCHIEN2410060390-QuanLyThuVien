# File: src/business/book_service.py
# Sinh vien thuc hien: Dao Van Chien - MSSV: 2410060390 - Lop: 24TXTHK1
class BookService:
    def __init__(self):
        self.books = []

    def add_book(self, book_id, title):
        if not book_id or not title:
            return "Loi: Ma sach va ten sach khong duoc de trong"
        self.books.append({"book_id": book_id, "title": title})
        return "Them sach thanh cong"
