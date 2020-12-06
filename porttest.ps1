# Allows for a basic TCP connection

#Test-NetConnection 127.0.0.1 -Port 25565

$ipaddress = 127.0.0.1
$port = 25565
$connection = New-Object System.Net.Sockets.TcpClient($ipaddress, $port)
if ($connection.Connected) {
    Write-Host "Success"
}
else {
    Write-Host "Failed"
}