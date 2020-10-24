from pywinauto.application import Application

app = Application().Start(cmd_line=u'"B:\\Program Files (x86)\\AbilityCash\\AbilityCash.exe" ')
acmw = app[u'AC-MW']
acmw.Wait('ready')
menu_item = acmw.MenuItem(u'\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440->&2 \u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438\tAlt+2')
menu_item.Click()
menu_item2 = acmw.MenuItem(u'\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u044f->\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c\tInsert')
menu_item2.Click()
window = app.Dialog
acrd = window[u'7']
acrd.MoveMouse()
acrd.Click()
pass
