import multiprocessing
import os
import sys

print("=== Main.py Debug Info ===")
print(f"Current working directory: {os.getcwd()}")
print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")

root_path = os.getcwd()
print(f"Root path: {root_path}")
sys.path.append(root_path)
print(f"Added to sys.path: {root_path}")

# Ensure plugins directory is in path
plugins_path = os.path.join(root_path, 'plugins')
sys.path.append(plugins_path)
print(f"Added plugins path: {plugins_path}")
print(f"Plugins directory exists: {os.path.exists(plugins_path)}")

print("Current sys.path:")
for i, path in enumerate(sys.path):
    print(f"  {i}: {path}")

print("=== Starting imports ===")
import uvicorn
print("✓ uvicorn imported successfully")

try:
    from application.settings import LOGGING
    print("✓ LOGGING imported successfully")
except Exception as e:
    print(f"❌ Error importing LOGGING: {e}")
    import traceback
    traceback.print_exc()
    raise

if __name__ == '__main__':
    multiprocessing.freeze_support()
    workers = 1
    if os.sys.platform.startswith('win'):
        # Windows操作系统
        workers = None
    uvicorn.run("application.asgi:application", reload=False, host="0.0.0.0", port=8000, workers=workers,
                log_config=LOGGING)
