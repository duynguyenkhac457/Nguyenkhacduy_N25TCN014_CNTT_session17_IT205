def security_log_analyzer():
    """
    Hệ thống phân tích log bảo mật với các chức năng:
    - Làm sạch log
    - Lọc cảnh báo nguy hiểm
    - Mã hóa địa chỉ IP
    """

    raw_logs = []
    processed_logs = []

    def clean_logs(raw_input):
        """
        Làm sạch log bằng translate và tách danh sách bằng split
        """
        table = str.maketrans("", "", "!@#$")
        cleaned = raw_input.translate(table)
        return [log.strip() for log in cleaned.split(";") if log.strip()]

    def load_logs():
        """
        Nhập và làm sạch log thô
        """
        nonlocal raw_logs
        print("--- NẠP DỮ LIỆU LOG ---")
        data = input("Nhập chuỗi log thô (cách nhau bởi dấu ;): ")
        raw_logs = clean_logs(data)
        print(f"Đã làm sạch và lưu {len(raw_logs)} dòng log vào hệ thống.")

    def filter_alert_logs():
        """
        Lọc log ERROR / CRITICAL bằng List Comprehension
        """
        nonlocal processed_logs
        if not raw_logs:
            print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
            return

        processed_logs = [
            log for log in raw_logs
            if "error" in log.lower() or "critical" in log.lower()
        ]

        print(f"Tìm thấy {len(processed_logs)} cảnh báo nguy hiểm:")
        for log in processed_logs:
            print(f"- {log}")

    def mask_ip_logs():
        """
        Mã hóa 2 dải số cuối của địa chỉ IP
        """
        if not raw_logs:
            print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
            return

        if not processed_logs:
            print("Không có log nguy hiểm để mã hóa")
            return

        masked_logs = []

        for log in processed_logs:
            parts = log.split()
            new_parts = []

            for part in parts:
                if "." in part and part.count(".") == 3:
                    ip_parts = part.split(".")
                    masked_ip = ".".join(ip_parts[:2] + ["*", "*"])
                    new_parts.append(masked_ip)
                else:
                    new_parts.append(part)

            masked_logs.append(" ".join(new_parts))

        print("--- MÃ HÓA IP ---")
        print("Báo cáo log an toàn:")
        for index, log in enumerate(masked_logs, start=1):
            print(f"{index}. {log}")

        return masked_logs

    while True:
        print("\n============= SECURITY LOG ANALYZER =============")
        print("1. Nhập và làm sạch dữ liệu Log thô")
        print("2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)")
        print("3. Mã hóa địa chỉ IP (Masking)")
        print("4. Đóng hệ thống")
        print("=================================================")

        choice = input("Chọn chức năng (1-4): ")

        match choice:
            case "1":
                load_logs()
            case "2":
                print("--- LỌC CẢNH BÁO ---")
                filter_alert_logs()
            case "3":
                mask_ip_logs()
            case "4":
                print("Hệ thống đã đóng. Kết thúc phân tích log.")
                break
            case _:
                print("Lựa chọn không hợp lệ")


security_log_analyzer()