# Removes all logs files
$files = "ftp/logs/ftp.log", "httpServer/logs/http.log", 
    "ssh/logs/ssh.log", "tcp/logs/minecraft_tcp.log"

foreach ($file in $files) {
    if (test-path $file) {
    remove-item $file
    }
}

