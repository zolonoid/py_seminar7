from pathlib import Path
import re

class Contact:
    def __init__(self,surname: str,name: str,phone: str) -> None:
        self._surname=surname
        self._name=name
        self._phone=phone

    def __str__(self) -> str:
        return f"{self._surname} {self._name} {self._phone}"
    
    def name(self) -> str:
        return self._name

    def surname(self) -> str:
        return self._surname

    def phone(self) -> str:
        return self._phone
    
    def is_valid(self)->bool:
        if re.fullmatch(r'^\w+$',self._surname) is None:
            return False
        if re.fullmatch(r'^\w+$',self._name) is None:
            return False
        if re.fullmatch(r'^[\d()+-]+$',self._phone) is None:
            return False
        return True


class PhoneBook:
    def __init__(self) -> None:
        self._book=[]
        self._load()

    def add_contact(self,contact: Contact,save=True)->None:
        if not contact.is_valid():
            print(f"{contact.surname()} {contact.name()} {contact.phone()}")
            raise ValueError
        self._book.append(contact)
        if save:
            self._save()

    def get_all_contacts(self)->list[Contact]:
        return self._book[:]

    def get_contacts_by_surname_and_name(self,surname: str,name: str)->list[Contact]:
        return [i for i in self._book if i.surname()==surname and i.name()==name]
    
    def get_contacts_by_surname(self,surname: str)->list[Contact]:
        return [i for i in self._book if i.surname()==surname]

    def get_contacts_by_name(self,name: str)->list[Contact]:
        return [i for i in self._book if i.name()==name]

    def get_contacts_by_phone(self,phone: str)->list[Contact]:
        return [i for i in self._book if i.phone()==phone]

    def import_from_txt(self,file: Path) -> None:
        for i in file.read_text('utf-8').split('*\n'):
            contact=[c for c in i.split('\n')]
            self.add_contact(Contact(contact[0],contact[1],contact[2]),False)
        self._save()

    def import_from_csv(self,file: Path) -> None:
        for i in file.read_text('utf-8').split('\n'):
            contact=[c for c in i.split(';')]
            self.add_contact(Contact(contact[0],contact[1],contact[2]),False)
        self._save()

    def export_to_txt(self,file: Path) -> None:
        file.write_text('\n*\n'.join([f"{i.surname()}\n{i.name()}\n{i.phone()}" for i in self._book]),'utf-8')

    def export_to_csv(self,file: Path) -> None:
        file.write_text('\n'.join([f"{i.surname()};{i.name()};{i.phone()}" for i in self._book]),'utf-8')

    def _save(self) -> None:
        Path("phone_book.csv").write_text('\n'.join([f"{i.surname()};{i.name()};{i.phone()}" for i in self._book]),'utf-8')

    def _load(self) -> None:
        for i in Path("phone_book.csv").read_text('utf-8').split('\n'):
            contact=[c for c in i.split(';')]
            if len(contact) != 3: continue
            self.add_contact(Contact(contact[0],contact[1],contact[2]),False)