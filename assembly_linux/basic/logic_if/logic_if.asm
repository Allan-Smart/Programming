section .data

    ; Ask user for their name
    name_prompt             db "Please enter your name: ",
    name_prompt_len         equ $ - name_prompt

    ; Ask user to enter a number between 1 and 10
    number_prompt           db "Enter a number between 1 - 10: "
    number_prompt_len       equ $ - number_prompt

    ; Print logic statements
    msg_less                db "Less than halfway", 10
    msg_less_len            equ $ - msg_less

    msg_equal               db "Is equal to five", 10
    msg_equal_len           equ $ - msg_equal

    msg_over                db "Is over halfway", 10
    msg_over_len            equ $ - msg_over

section .bss

    ; name buffer
    name_buffer             resb 32

    ; number buffre
    number_buffer           resb 16

section .text

    global _start


_start:

    ;====================================================
    ; 1. PROMPT USER TO ENTER NAME
    ;====================================================
    mov eax, 1                                  ; syscall 1 = sys_write
    mov edi, 1,                                 ; file descriptor 1 = stdout (screen)
    mov rsi, name_prompt                        ; pointer to the prompt string
    mov edx, name_prompt_len                    ; number of bytes to print
    syscall                                     ; invoke kernel

    ;====================================================
    ; 2. READ USER'S NAME
    ;====================================================
    xor eax, eax                                ; syscall 0 = sys read
    xor edi, edi                                ; file descriptor 0 = stdin (screen)
    mov rsi, name_buffer                        ; pointer to our reserved memory buffer 
    mov edx, 32                                 ; maximum number of bytes to read
    syscall                                     ; invoke kernel
    mov r8, rax                                 ; saves the number of bytes of user input


    ;====================================================
    ; 3. PROMPT USER TO ENTER NUMBER
    ;====================================================
    mov eax, 1                                  ; syscall 1 = sys_write
    mov edi, 1                                  ; file descriptor 1 = stdout (screen)
    mov rsi, number_prompt                      ; pointer to the prompt string
    mov edx, number_prompt_len                  ; number of bytes to print
    syscall                                     ; invoke kernel

    ;====================================================
    ; 4. READ USER'S NUMBER
    ;====================================================
    xor eax, eax                                ; syscall 0 = sys read
    xor edi, edi                                ; file descriptor 0 = stdin (screen)
    mov rsi, number_buffer                      ; pointer to our reserved memory buffer
    mov edx, 16                                 ; maximum number of bytes to read
    syscall                                     ; invoke kernel

    ;====================================================
    ; 5. COMPARE AND PRINT RESULT
    ;====================================================
    cmp byte [number_buffer], '1'
    jne single_digit
    cmp byte [number_buffer + 1], '0'
    je over

single_digit:
    movzx eax, byte [number_buffer]
    sub eax, '0'
    cmp eax, 5
    jl less
    je equal
    jg over

less:
    mov eax, 1
    mov edi, 1
    mov rsi, msg_less
    mov edx, msg_less_len
    syscall
    jmp done

equal:
    mov eax, 1
    mov edi, 1
    mov rsi, msg_equal
    mov edx, msg_equal_len
    syscall
    jmp done

over:
    mov eax, 1
    mov edi, 1
    mov rsi, msg_over
    mov edx, msg_over_len
    syscall

    ;====================================================
    ; 6. EXIT
    ;====================================================
done:
    mov eax, 60                                 ; syscall 60 = sys_exit
    xor edi, edi                                ; exit status 0
    syscall                                     ; invoke kernel
