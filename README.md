### ccc814p's x04 CPU Emulator
# Intro
Welcome to ccc814p's x04 CPU Emulator! In this instruction manual, you will learn how to move values into registers, clone the output register, and perform math!
# Moving Values into Registers
The first command you will learn is the `mov` command. The `mov` command's binary version is `1000`. Here is the syntax of a `mov`/`1000` command.
```1000 0000 0001```
## Each Part Explained
`1000`
 Main Instruction |
`0000`
 Register to move value into |
`0001`
 Value to move into the register |
# Math!
The next commands you will learn are mathematical functions! `Add=0001`
`Sub=0010`
`Mul=0011`
`Div=0100`
All math functions share a similar syntax.
```0010 0000 0001```
## Each Part Explained
`0010`
 Mathematical Operand |
`0000`
 First register in math problem |
`0001`
 Second register in math problem |
Think of it this way.
```register1-register2```
The answer to the math problem is moved into a special register named register O!
# Moving the O Register's Value Into Another Register
To move the O register's value into another register, we must use the `mvO`, or `1001` instruction.
The syntax of `mvO`/`1001` looks like this.
```1001 0000 0011```
## Each Part Explained
`1001`
 Main mvO instruction |
`0000`
 Random integer (This doesn't matter!) |
`0011`
 Register to move the O register's value into. |
# Shutting Off the Emulator
To shut off the emulator, simply type
```0000 0000 0000```
