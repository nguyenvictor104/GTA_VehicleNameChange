# Prompt user for input
$newName = Read-Host "Enter the new name for the files"

# Get all files in the current directory excluding PowerShell files
$files = Get-ChildItem -File | Where-Object { $_.Extension -ne '.ps1' }

# Rename each file with the new name, appending "_hi" if the file name includes it
foreach ($file in $files) {
    $appendString = ""
    if ($file.BaseName -like "*_hi*") {
        $appendString = "_hi"
    }

    $newFileName = $newName + $appendString + $file.Extension
    Rename-Item -Path $file.FullName -NewName $newFileName
}

Write-Host "Files renamed successfully."