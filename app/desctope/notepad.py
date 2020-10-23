from pywinauto.application import Application
app = Application().Start(cmd_line=u'"B:\Program Files (x86)\AbilityCash\AbilityCash.exe" ')
acmw = app[u'AC-MW']
acdp = acmw[u'AC-E']
acdp.Click()

for _ in range(10):
    acmw.Wait('ready')
    acdp = acmw[u'AC-E']
    acdp.Click()
    acmw[u'AC-E'].set_text('123')
    for _ in range(10):
        acmw.Wait('ready')
        acdp = acmw[u'AC-E']
        acdp.Click()
        acmw[u'AC-E'].set_text('123')
acmw[u'AC-E'].set_text('123')
