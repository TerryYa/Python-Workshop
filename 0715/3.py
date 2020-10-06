import pandas as pd


def main():
    n = int(input())
    cols = ['ID', 'Chinese', 'English', 'Math',
            'Program', 'Algorithm', 'Average']
    df_table = pd.DataFrame(columns=cols)
    for i in range(n):
        tmp = dict()
        while True:
            input_again = False
            datas = input().split(' ')
            for score in datas[1:]:
                if float(score) < 0 or float(score) > 100:
                    print('<<< Please enter again! >>>')
                    input_again = True
                    break
            if not input_again:
                break

        total = 0
        tmp['ID'] = int(datas[0])
        for c, data in zip(cols[1:-1], datas[1:]):
            tmp[c] = data
            total += float(data)
        tmp['Average'] = f'{total / len(cols[1:-1]):.2f}'
        df_table = df_table.append(tmp, ignore_index=True)
    df_table = df_table.sort_values('ID', ascending=True)
    df_table = df_table.sort_values('Average', ascending=False)
    print(df_table)


if __name__ == "__main__":
    main()
