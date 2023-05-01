#include <stdio.h>
#include <string.h>

int main(void)
{
    char word[5001];
    int alpha[26] = { 0 };
    int cnt = 0;

    while (gets(word)) {
        for (int i = 0; word[i]; i++) {
            if (word[i] >= 'a' && word[i] <= 'z') {
                alpha[word[i] - 'a']++;
                if (alpha[word[i] - 'a'] > cnt) cnt = alpha[word[i] - 'a'];
            }
        }
    }

    for (int i = 0; i < 26; i++) {
        if (alpha[i] == cnt)
            printf("%c", i + 'a');
    }
    return 0;
}