from pybricks.tools import hub_menu


# Make a menu to choose a letter. You can also use numbers.
selected = hub_menu("1", "2", "3")

# Based on the selection, run a program.
if selected == "1":
    import mission_01
elif selected == "2":
    import mission_02
elif selected == "3":
    import xBox_Controls