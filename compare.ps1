$LIST1 = Get-ChildItem -Path $args[0] -name
$LIST2 = Get-ChildItem -Path $args[1] -name

if (-Not (($LIST1 | Measure-Object).count -eq ($LIST2 | Measure-Object).count)) {
    Write-Host "The amount of Files doesn't match." -ForegroundColor Red
} Else {
    $cnt = ($LIST1 | Measure-Object).count
    for ($i = 0; $i -lt $cnt; $i++) {

        $FILE1 = Join-Path -Path $args[0] -ChildPath $LIST1[$i]
        $FILE2 = Join-Path -Path $args[1] -ChildPath $LIST2[$i]

        if (Compare-Object -ReferenceObject $(Get-Content $FILE1) -DifferenceObject $(Get-Content $FILE2)) {

            Write-Host "Compare Failed: " -ForegroundColor Red -NoNewline
            Write-Host "$(Write-Output $FILE1) " -ForegroundColor Cyan -NoNewline
            Write-Host "and " -ForegroundColor White -NoNewline
            Write-Host "$(Write-Output $FILE2)" -ForegroundColor Magenta
            exit(-1)
        }
    }
    Write-Host "Compare Success: " -ForegroundColor Green -NoNewline
    Write-Host "$(Write-Output $args[0]) " -ForegroundColor Cyan -NoNewline
    Write-Host "and " -ForegroundColor White -NoNewline
    Write-Host "$(Write-Output $args[1])" -ForegroundColor Magenta
}
