$scriptLocation = "$PSScriptRoot\*"
$curaLocation = 'C:\Program Files\Ultimaker Cura 5.7.1\share\cura'
#$curaLocation = 'D:\temp\cura'
$exclude = @('*.ps1')
$output = Copy-Item -Path $scriptLocation -Destination $curaLocation -Exclude $exclude -Force -Recurse -PassThru

if ($output)
{
    $output
}
else
{
    "Copy failure"
} 