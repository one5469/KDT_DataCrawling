import pandas as pd

filename = './hollys_branches.csv'

hollysDF = pd.read_csv(filename, usecols=['위치(시,구)', '주소', '전화번호'])

while True:
    city = input('검색할 매장의 도시를 입력하세요: ')

    if city == 'quit':
        print('종료 합니다.')
        break
    else:
        cityDF = hollysDF[hollysDF['위치(시,구)'].str.contains(city)]
        print('--------------------')
        print('검색된 매장 수: ', cityDF.shape[0])
        print('--------------------')
        cnt = 1
        for i in cityDF.index:
            print(f'[{cnt:>3}]: {cityDF.loc[i][["주소", "전화번호"]].values}')
            cnt += 1
        print('----------------------------------------------------------------------------------------------------')
