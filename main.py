import sys

# PID Namespace Simulator
# Each namespace gets its own PID counter starting at 1.
# Commands:
#   NEWNS  -> allocate next ns id, init empty process table, print id
#   FORK <ns> <name>  -> spawn process; assign in-ns pid; print pid
#   EXIT <ns> <pid>  -> mark exited; print OK
#   PS <ns>  -> print '<pid> <name> <state>' sorted by pid

# TODO: declare your state structures here
out = []

for raw in sys.stdin:
    line = raw.rstrip("\n")
    if not line.strip():
        continue
    # Use split(' ', N) when an argument may contain spaces (e.g. WRITE <path> <content>)
    parts = line.split()
    cmd = parts[0]
    if cmd == "NEWNS":
        # TODO: allocate next ns id, init empty process table, print id
        pass
    elif cmd == "FORK":
        # args: parts[1]=ns, parts[2]=name
        # TODO: spawn process; assign in-ns pid; print pid
        pass
    elif cmd == "EXIT":
        # args: parts[1]=ns, parts[2]=pid
        # TODO: mark exited; print OK
        pass
    elif cmd == "PS":
        # args: parts[1]=ns
        # TODO: print '<pid> <name> <state>' sorted by pid
        pass

print("\n".join(out))
