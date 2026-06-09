import itertools


def esports_matchmaker():
    """
    Hệ thống bốc thăm và tạo lịch thi đấu Esports
    """

    teams_list = []
    match_schedule = []

    def input_teams():
        """
        Nhập và chuẩn hóa danh sách đội tuyển
        """
        nonlocal teams_list
        print("--- NHẬP DANH SÁCH ---")
        raw_input = input("Nhập các đội (cách nhau bởi dấu phẩy): ")

        teams = [
            team.strip().upper()
            for team in raw_input.split(",")
            if team.strip()
        ]

        teams = list(dict.fromkeys(teams))
        teams_list = teams

        print(f"Đã ghi nhận {len(teams_list)} đội: {teams_list}")

    def create_schedule():
        """
        Tạo lịch thi đấu vòng tròn một lượt
        """
        nonlocal match_schedule

        if len(teams_list) < 2:
            print("Lỗi: Cần tối thiểu 2 đội để tạo lịch thi đấu.")
            return

        pairs = itertools.combinations(teams_list, 2)
        match_schedule = [f"{a} vs {b}" for a, b in pairs]

        print("--- LỊCH THI ĐẤU VÒNG BẢNG ---")
        for index, match in enumerate(match_schedule, start=1):
            print(f"{index}. {match}")

        print(f"Tổng số trận đấu: {len(match_schedule)} trận.")

        return match_schedule

    def generate_match_ids():
        """
        Sinh mã định danh trận đấu
        """
        if not match_schedule:
            print("Vui lòng tạo lịch thi đấu trước khi sinh mã ID.")
            return

        print("--- MÃ TRẬN ĐẤU (MATCH ID) ---")

        for index, match in enumerate(match_schedule, start=1):
            team_a, team_b = match.split(" vs ")

            code_a = f"{team_a[:3]:X<3}"
            code_b = f"{team_b[:3]:X<3}"

            match_id = f"M{index:02d}-{code_a}-{code_b}"
            print(f"Trận {index} ({match}) -> ID: {match_id}")

    while True:
        print("\n============= ESPORTS MATCHMAKER =============")
        print("1. Nhập danh sách Đội tuyển")
        print("2. Tạo lịch thi đấu (Combinations)")
        print("3. Tạo mã trận đấu tự động")
        print("4. Đóng hệ thống")
        print("==============================================")

        choice = input("Chọn chức năng (1-4): ")

        match choice:
            case "1":
                input_teams()
            case "2":
                create_schedule()
            case "3":
                generate_match_ids()
            case "4":
                print("Hệ thống đã đóng. Kết thúc chương trình.")
                break
            case _:
                print("Lựa chọn không hợp lệ")


esports_matchmaker()