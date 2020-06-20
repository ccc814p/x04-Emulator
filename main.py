import os, sys
regs = [0, 0, 0, 0, 0]
regsO = 0
runtime = True
print("\nRegisters")
for x in regs:
  print(x)
print(regsO)

while runtime:
  program = input()
  program = program.split()
  program[0] = int(program[0], 2)
  program[1] = int(program[1], 2)
  program[2] = int(program[2], 2)
  print(program)
  print("\n\n")
  if program[0] == 8:
      regs[program[1]] = program[2]
  if program[0] == 1:
      regsO = regs[program[1]] + regs[program[2]]
  if program[0] == 2:
      regsO = regs[program[1]] - regs[program[2]]
  if program[0] == 3:
      regsO = regs[program[1]] * regs[program[2]]
  if program[0] == 4:
      regsO = regs[program[1]] / regs[program[2]]
  if program[0] == 0:
    runtime = False
  if program[0] == 9:
    regs[program[2]] = regsO
  print ("\033[2J\033[H")
  print("Registers")
  for x in regs:
    print(bin(x)[2:])
  print(bin(regsO)[2:])