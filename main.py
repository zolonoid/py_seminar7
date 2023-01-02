import view
import controller
import model

view.PhoneBookShell(controller.Controller(model.PhoneBook())).cmdloop()