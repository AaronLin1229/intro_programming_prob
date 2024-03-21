#include <stdio.h>
#include <string.h>
 
int check1(char *s1, char *s2){
    int n1 = strlen(s1), n2 = strlen(s2);
    if(n1 != n2) return 0;
 
    for(int i = 0; i < n1 - 1; i++){
        {char tmp = s1[i]; s1[i] = s1[i + 1]; s1[i + 1] = tmp;}
        if(strcmp(s1, s2) == 0) return 1;
        {char tmp = s1[i]; s1[i] = s1[i + 1]; s1[i + 1] = tmp;}
    }
    return 0;
}
 
int check2(char *s1, char *s2){
    int n1 = strlen(s1), n2 = strlen(s2);
    if(n2 - n1 != 1) return 0;
 
    int first_diff = 0;
    for(; first_diff < n1; first_diff++){
        if(s1[first_diff] != s2[first_diff]) break;
    }
 
    for(int i = first_diff; i < n1; i++){
        if(s1[i] != s2[i + 1]) return 0;
    }
    return 1;
}
 
int check3(char *s1, char *s2){
    return strcmp(s1, s2) == 0;
}
 
int check(char *s1, char *s2){
    if(strlen(s1) > strlen(s2)){
        char* tmp = s1; s1 = s2; s2 = tmp; 
    }
 
    return check3(s1, s2) || check2(s1, s2) || check1(s1, s2);
}
 
 
int main(){
    int n;
    scanf("%d", &n);
 
    while(n--){
        char s1[128], s2[128];
        scanf("%s %s", s1, s2);
 
        printf("%s\n", check(s1, s2) ? "yes" : "no");
    }
}