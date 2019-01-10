# -*- mode: python -*-
#
# PyInstaller configuration.
# To build executable: $ pyinstaller pyshmup.spec

block_cipher = None


a = Analysis(['pyshmup.py'],
             pathex=['C:\\Users\\Nate\\Workspace\\pyshmup'],
             binaries=[],
             datas=[('resources', 'resources')],
             hiddenimports=['pygame'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='pyshmup',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
