$customLocation = Get-Location
$customLocation = "$customLocation\*"
$curaLocation = 'C:\Program Files\Ultimaker Cura 5.3.0\share\cura'
#$curaLocation = 'D:\temp\cura'
$exclude = @('*.ps1')
$output = Copy-Item -Path $customLocation -Destination $curaLocation -Exclude $exclude -Force -Recurse -PassThru

if ($output)
{
    $output
}
else
{
    "Copy failure"
} 