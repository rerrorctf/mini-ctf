import angr

proj = angr.Project("./task", auto_load_libs=False)

initial_state = proj.factory.entry_state()

sim = proj.factory.simgr(initial_state)

sim.explore(find=0x00401325, avoid=0x00401342)

print(sim.found[0].posix.dumps(0))

