
section .data

    msg     db "Hello, World!", 10          ; Define string with newline character
    len     equ $ - msg                     ; Calculate string length dynammically

section .text

    global _start                           ; Expose entry point to the linker

_start:

    ; ---------- Print "Hello, World!" ----------

    mov eax, 1                              ; System call ID for sys_write
    mov edi, 1                              ; File descriptor 1 (stdout)
    mov rsi, msg                            ; Pointer to the message string
    mov edx, len                            ; Number of bytes to write
    syscall

    ; ---------- Exit the program cleanly ----------

    mov eax, 60                             ; System call ID for sys_exit
    mov edi, 0                              ; Exit plainly
    syscall