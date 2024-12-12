# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['PDFgenerator.py'],
    pathex=[],
    binaries=[],
    datas=[
    ('C:/Users/binja/anaconda3/Lib/site-packages/pymatgen/core/periodic_table.json', 'pymatgen/core'),
    ('C:/Users/binja/anaconda3/Lib/site-packages/pymatgen/core/bond_lengths.json', 'pymatgen/core'),
    ('C:/Users/binja/anaconda3/Lib/site-packages/pymatgen/core/func_groups.json', 'pymatgen/core'),
    ('C:/Users/binja/anaconda3/Lib/site-packages/pymatgen/core/libxc_docs.json', 'pymatgen/core'),
    ('C:/Users/binja/anaconda3/Lib/site-packages/pymatgen/core/quad_data.json', 'pymatgen/core'),
    ('C:/Users/binja/anaconda3/Lib/site-packages/pymatgen/core/reconstructions_archive.json', 'pymatgen/core'),
    ('C:/Users/binja/anaconda3/Lib/site-packages/pymatgen/symmetry/symm_data.json', 'pymatgen/symmetry'),
    ('C:/Users/binja/anaconda3/Lib/site-packages/pymatgen/symmetry/symm_ops.json', 'pymatgen/symmetry'),
    ('C:/Users/binja/anaconda3/Lib/site-packages/pymatgen/analysis/aflow_prototypes.json', 'pymatgen/analysis'),
    ('C:/Users/binja/anaconda3/Lib/site-packages/pymatgen/analysis/ionic_radii.json', 'pymatgen/analysis'),
    ('C:/Users/binja/anaconda3/Lib/site-packages/pymatgen/analysis/ionic_radii.json', 'pymatgen/analysis'),
    ('C:/Users/binja/anaconda3/Lib/site-packages/pymatgen/analysis/diffraction/atomic_scattering_params.json', 'pymatgen/analysis/diffraction'),
    ('C:/Users/binja/anaconda3/Lib/site-packages/pymatgen/analysis/diffraction/neutron_scattering_length.json', 'pymatgen/analysis/diffraction'),
    ('C:/Users/binja/anaconda3/Lib/site-packages/pymatgen/io/vasp/incar_parameters.json', 'pymatgen/io/vasp'),
    ('C:/Users/binja/anaconda3/Lib/site-packages/pymatgen/io/vasp/vasp_potcar_file_hashes.json', 'pymatgen/io/vasp'),
    ('C:/Users/binja/anaconda3/Lib/site-packages/pymatgen/io/vasp/vasp_potcar_pymatgen_hashes.json', 'pymatgen/io/vasp'),
    ('C:/Users/binja/anaconda3/Lib/site-packages/pymatgen/entries/data/g_els.json', 'pymatgen/entries/data'),
    ('C:/Users/binja/anaconda3/Lib/site-packages/pymatgen/entries/data/nist_gas_gf.json', 'pymatgen/entries/data'),

]
    ,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='PDFgenerator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
