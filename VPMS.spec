# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew
from kivymd import hooks_path as kivymd_hooks_path
import sys
import os
path = os.path.abspath(".")

block_cipher = None


a = Analysis(['main.py'],
             pathex=[path],
             binaries=[],
             datas=[],
             hiddenimports=['kivymd.stiffscroll'],
             hookspath=[kivymd_hooks_path],
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
          [],
          exclude_binaries=True,
          name='VPMS',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,Tree('C:\\Users\\Aniket thani\\Desktop\\Vehicle-Parking-Management-System-main\\'),
               a.binaries,
               a.zipfiles,
               a.datas, *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='VPMS')
