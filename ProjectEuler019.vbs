Option Explicit

Sub CountSunday()
On Error GoTo errorhandler:

Dim dateInfo As Date
Dim count As Long
count = 0

For dateInfo = DateSerial(1901, 1, 1) To DateSerial(2000, 12, 31)
    If DateSerial(Year(dateInfo), Month(dateInfo), 1) = dateInfo And Weekday(dateInfo) = 1 Then
        count = count + 1
    End If
Next

MsgBox count

Exit Sub
errorhandler:
    MsgBox "An error occured: " & Err.Description
    End
End Sub
