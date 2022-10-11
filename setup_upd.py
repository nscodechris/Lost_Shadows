import cx_Freeze

executables = [cx_Freeze.Executable("upd_ver_1.1.py")]

cx_Freeze.setup(
    name="patch_upd",
    executables = executables

    )