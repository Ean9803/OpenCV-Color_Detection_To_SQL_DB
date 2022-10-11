import NetworkTable as NT
import VisionCV as CV

Vis = CV.VisionTracker()
Table = NT.NetTable()

while not Vis.CancelBtn():
    Objects = Vis.ProcessVideo()
    i = 0
    Table.DeleteAllData()
    for Obj in Objects:
        Table.InsertData(i, Obj[0], Obj[1])
        i += 1
    Table.InsertData(-1, i, i)
    Table.CommitChanges()
Vis.FinishVideo()
Table.CloseTable()