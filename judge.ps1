$folder = $args[0]
$date = $args[0].Split('\')[1]

If ($args.Length -lt 2){
    echo "Error! Please follow the format:`n judge.ps1 [path_to_file] [number_of_question]"
    exit(-1)
}

If (Test-Path "${folder}output.txt"){
    Clear-Content "${folder}output.txt"
}

For ($i = 1; $i -le $args[1]; $i++) {
    $no = '{0:d2}' -f $i
    Get-Content "$date\in_$i.txt" | python "${folder}${date}${no}.py" >> "${folder}output.txt"

    echo "`n" >> "${folder}output.txt"
}
