from pywinauto.application import Application

app = Application().Start(cmd_line=u'"B:\\Program Files (x86)\\AbilityCash\\AbilityCash.exe" ')

menu_item = app[u'AC-MW'].MenuItem(u'Просмотр->Операции  Alt+2').Click()

menu_item2 = app[u'AC-MW'].MenuItem(u'Действия->Добавить Insert').Click()

window = app.Dialog  # <--- Переход к работе с диалогом
window[u'AC-BC'].Click()  # <--- Приход
window[u'AC-BC7'].Click()  # <--- Не выполнена
# window[u'AC-BC5'].Click()  # <--- выполнена
# window[u'AC-BC2'].Click()  # <--- Расход
window[u'AC-E'].type_keys('10.00')  # <--- Установить значение в ячейку
window[u'AC-E2'].type_keys('ВСТАВИЛ ЗНАЧЕНИЕ!')  # <--- Установить значение в ячейку
window[u'AC-BC11'].Click()  # <--- Кнопка Добавить

app.Kill_()