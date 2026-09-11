1. 상품코드를 입력하면 즉시 재고 수량을 확인해야 하는 재고 관리 데이터
    * 선택한 자료 구조: 딕셔너리
    * 선택 근거: 상품코드라는 키로 즉시 재고 수량이라는 값을 찾아야 하기 때문   
    * 예시코드:   
    ```python
    inventory = {'B0040':25, 'A1004':50}
    product_code = 'B0040'

    stock = inventory.get(product_code, 0)
    print(f"{product_code}의 재고: {stock}개")
    ```

2. 이벤트 응모 고객 명단에서 중복 응모를 제거하고, 기존 회원 명단과의 교집합을 구해야 하는 상황
    * 선택한 자료 구조: 세트(집합)
    * 선택 근거: 중복을 허용하지 않고, 교집합, 합집합과 같은 집합 메서드의 사용이 가능하기 때문
    * 예시코드:   
    ```python
    customer = {'c1', 'c2', 'c999', 'a125', 'b1'} 
    eventin_customer = {'c1', 'c2', 'c3', 'c3'}

    eventin_customer & customer
    ```

3. 월별 매출액을 1월부터 12월까지 순서대로 저장하고 순회하는 데이터
    * 선택한 자료: 리스트
    * 선택 근거: 순서가 고정되어 있고, 순회하는 데이터를 다루기 때문. 리스트는 인덱스를 1~12월에 대응 시킬 수 있어 순차 처리에 유리하다.
    * 예시코드:   
    ```python
    monthly_sales = [100, 150, 200, 150, 300, 400]

    for month, sales in enumerate(monthly_sales, 1):
      print(f"{month}월 매출: {sales}원")
    ```

4. 한 번 발급되면 절대 변경되어서는 안 되는 (위도, 경도) 매장 좌표
    * 선택한 자료 구조: 튜플
    * 선택 근거: 튜플은 삭제나 변경이 불가능하기 때문에, 바뀌면 안되는 자료들을 다룰 때 유용하다.
    * 예시코드:   
    ```python
    store_location = (37.5416, 280.1559)
    lat, lon = store_location

    print(f"위도: {lat}, 경도: {lon}")
    ```

5. 1,000만 줄짜리 웹 서버 접속 로그 파일에서 특정 조건의 줄 수를 세는 작업 (자료구조 + 처리 방식 관점에서 서술)
    * 선택한 자료 구조: iterator
    * 선택 근거: 1000만 줄 로그 파일을 그대로 메모리에 올리면 메모리 사용량이 매우 커지기 때문에 과부하가 올 수 있다. 또, 조건에 맞는 줄 수를 세는 것이기 때문에 별도로 로그를 저장하지 않고도 처리가 가능한 iterator를 활용해 필요할 때마다 한 줄 씩 처리하는 것이 자원 활용 측면에서 효율적이다. 
    * 예시코드:   
    ```python
    count = 0
    with open("file.log", encoding="utf-8") as log_file:
        for line in log_file:                 # 한 줄씩 읽어 메모리 절약
            if "500" in line:
                count += 1
    print(f"500 출현 횟수: {count}")
    ```