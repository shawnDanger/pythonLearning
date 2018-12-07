# -*- mode: python -*-

block_cipher = None


a = Analysis(['hi.py'],
             pathex=['D:\\MajorSoftware\\IDEA\\PyCharm\\PyCharmWorkspace\\GitHub\\pythonLearning\\src\\main\\base\\chp18_程序打包\\01_setuptools基础'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          name='hi',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
