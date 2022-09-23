import cx_Freeze

executables = [cx_Freeze.Executable("new_hero_classes.py")]

cx_Freeze.setup(
    name="A bit Racey",
    options={"build_exe": {"packages":["pygame", "dbm"]}},
    executables = executables

    )