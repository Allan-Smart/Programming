
# Compiler and linker settings
ASM 		= nasm
ASMFLAGS 	= -f elf64 -g -F dwarf
LD 			= ld
LDFLAGS 	= 


# Target binary and object files
TARGET 		= logic_if
OBJ 		= logic_if.o
SRC			= logic_if.asm


# Defaul rule: builds the executable
all: $(TARGET)


# Link the object file into the final binary
$(TARGET): $(OBJ)
	$(LD) $(LDFLAGS) $(OBJ) -o $(TARGET)


# Assemble the source file into an object file
$(OBJ): $(SRC)
	$(ASM) $(ASMFLAGS) $(SRC) -o $(OBJ)


# Remove generated build files
clean:
	rm -f $(OBJ) $(TARGET)


.PHONY: all clean