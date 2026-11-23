# Chép bộ skill từ kho về đúng vị trí trên máy. Chỉ chép, không xóa.
# File trùng tên đang có ở đích sẽ được sao lưu vào E:\New folder\_backup\00-Chung\ trước khi ghi.
$ErrorActionPreference = 'Stop'
$kho   = $PSScriptRoot
$tg    = Get-Date -Format 'yyyyMMdd-HHmm'
$bk    = "E:\New folder\_backup\00-Chung\$tg`_skill-truoc-khoi-phuc"

$cap = @(
  @("$kho\01-UserClaude\skills",   "$env:USERPROFILE\.claude\skills"),
  @("$kho\02-DuAn-claude\skills",  "E:\New folder\.claude\skills"),
  @("$kho\02-DuAn-claude\agents",  "E:\New folder\.claude\agents"),
  @("$kho\02-DuAn-claude\commands","E:\New folder\.claude\commands"),
  @("$kho\03-Skill-DoBoc_v02",     "E:\New folder\06-CongCu\01-Skill-DoBoc_v02")
)

foreach ($c in $cap) {
  $nguon = $c[0]; $dich = $c[1]
  if (-not (Test-Path $nguon)) { Write-Host "Bo qua (kho khong co): $nguon"; continue }
  if (Test-Path $dich) {
    $ten = ($dich -replace '[:\\]', '_')
    robocopy $dich "$bk\$ten" /E /NFL /NDL /NJH /NJS /NP | Out-Null
    Write-Host "Da sao luu: $dich"
  }
  robocopy $nguon $dich /E /NFL /NDL /NJH /NJS /NP | Out-Null
  Write-Host "Da chep: $nguon -> $dich"
}
# File CLAUDE.md (global va du an)
$tep = @(
  @("$kho\01-UserClaude\CLAUDE.md",  "$env:USERPROFILE\.claude\CLAUDE.md"),
  @("$kho\02-DuAn-claude\CLAUDE.md", "E:\New folder\CLAUDE.md")
)
foreach ($t in $tep) {
  $nguon = $t[0]; $dich = $t[1]
  if (-not (Test-Path $nguon)) { Write-Host "Bo qua (kho khong co): $nguon"; continue }
  if (Test-Path $dich) {
    New-Item -ItemType Directory -Force $bk | Out-Null
    $ten = ($dich -replace '[:\\]', '_')
    Copy-Item $dich "$bk\$ten"
    Write-Host "Da sao luu: $dich"
  }
  New-Item -ItemType Directory -Force (Split-Path $dich) | Out-Null
  Copy-Item $nguon $dich -Force
  Write-Host "Da chep: $nguon -> $dich"
}
Write-Host "Xong. Mo lai Claude Code de nhan skill."
