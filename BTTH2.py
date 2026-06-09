import functools


def ecommerce_analytics():
    """
    Hệ thống phân tích dữ liệu sản phẩm thương mại điện tử
    """

    product_list = [
        "P01-Tai Nghe Bluetooth-550000-4.5",
        "P02-Chuột Không Dây-250000-4.8",
        "P03-Bàn Phím Cơ-850000-4.5",
        "P04-Sạc Dự Phòng-300000"
    ]

    def display_labels():
        """
        Hiển thị tem nhãn sản phẩm
        """
        print("--- DANH SÁCH TEM NHÃN ---")
        template = "Mã: {code:<10} | Tên: {name:<22} | Giá: {price} VND | Rating: {rating}*"

        for item in product_list:
            try:
                code, name, price, rating = item.split("-")
                if not price.isdigit():
                    raise ValueError

                price_fmt = f"{int(price):,}"
                data = {
                    "code": code,
                    "name": name,
                    "price": price_fmt,
                    "rating": rating
                }

                print(template.format_map(data))

            except IndexError:
                print(f"Bỏ qua sản phẩm {item.split('-')[0]} do sai cấu trúc dữ liệu")
            except ValueError:
                print(f"Bỏ qua sản phẩm {item.split('-')[0]} do lỗi giá tiền")

    def sort_products():
        """
        Sắp xếp sản phẩm theo rating giảm dần, giá tăng dần
        """

        def sort_key(item):
            try:
                _, _, price, rating = item.split("-")
                if not price.isdigit():
                    raise ValueError
                return (-float(rating), int(price))
            except (IndexError, ValueError):
                return (float("inf"), float("inf"))

        product_list.sort(key=sort_key)

        print("--- SẮP XẾP SẢN PHẨM ---")
        print("Đã sắp xếp thành công! Cập nhật danh sách:")
        for index, product in enumerate(product_list, start=1):
            print(f"{index}. {product}")

    def calculate_total_value():
        """
        Tính tổng giá trị kho hàng
        """
        prices = []

        for item in product_list:
            try:
                price = item.split("-")[2]
                if price.isdigit():
                    prices.append(int(price))
            except IndexError:
                pass

        total = functools.reduce(lambda a, b: a + b, prices, 0)
        print("--- TỔNG GIÁ TRỊ KHO ---")
        print(f"Tổng giá trị các mặt hàng hiện tại là: {total:,} VND.")

        return total

    while True:
        print("\n============= E-COMMERCE ANALYTICS =============")
        print("1. Hiển thị tem nhãn sản phẩm")
        print("2. Sắp xếp sản phẩm thông minh")
        print("3. Tính tổng giá trị kho hàng")
        print("4. Đóng hệ thống")
        print("================================================")

        choice = input("Chọn chức năng (1-4): ")

        match choice:
            case "1":
                display_labels()
            case "2":
                sort_products()
            case "3":
                calculate_total_value()
            case "4":
                print("Hệ thống đã đóng. Kết thúc phân tích.")
                break
            case _:
                print("Lựa chọn không hợp lệ")


ecommerce_analytics()