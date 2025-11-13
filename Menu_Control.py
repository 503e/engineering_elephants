from pybricks.tools import hub_menu

# Make a menu to choose a letter. You can also use numbers.
selected = hub_menu("1", "2", "3", "4","5", "6", "X")

# Based on the selection, run a program.
if selected == "1":
    import thesandmission
elif selected == "2":
      import mission_01
elif selected == "3":
    import mission_03
elif    selected == "4":
    import mission_02_final
elif    selected == "5":
    import mission_07
elif    selected == "6":
    import mission_08
elif selected == "X":
    import xBox_Controls
