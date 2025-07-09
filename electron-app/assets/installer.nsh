; 简单的 NSIS 自定义脚本 - 解决卸载完整性问题

; 卸载前检查
!macro customUnInit
  ; 检查程序是否正在运行并强制关闭
  FindWindow $0 "" "BRCA Desktop"
  IntCmp $0 0 done
  SendMessage $0 ${WM_CLOSE} 0 0
  Sleep 1000
  FindWindow $0 "" "BRCA Desktop"
  IntCmp $0 0 done
  ; 如果仍在运行，强制结束进程
  nsExec::ExecToStack 'taskkill /f /im "BRCA Desktop.exe"'
  nsExec::ExecToStack 'taskkill /f /im "brca_backend.exe"'
  done:
!macroend

; 自定义卸载过程
!macro customUnInstall
  ; 确保进程已停止
  nsExec::ExecToStack 'taskkill /f /im "BRCA Desktop.exe"'
  nsExec::ExecToStack 'taskkill /f /im "brca_backend.exe"'
  Sleep 500
  
  ; 删除程序文件
  Delete "$INSTDIR\BRCA Desktop.exe"
  Delete "$INSTDIR\brca_backend.exe"
  
  ; 删除用户数据
  RMDir /r "$APPDATA\brca-desktop"
  RMDir /r "$LOCALAPPDATA\brca-desktop"
  
  ; 删除快捷方式
  Delete "$DESKTOP\BRCA Desktop.lnk"
  Delete "$SMPROGRAMS\BRCA Desktop.lnk"
  Delete "$SMPROGRAMS\BRCA\BRCA Desktop.lnk"
  Delete "$SMPROGRAMS\BRCA\Uninstall BRCA Desktop.lnk"
  RMDir "$SMPROGRAMS\BRCA"
  
  ; 清理注册表
  DeleteRegKey HKLM "SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\{${UNINSTALL_APP_KEY}}"
  DeleteRegKey HKCU "SOFTWARE\brca-desktop"
!macroend 