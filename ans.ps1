$date = $args[0]
$no = $args[1]

If ($args.Length -lt 2) {
    echo "Error! Please follow the format:`n ans.ps1 [date] [number_of_question]"
    exit(-1)
}

If (Test-Path "${date}out.txt") {
    Clear-Content "${date}out.txt"
}

For ($i = 1; $i -le $no; $i++) {
    Get-Content "${date}in_$i.txt" | python "$date$i.py" >> "${date}out.txt"
    echo "`n" >> "${date}out.txt"
}
