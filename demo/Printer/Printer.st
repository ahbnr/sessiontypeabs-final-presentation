0 -fStart-> App:start.
(
  App      -fInit->    Printer:init.
    Printer  resolves fInit.
  App      -fWrite->    Printer:write.
    Printer  resolves fWrite.
  App      -fPrint->    Printer:print.
    Rel(App, fPrint).
    Printer  resolves fPrint
)*.
App resolves fStart
