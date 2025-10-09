from pybricks.tools import hub_menu

# Make a menu to choose a letter. You can also use numbers.
selected = hub_menu("1", "2", "3")

# Based on the selection, run a program.
if selected == "1":
    import hello_world
elif selected == "2":
    import sound
elif selected == "3":
    import xBox_Controls