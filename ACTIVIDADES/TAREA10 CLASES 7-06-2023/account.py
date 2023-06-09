class account:
    def __init__ (self,borrowed_books,reserved_books,returned_books,lost_books,fine_amount):
        self.__borrowed_books=borrowed_books
        self.__reserved_books=reserved_books
        self.__returned_books=returned_books
        self.__lost_books=lost_books
        self.__fine_amount=fine_amount