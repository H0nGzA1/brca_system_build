# BRCA Desktop Complete Cleanup Script
# Must be run as Administrator

Write-Host "=== BRCA Desktop Complete Cleanup Tool ===" -ForegroundColor Green
Write-Host "Cleaning all BRCA Desktop files and registry entries..." -ForegroundColor Yellow

# Step 1: Stop all related processes
Write-Host "`n[1/6] Stopping related processes..." -ForegroundColor Cyan
$processes = @("BRCA Desktop", "brca_backend", "brca-desktop")
foreach ($proc in $processes) {
    try {
        Get-Process -Name $proc -ErrorAction SilentlyContinue | Stop-Process -Force
        Write-Host "✓ Stopped process: $proc" -ForegroundColor Green
    } catch {
        Write-Host "○ Process not running: $proc" -ForegroundColor Gray
    }
}

# Step 2: Delete program files
Write-Host "`n[2/6] Deleting program files..." -ForegroundColor Cyan
$programPaths = @(
    "$env:ProgramFiles\BRCA Desktop",
    "$env:ProgramFiles(x86)\BRCA Desktop",
    "$env:LOCALAPPDATA\Programs\BRCA Desktop",
    "$env:LOCALAPPDATA\Programs\brca-desktop"
)

foreach ($path in $programPaths) {
    if (Test-Path $path) {
        Remove-Item $path -Recurse -Force -ErrorAction SilentlyContinue
        Write-Host "✓ Deleted directory: $path" -ForegroundColor Green
    } else {
        Write-Host "○ Directory not found: $path" -ForegroundColor Gray
    }
}

# Step 3: Clean registry
Write-Host "`n[3/6] Cleaning registry..." -ForegroundColor Cyan
$uninstallKeys = @(
    "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*",
    "HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*"
)

$removed = 0
foreach ($keyPath in $uninstallKeys) {
    Get-ChildItem $keyPath -ErrorAction SilentlyContinue | ForEach-Object {
        $displayName = (Get-ItemProperty $_.PSPath -Name "DisplayName" -ErrorAction SilentlyContinue).DisplayName
        if ($displayName -like "*BRCA*") {
            Remove-Item $_.PSPath -Recurse -Force -ErrorAction SilentlyContinue
            Write-Host "✓ Deleted uninstall registry entry: $displayName" -ForegroundColor Green
            $removed++
        }
    }
}

# Clean application registry entries
$appKeys = @(
    "HKCU:\SOFTWARE\brca-desktop",
    "HKCU:\SOFTWARE\BRCA Desktop",
    "HKLM:\SOFTWARE\brca-desktop",
    "HKLM:\SOFTWARE\BRCA Desktop"
)

foreach ($key in $appKeys) {
    if (Test-Path $key) {
        Remove-Item $key -Recurse -Force -ErrorAction SilentlyContinue
        Write-Host "✓ Deleted app registry entry: $key" -ForegroundColor Green
        $removed++
    }
}

if ($removed -eq 0) {
    Write-Host "○ No related registry entries found" -ForegroundColor Gray
}

# Step 4: Delete shortcuts
Write-Host "`n[4/6] Deleting shortcuts..." -ForegroundColor Cyan
$shortcuts = @(
    "$env:PUBLIC\Desktop\BRCA Desktop.lnk",
    "$env:USERPROFILE\Desktop\BRCA Desktop.lnk",
    "$env:ProgramData\Microsoft\Windows\Start Menu\Programs\BRCA Desktop.lnk",
    "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\BRCA Desktop.lnk"
)

$shortcutDirs = @(
    "$env:ProgramData\Microsoft\Windows\Start Menu\Programs\BRCA",
    "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\BRCA"
)

foreach ($shortcut in $shortcuts) {
    if (Test-Path $shortcut) {
        Remove-Item $shortcut -Force -ErrorAction SilentlyContinue
        Write-Host "✓ Deleted shortcut: $shortcut" -ForegroundColor Green
    }
}

foreach ($dir in $shortcutDirs) {
    if (Test-Path $dir) {
        Remove-Item $dir -Recurse -Force -ErrorAction SilentlyContinue
        Write-Host "✓ Deleted shortcut directory: $dir" -ForegroundColor Green
    }
}

# Step 5: Clean user data
Write-Host "`n[5/6] Cleaning user data..." -ForegroundColor Cyan
$userDataPaths = @(
    "$env:APPDATA\brca-desktop",
    "$env:APPDATA\BRCA Desktop",
    "$env:LOCALAPPDATA\brca-desktop",
    "$env:LOCALAPPDATA\BRCA Desktop"
)

foreach ($path in $userDataPaths) {
    if (Test-Path $path) {
        Remove-Item $path -Recurse -Force -ErrorAction SilentlyContinue
        Write-Host "✓ Deleted user data: $path" -ForegroundColor Green
    } else {
        Write-Host "○ User data not found: $path" -ForegroundColor Gray
    }
}

# Step 6: Clean temporary files
Write-Host "`n[6/6] Cleaning temporary files..." -ForegroundColor Cyan
$tempFiles = Get-ChildItem "$env:TEMP\brca*", "$env:TEMP\BRCA*" -ErrorAction SilentlyContinue
if ($tempFiles) {
    $tempFiles | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
    Write-Host "✓ Cleaned temporary files" -ForegroundColor Green
} else {
    Write-Host "○ No temporary files found" -ForegroundColor Gray
}

Write-Host "`n=== Cleanup Complete ===" -ForegroundColor Green
Write-Host "BRCA Desktop has been completely cleaned." -ForegroundColor Yellow
Write-Host "It is recommended to restart the computer before installing the new version." -ForegroundColor Yellow

# Ask if user wants to restart
$restart = Read-Host "`nDo you want to restart the computer now? (y/n)"
if ($restart -eq "y" -or $restart -eq "Y") {
    Write-Host "Restarting computer..." -ForegroundColor Yellow
    Start-Sleep -Seconds 3
    Restart-Computer -Force
} 