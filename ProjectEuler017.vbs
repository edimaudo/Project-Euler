Option Explicit

Sub runCheckName()
On Error GoTo ErrorHandler:

Dim ws As Worksheet
Dim i As Long
Dim rangevalue As String

Set ws = ThisWorkbook.Worksheets("Sheet1")

For i = 1 To 1000
    Range("A" & i + 1).Value = i
    Range("B" & i + 1).Value = SpellNumber(i)
    Range("C" & i + 1).Value = countword(Range("B" & i + 1).Value)
Next i

Dim finalcount  As Long
finalcount = ThisWorkbook.Sheets("Sheet1").Cells(Rows.count, "C").End(xlUp).Row

rangevalue = "C2" & ":" & "C" & CStr(finalcount)
Range("D1").Value = WorksheetFunction.Sum(ThisWorkbook.Sheets("Sheet1").Range(rangevalue))
Range("E1").Value = "Total"

Exit Sub
ErrorHandler:
    MsgBox "an error occured"
    MsgBox Err.Description
    End
End Sub

'counts number of words in a string and removes spaces
Function countword(ByRef word As String)
On Error GoTo ErrorHandler:

Dim i As Long
Dim count As Long
Dim newword As String
count = 0
newword = Replace(word, " ", "")
For i = 1 To Len(newword)
    count = count + 1
Next

countword = count


Exit Function
ErrorHandler:
    MsgBox "An error occured while counting words"
    End
End Function

'function that convers numbers to words
'https://support.microsoft.com/en-us/kb/213360'
Function SpellNumber(ByVal MyNumber)
    Dim Dollars, Cents, Temp
    Dim DecimalPlace, count
    ReDim Place(9) As String
    Place(2) = " Thousand "
    Place(3) = " Million "
    Place(4) = " Billion "
    Place(5) = " Trillion "
    ' String representation of amount.
    MyNumber = Trim(Str(MyNumber))
    ' Position of decimal place 0 if none.
    DecimalPlace = InStr(MyNumber, ".")
    ' Convert cents and set MyNumber to dollar amount.
    If DecimalPlace > 0 Then
        Cents = GetTens(Left(Mid(MyNumber, DecimalPlace + 1) & _
                  "00", 2))
        MyNumber = Trim(Left(MyNumber, DecimalPlace - 1))
    End If
    count = 1
    Do While MyNumber <> ""
        Temp = GetHundreds(Right(MyNumber, 3))
        If Temp <> "" Then Dollars = Temp & Place(count) & Dollars
        If Len(MyNumber) > 3 Then
            MyNumber = Left(MyNumber, Len(MyNumber) - 3)
        Else
            MyNumber = ""
        End If
        count = count + 1
    Loop
    Select Case Dollars
        Case ""
            Dollars = "No Dollars"
        Case "One"
            Dollars = "One"
         Case Else
            Dollars = Dollars
    End Select
    Select Case Cents
        Case ""
            Cents = ""
        Case "One"
            Cents = ""
              Case Else
            Cents = ""
    End Select
    SpellNumber = Dollars & Cents
End Function
      
' Converts a number from 100-999 into text
Function GetHundreds(ByVal MyNumber)
    Dim Result As String
    If Val(MyNumber) = 0 Then Exit Function
    MyNumber = Right("000" & MyNumber, 3)
    ' Convert the hundreds place.
    If Mid(MyNumber, 1, 1) <> "0" And Right(MyNumber, 1) = "0" And Mid(MyNumber, 2, 1) = "0" Then
        Result = GetDigit(Mid(MyNumber, 1, 1)) & " Hundred "
    ElseIf Mid(MyNumber, 1, 1) <> "0" Then
        Result = GetDigit(Mid(MyNumber, 1, 1)) & " Hundred " & "and "
    Else
        
    End If
    ' Convert the tens and ones place.
    If Mid(MyNumber, 2, 1) <> "0" Then
        Result = Result & GetTens(Mid(MyNumber, 2))
    Else
        Result = Result & GetDigit(Mid(MyNumber, 3))
    End If
    GetHundreds = Result
End Function
      
' Converts a number from 10 to 99 into text.
Function GetTens(TensText)
    Dim Result As String
    Result = ""           ' Null out the temporary function value.
    If Val(Left(TensText, 1)) = 1 Then   ' If value between 10-19...
        Select Case Val(TensText)
            Case 10: Result = "Ten"
            Case 11: Result = "Eleven"
            Case 12: Result = "Twelve"
            Case 13: Result = "Thirteen"
            Case 14: Result = "Fourteen"
            Case 15: Result = "Fifteen"
            Case 16: Result = "Sixteen"
            Case 17: Result = "Seventeen"
            Case 18: Result = "Eighteen"
            Case 19: Result = "Nineteen"
            Case Else
        End Select
    Else                                 ' If value between 20-99...
        Select Case Val(Left(TensText, 1))
            Case 2: Result = "Twenty "
            Case 3: Result = "Thirty "
            Case 4: Result = "Forty "
            Case 5: Result = "Fifty "
            Case 6: Result = "Sixty "
            Case 7: Result = "Seventy "
            Case 8: Result = "Eighty "
            Case 9: Result = "Ninety "
            Case Else
        End Select
        Result = Result & GetDigit _
            (Right(TensText, 1))  ' Retrieve ones place.
    End If
    GetTens = Result
End Function
     
' Converts a number from 1 to 9 into text.
Function GetDigit(Digit)
    Select Case Val(Digit)
        Case 1: GetDigit = "One"
        Case 2: GetDigit = "Two"
        Case 3: GetDigit = "Three"
        Case 4: GetDigit = "Four"
        Case 5: GetDigit = "Five"
        Case 6: GetDigit = "Six"
        Case 7: GetDigit = "Seven"
        Case 8: GetDigit = "Eight"
        Case 9: GetDigit = "Nine"
        Case Else: GetDigit = ""
    End Select
End Function

