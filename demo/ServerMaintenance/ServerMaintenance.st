0 -fStart-> Controller:start.
(
  Controller -fCheck-> MainServer:checkStatus.
  MainServer {
    MainServer resolves fCheck with Ok.
      Controller fetches fCheck as Ok,

    MainServer resolves fCheck with NeedsUpdate.
      Controller fetches fCheck as NeedsUpdate.

      Controller -fPowerOn-> BackupServer:powerOn.
        Rel(Controller, fPowerOn).
        BackupServer resolves fPowerOn.

      Controller -fDivert-> Proxy:divertToBackup.
        Rel(Controller, fDivert).
        Proxy resolves fDivert.

      Controller -fUpdate-> MainServer:update.
        MainServer resolves fUpdate
  }
)*.
Controller resolves fStart
