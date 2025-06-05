$scriptLocation = "$PSScriptRoot\*"
$curaLocation = 'C:\Program Files\Ultimaker Cura 5.10.0\share\cura'
#$curaLocation = 'D:\temp\cura'
$exclude = @('*.ps1', '*.py')
$output = Copy-Item -Path $scriptLocation -Destination $curaLocation -Exclude $exclude -Force -Recurse -PassThru

if ($output)
{
    $output
}
else
{
    "Copy failure"
}