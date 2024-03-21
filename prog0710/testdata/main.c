#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>
#define plate_1 1
#define plate_2 2
 
int cmp(const void* a, const void* b){
    return strcmp((char*)a, (char*)b);
}
 
bool check_1(char* s){
    if(s[2] == '-'){
        for(int i = 0; i < 7; i++){
            if(i == 2) continue;
            if(!(isalpha(s[i]) || isdigit(s[i]))) return false;
        }
    }
    else if(s[3] == '-'){
        for(int i = 0; i < 7; i++){
            if(i == 3) continue;
            if(!(isalpha(s[i]) || isdigit(s[i]))) return false;
        }
    }
    else{
        return false;;
    }
    return true;
}
bool check_2(char* s){
    bool have_digit = false;
    int sum = 0;
    for(int i = 0; i < 7; i++){
        if(isdigit(s[i])){
            have_digit = true;
            sum += (s[i] - '0');
        }
    }
    return have_digit && (sum % 7 != 0);
}
bool check_3(char* s){
    int count[128] = {0};
    for(int i = 0; i < 7; i++){
        count[s[i]] += 1;
    }
    for(int i = 0; i < 128; i++){
        if(count[i] >= 3) return false;
    }
    return true;
}
bool check_4(char* s){
    for(int i = 0; i < 7 - 1; i++){
        if(s[i] == s[i + 1] && s[i] == '4'){
            return false;
        }
    }
    return true;
}
 
static inline bool check(char* s){
    return check_1(s) && check_2(s) && check_3(s) && check_4(s);
}
 
int main(){
    int n; scanf("%d", &n);
 
    char s1[32][10], s2[32][10];
    int cnt1 = 0, cnt2 = 0;
    for(int i = 0; i < n; i++){
        char s[10]; scanf("%s", s);
        if(check(s)){
            if(s[2] == '-'){
                strcpy(s1[cnt1++], s);
            }
            else if(s[3] == '-'){
                strcpy(s2[cnt2++], s);
            }
        }
    }
    qsort(s1, cnt1, sizeof(s1[0]), cmp);
    qsort(s2, cnt2, sizeof(s2[0]), cmp);
    for(int i = 0; i < cnt1; i++) printf("%s\n", s1[i]);
    for(int i = 0; i < cnt2; i++) printf("%s\n", s2[i]);
 
}