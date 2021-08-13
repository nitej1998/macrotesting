    ' Configfile = "C:\Users\Admin\Desktop\Optimised Accelerated Config.xlsx"
  on error resume next    
    Configfile = WScript.Arguments(0)
    Set eapp = CreateObject("Excel.Application")
    eapp.Visible = True
    Set wkbk_Config = eapp.Workbooks.Open(Configfile)
    vNewfile = wkbk_Config.Sheets("Filepaths").Range("B2").Value
    vOldfile = wkbk_Config.Sheets("Filepaths").Range("B1").Value
    Set wkbk_from = eapp.Workbooks.Open(vOldfile)
    Set wkbk_to = eapp.Workbooks.Open(vNewfile)
    Set objsht = wkbk_Config.Sheets("Channels")
    LR = objsht.UsedRange.Rows.Count
    For i = 2 To LR
		 vChannels = wkbk_Config.Sheets("Channels").Range("A" & i).Value
		 Set FoundCell = wkbk_from.Worksheets("TV Plan").Range("A:A").Find(vChannels)
		 OldfileStartRow = FoundCell.Row
		 Set FoundCell = wkbk_from.Worksheets("TV Plan").Range("A:A").Find("Total " & vChannels)
		 OldfileEndRow = FoundCell.Row - 1
		 Set FoundCell = wkbk_to.Worksheets("TV Plan").Range("A:A").Find(vChannels)
		 NewfileStartRow = FoundCell.Row
		 Set FoundCell = wkbk_to.Worksheets("TV Plan").Range("A:A").Find("Total " & vChannels)
		 NewfileEndRow = FoundCell.Row - 1
		 For j = 13 To 52
		   sColumn = Split(wkbk_from.Sheets("TV Plan").Cells(1, j).Address(True, False), "$")(0)
		   wkbk_from.Worksheets("TV Plan").Range(sColumn & OldfileStartRow & ":" & sColumn & OldfileEndRow).Copy wkbk_to.Worksheets("TV Plan").Range(sColumn & NewfileStartRow & ":" & sColumn & NewfileStartRow)
		   j = j + 3                 	               
		 Next
    Next
    
    wkbk_to.Save
    wkbk_from.Close
    wkbk_to.Close
    wkbk_Config.Close
	