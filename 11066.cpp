int main() {
    for (scanf("%d", &T); T--;) {
        scanf("%d", &N);
        for (int i = 1; i <= N; i++)
            scanf("%d", &novel[i]), psum[i] = psum[i - 1] + novel[i];
        for (int i = 1; i <= N; i++)
            num[i - 1][i] = i;
        for (int d = 2; d <= N; d++) {
            for (int i = 0; i + d <= N; i++) {
                int j = i + d;
                dp2[i][j] = 2e9;
                for (int k = num[i][j - 1]; k <= num[i + 1][j]; k++) {
                    
                    int v = dp2[i][k] + dp2[k][j] + psum[j] - psum[i];
                    if (dp2[i][j] > v)
                        dp2[i][j] = v, num[i][j] = k;
                }
            }
        }
        printf("%d\n", dp2[0][N]);
    }
    return 0;
}
