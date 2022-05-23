$customLocation = Get-Location
$customLocation = "$customLocation\*"
$curaLocation = 'C:\Program Files\Ultimaker Cura 5.0.0\share\cura'
#$curaLocation = 'D:\temp\cura'
$exclude = @('*.ps1')
Copy-Item -Path $customLocation -Destination $curaLocation -Exclude $exclude -Force -Recurse 