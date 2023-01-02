import cmd
from controller import Controller

class PhoneBookShell(cmd.Cmd):
    intro = 'Введите help или ? для получения перечня команд.\n'
    prompt = 'Phone Book >>> '

    def __init__(self,controller: Controller):
        super().__init__()
        self._controller=controller

    def do_add(self,arg):
        'Добавить контакт:  add Фамилия Имя Телефон'
        self._controller.add_contact(arg)

    def do_all(self,arg):
        'Показать все контакты:  all'
        print('\n'.join(self._controller.all_contacts()))

    def do_fullname(self,arg):
        'Показать контакты с указанными фамилией и именем:  fullname Фамилия Имя'
        print('\n'.join(self._controller.contacts_by_fullname(arg)))
    
    def do_surname(self,arg):
        'Показать контакты с указанной фамилией:  surname Фамилия'
        print('\n'.join(self._controller.contacts_by_surname(arg)))

    def do_name(self,arg):
        'Показать контакты с указанным именем:  name Имя'
        print('\n'.join(self._controller.contacts_by_name(arg)))

    def do_phone(self,arg):
        'Показать контакты с указанным телефоном:  phone Телефон'
        print('\n'.join(self._controller.contacts_by_phone(arg)))

    def do_fromtxt(self,arg):
        'Импортировать контакты из файла .txt:  fromtxt Файл'
        self._controller.import_from_txt(arg)

    def do_fromcsv(self,arg):
        'Импортировать контакты из файла .csv:  fromcsv Файл'
        self._controller.import_from_csv(arg)

    def do_totxt(self,arg):
        'Экспортировать контакты в файл .txt:  totxt Файл'
        self._controller.export_to_txt(arg)

    def do_tocsv(self,arg):
        'Экспортировать контакты в файл .csv:  tocsv Файл'
        self._controller.export_to_csv(arg)