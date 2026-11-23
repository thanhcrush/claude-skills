# Bộ skill Claude Code — Công ty TNHH Nghĩa Đạt

Kho riêng tư (Private). Bản chép từ máy chính ngày 23/11/2026.

## Nội dung

| Thư mục trong kho | Lấy từ (máy chính) | Chép về (máy mới) |
|---|---|---|
| `01-UserClaude\skills\` | `C:\Users\<tên máy>\.claude\skills\` | `%USERPROFILE%\.claude\skills\` |
| `02-DuAn-claude\skills\` | `E:\New folder\.claude\skills\` | `E:\New folder\.claude\skills\` |
| `02-DuAn-claude\agents\` | `E:\New folder\.claude\agents\` | `E:\New folder\.claude\agents\` |
| `02-DuAn-claude\commands\` | `E:\New folder\.claude\commands\` | `E:\New folder\.claude\commands\` |
| `03-Skill-DoBoc_v02\` | `E:\New folder\06-CongCu\01-Skill-DoBoc_v02\` | `E:\New folder\06-CongCu\01-Skill-DoBoc_v02\` |
| `01-UserClaude\CLAUDE.md` | `C:\Users\<tên máy>\.claude\CLAUDE.md` (global) | `%USERPROFILE%\.claude\CLAUDE.md` |
| `02-DuAn-claude\CLAUDE.md` | `E:\New folder\CLAUDE.md` (dự án) | `E:\New folder\CLAUDE.md` |

Không có trong kho: thư mục memory, cài đặt (settings.json), MCP, Python và thư viện.

## Cài lên máy thứ 2

1. Cài Git, GitHub CLI: `winget install --id GitHub.cli -e`
2. Đăng nhập: `gh auth login --web`
3. Tải kho về:
   ```powershell
   gh repo clone <tài khoản>/claude-skills "E:\New folder\06-CongCu\09-GitHub-Skill"
   ```
4. Chép vào đúng chỗ (file đang có ở máy mới sẽ được sao lưu vào `E:\New folder\_backup\00-Chung\` trước):
   ```powershell
   powershell -ExecutionPolicy Bypass -File "E:\New folder\06-CongCu\09-GitHub-Skill\khoi_phuc.ps1"
   ```
5. Mở lại Claude Code.

## Cập nhật về sau

- Máy chính sửa skill xong: chép lại vào thư mục này, rồi `git add -A`, `git commit -m "..."`, `git push`.
- Máy thứ 2: `git pull`, rồi chạy lại `khoi_phuc.ps1`.
