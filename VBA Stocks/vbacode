Sub stock()
    For Each ws In Worksheets
        Dim ticker As String
        Dim lastrow As Long
        lastrow = ws.Range("A" & Rows.Count).End(xlUp).Row
        Dim volume As Double
        volume = 0
        Dim yearlychange As Double
        Dim percentcharged As Double
        Dim start As Long
        start = 2
        ' Keep track of the location for each ticker in the summary table
        Dim Summary_Table_Row As Integer
        Summary_Table_Row = 2
        ' Loop through all stock volume
        For i = 2 To lastrow
        volume = volume + ws.Cells(i, 7).Value
            ' Check if we are still within the same ticker
            If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
                ' Set the ticker name
                ticker = ws.Cells(i, 1).Value
                ' Add to the total stock volume
                yearlychange = ws.Cells(i, 6) - ws.Cells(start, 3)
                If ws.Cells(start, 3).Value <> 0 Then
                    percentcharged = (yearlychange / ws.Cells(start, 3))
                    Else
                    percentcharged = (yearlychange / 0.0001)
                End If
                ws.Range("I" & Summary_Table_Row).Value = ticker
                ws.Range("J" & Summary_Table_Row).Value = yearlychange
                ws.Range("K" & Summary_Table_Row).Value = percentcharged
                ws.Range("L" & Summary_Table_Row).Value = volume
                
                ws.Cells(Summary_Table_Row, 11).NumberFormat = "0.00%"
                'Conditional formatting that will highlight positive change in green and negative change in red For Yearly Change and Yearly Percentage Change
                If (yearlychange > 0) Then
                    ws.Cells(Summary_Table_Row, 11).Interior.ColorIndex = 4
                ElseIf (yearlychange < 0) Then
                    ws.Cells(Summary_Table_Row, 11).Interior.ColorIndex = 3
                Else
                    ws.Cells(Summary_Table_Row, 11).Interior.ColorIndex = 0
                End If
                ' Add one to the summary table row
                Summary_Table_Row = Summary_Table_Row + 1
                ' Reset the total volume
                volume = 0
                start = i + 1
            Else
            ' Add to the total volume
            End If
        Next i
        Next ws
 End Sub
Sub Greatest()
Dim ws As Worksheet
For Each ws In ActiveWindow.SelectedSheets
   
Dim percentincrease As Double
Dim percentdecrease As Double
Dim greatestvolume As Double
Dim tickername As String
 Dim lastrow As Long
        lastrow = ws.Range("A" & Rows.Count).End(xlUp).Row
ws.Range("O2").Value = "Greatest % Increase"
ws.Range("O3").Value = "Greatest % Decrease"
ws.Range("O4").Value = "Greatest Total Volume"
ws.Range("P1").Value = "Value"
percentincrease = ws.Application.WorksheetFunction.Max(Columns("K").Value)
    ws.Cells(2, 16).NumberFormat = "0.00%"
    ws.Cells(2, 16).Value = percentincrease
percentdecrease = ws.Application.WorksheetFunction.Min(Columns("K").Value)
    ws.Cells(3, 16).NumberFormat = "0.00%"
    ws.Cells(3, 16).Value = percentdecrease
greatestvolume = ws.Application.WorksheetFunction.Max(Columns("L").Value)
    ws.Cells(4, 16).Value = greatestvolume

    
Next ws
End Sub


