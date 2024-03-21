#include <stdio.h>
#include <string.h>

void remove_leading_zeros(char *s){
    int n = strlen(s);

    int first_nonzero_idx = 0;
    for(; first_nonzero_idx < n; first_nonzero_idx++){
        if(s[first_nonzero_idx] != '0') break;
    }

    if(first_nonzero_idx == n){
        s[0] = '0';
        s[1] = '\0';
    }
    else{
        int new_idx = 0;
        for(int i = first_nonzero_idx; i < n; i++){
            s[new_idx++] = s[i];
        }
        s[new_idx] = '\0';
    }
}

int main() {
    char s[1024];
    scanf("%s", s);
    remove_leading_zeros(s);
    printf("%s\n", s);
    return 0;
}
