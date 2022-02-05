Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "main.bat" & Chr(34), windowStyle, waitOnReturn
Set WshShell = Nothing