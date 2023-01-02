from model import Contact, PhoneBook
from pathlib import Path

class Controller:
    def __init__(self,phone_book: PhoneBook) -> None:
        self._book=phone_book

    def add_contact(self,contact: str)->None:
        s=contact.split()
        if len(s) != 3:
            raise ValueError
        self._book.add_contact(Contact(s[0],s[1],s[2]))

    def all_contacts(self)->list[str]:
        return [str(i) for i in self._book.get_all_contacts()]

    def contacts_by_fullname(self,fullname: str)->list[str]:
        fname=fullname.split()
        if len(fname) != 2:
            raise ValueError
        return [str(i) for i in self._book.get_contacts_by_surname_and_name(fname[0],fname[1])]
    
    def contacts_by_surname(self,surname: str)->list[str]:
        return [str(i) for i in self._book.get_contacts_by_surname(surname)]

    def contacts_by_name(self,name: str)->list[str]:
        return [str(i) for i in self._book.get_contacts_by_name(name)]

    def contacts_by_phone(self,phone: str)->list[str]:
        return [str(i) for i in self._book.get_contacts_by_phone(phone)]

    def import_from_txt(self,file: str) -> None:
        self._book.import_from_txt(Path(file))

    def import_from_csv(self,file: str) -> None:
        self._book.import_from_csv(Path(file))

    def export_to_txt(self,file: str) -> None:
        self._book.export_to_txt(Path(file))

    def export_to_csv(self,file: str) -> None:
        self._book.export_to_csv(Path(file))