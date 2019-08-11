/*
    Compile with gcc bufff.c  -m32 -o bufff -fno-stack-protector -O0 -no-pie
    The file is named bufff
*/

#include<stdio.h>
#include<stdlib.h>

void ohSh1t() {
    puts("Such a weird name! But hey, nice job! Welcome!");
    puts("Try to find the flag (lying around somewhere?)\n");
    system("/bin/sh");
}

void indestructible() {
    char name[42] = {0};
    char* output1 = "I am the best hacker on earth";
    char* output2 = "I am indestructible";
    char* output3 = "try me:)";
    char* output4 = "Hmm you can do better than that:)";
    puts(output1);
    puts(output2);
    puts(output3);
    printf("> ");
    gets(name);

}


int main() {
    setbuf(stdout, NULL);
    fflush(stdin);
    indestructible();
    puts("Hmm you can do better than that:)");
}
