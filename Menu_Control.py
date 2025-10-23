from pybricks.tools import hub_menu

# Make a menu to choose a letter. You can also use numbers.
selected = hub_menu("1", "2", "3", "4")

# Based on the selection, run a program.
if selected == "1":
    import mission_01
elif selected == "2":
    import thesandmission
elif selected == "3":
    import mission_03
elif    selected == "4":
    import mission_02_final