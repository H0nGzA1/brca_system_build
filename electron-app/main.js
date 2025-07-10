const { app, BrowserWindow } = require('electron');
const { execFile } = require('child_process');
const path = require('path');
const fs = require('fs');
const os = require('os');

let backendProcess;
let backendPath;
if (process.platform === 'darwin') {
  if (os.arch() === 'arm64') {
    backendPath = path.join(__dirname, 'backend_dist', 'mac-arm64', 'brca_backend');
  } else if (os.arch() === 'x64') {
    backendPath = path.join(__dirname, 'backend_dist', 'mac-x64', 'brca_backend');
  } else {
    throw new Error('Unsupported macOS architecture: ' + os.arch());
  }
} else if (process.platform === 'win32') {
  backendPath = path.join(__dirname, 'backend_dist', 'win', 'brca_backend.exe');
} else if (process.platform === 'linux') {
  backendPath = path.join(__dirname, 'backend_dist', 'linux', 'brca_backend');
} else {
  throw new Error('Unsupported platform: ' + process.platform);
}

function createWindow () {
  const win = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
      webSecurity: false, // 允许本地资源加载
      allowRunningInsecureContent: true,
      webviewTag: true,
      // 确保支持Vue Router
      enableRemoteModule: true
    }
  });

  let indexPath = path.join(__dirname, 'static', 'index.html');
  console.log('indexPath:', indexPath, fs.existsSync(indexPath));
  win.loadFile(indexPath);

  // 允许所有导航，包括hash路由
  win.webContents.on('will-navigate', (event, navigationUrl) => {
    console.log('导航到:', navigationUrl);
    // 允许所有导航
  });

  // 处理新窗口打开
  win.webContents.setWindowOpenHandler(({ url }) => {
    console.log('新窗口请求:', url);
    return { action: 'deny' };
  });

  win.webContents.on('did-fail-load', (event, errorCode, errorDescription, validatedURL) => {
    console.log('页面加载失败:', errorCode, errorDescription, validatedURL);
  });
  win.webContents.on('did-finish-load', () => {
    console.log('页面加载成功');
    // 页面加载完成后再启动后端
    if (!backendProcess) {
      backendProcess = execFile(backendPath);
      console.log('后端已启动');
    }
  });

  // 开发时打开开发者工具
  if (process.env.NODE_ENV === 'development') {
    win.webContents.openDevTools();
  }
}

app.whenReady().then(() => {
  createWindow();
});

app.on('window-all-closed', () => {
  if (backendProcess) backendProcess.kill();
  if (process.platform !== 'darwin') app.quit();
}); 